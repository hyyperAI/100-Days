import os

from flask import Flask, render_template,request, redirect, url_for, flash,abort
from functools import wraps
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from os import environ
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreatePostForm,UserForm
from flask_gravatar import Gravatar
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

SQL_URI=os.environ.get("SQL_URI")
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)
login_manager=LoginManager(app)



##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = SQL_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# create admin_only decorator
def admin_only(func):
    # this wraps the function around original fucnction
    @wraps(func)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id!=1:
            return abort(403)
        # other wise return the function
        return func(*args, **kwargs)
    # return decorated function
    return decorated_function

##CONFIGURE TABLES



class User(db.Model,UserMixin):
    __tablename__="user_details"
    id = db.Column(db.Integer, primary_key=True,)
    name = db.Column(db.String(250), nullable=False)
    user_email = db.Column(db.String(250), unique=True, nullable=False)
    user_password = db.Column(db.String(100), nullable=False)
    

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # relationship
    # parent_name ensure that it refers to Key in user_details.name that is from another table
    # userdetails is the nem of table from another class

    parent_name=db.Column(db.String(250),ForeignKey("user_details.name"),default='',nullable=False)
    userdb=relationship("User",back_populates="blogpostdb")


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()

@app.route('/')
def get_all_posts():
    # return "this is index page"
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts,current_user=current_user)


@app.route('/register',methods=["GET","POST"])
def register():
    form=UserForm()
    if form.validate_on_submit():
        password=generate_password_hash(form.password.data)
        email=form.email.data
        check_user=db.session.query(User).get(email)
        # check wheter the user is already sign in
        if check_user:
            flash("you are already signin")
            return redirect(url_for("login"))
        else:
            new_user=User(name=form.name.data,user_email=form.email.data,user_password=password)
            db.session.add(new_user)
            flash("Thankyou for regitration")
            return redirect(url_for("login"))
    else:
        return render_template("register.html",form=form,current_user=current_user)


@app.route('/login',methods=["POST","GET"])
def login():
    form =UserForm()
    if form.validate_on_submit():
        email=form.email.data
        user=db.session.query(User).filter_by(user_email=email).first()
        # check wheter the user is already sign in
        if  not user :
            flash("Email not found")
            login_user(user)
            return redirect(url_for("about"))


        if not check_password_hash(user.user_password,form.password.data):
            flash("Your password is in correct")
            return redirect(url_for("login"))
        else:
            print("is login")
            login_user(user)
            return redirect(url_for("get_all_posts"))
    print("form")
    return render_template("login.html",form=form,current_user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    print("good")
    return redirect(url_for('get_all_posts'))

@app.route("/search")
def post_by_user():
    blog_author=request.args.get("author")
    all_post=db.session.query(BlogPost).filter_by(author=blog_author)
    return render_template("index.html",all_posts=all_post)

@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post,current_user=current_user)


@app.route("/about")
def about():
    return render_template("about.html",current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html",current_user=current_user)


@app.route("/new-post",methods=["GET","POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user.name,
            date=date.today().strftime("%B %d, %Y")
        )
        with app.app_context():
            db.session.add(new_post)
            db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form,current_user=current_user)


@app.route("/edit-post/<int:post_id>", methods=['POST', 'GET'])
@admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )

    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        # post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form,current_user=current_user)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)

    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000,debug=True)
    with app.app_context():
        print("created")
        db.create_all()
        db.session.commit()
    app.run(debug=True)






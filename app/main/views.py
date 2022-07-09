from flask import render_template,request,redirect,url_for,abort
from . import main
from ..request import get_quotes
from flask_login import login_required,current_user
from ..models import Blog, User, Comment
from .forms import UpdateProfile,CommentForm,BlogForm,UpdateBlog
from .. import db,photos
import markdown2 
from ..email import mail_message

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quotes = get_quotes()
    title = 'Pesonal Blog'
    blogs = Blog.get_blogs()
    return render_template('index.html', title = title, blogs = blogs, quotes = quotes)

@main.route('/blog/<int:id>')
def blog(id):
    '''
    View blog page function that returns the blog details page and its data
    '''
    blog = Blog.query.get(id)
    title = f'{blog.title}'
    comments = Comment.query.filter_by(blog_id = id).all()
    return render_template('blog.html',title = title,blog = blog,comments = comments)

@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    '''
    Function that creates new pitches
    '''
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        new_blog= Blog(title = title, text = text, user = current_user)

        new_blog.save_blog()
        return redirect(url_for('.index'))
    title = 'Create Blog'
    return render_template('new_blog.html',title = title, blog_form = form)

@main.route('/update_blog/<int:id>', methods=['GET','POST'])
@login_required
def update_blog(id):
    form = UpdateBlog()
  
    if form.validate_on_submit():
        blog = Blog.query.filter_by(id=id).first()
        text=form.text.data
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index', id=id, text=text))
    return render_template('update_blog.html', update_form=form)

@main.route('/delete_blog/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_blog(id):
    blog = Blog.query.get(id)

    if blog is None:
        abort(404)

    db.session.delete(blog)
    db.session.commit()
    return redirect (url_for('main.index'))

@main.route('/blog/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    blog = Blog.query.get(id)

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(blog_id=blog.id,comment = comment, user = current_user)
        new_comment.save_comment()
        return redirect(url_for('.blog',id = blog.id ))

    title = f'{blog.title} comment'
    return render_template('new_comment.html',title = title, comment_form=form, blog = blog)

@main.route('/delete_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_comment(id):
    comment =Comment.query.get(id)

    if comment is None:
        abort(404)

    db.session.delete(comment)
    db.session.commit()
    return redirect (url_for('.index'))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comment/<int:id>')
def single_comment(id):
    comment = Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.comment,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html',comment = comment,format_comment = format_comment)

@main.route('/single_blog/<int:id>')
def single_blog(id):
    blog = Blog.query.get(id)
    if blog is None:
        abort(404)
    format_blog = markdown2.markdown(blog.text,update_blog.text,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('single_blog.html',blog = blog,format_blog=format_blog)




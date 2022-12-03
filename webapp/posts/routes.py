from flask import render_template, url_for, flash, redirect, request, abort,Blueprint
from webapp.posts.forms import PostForm
from webapp.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from webapp import db
from webapp.db_models import Post
from flask_login import current_user,login_required




posts = Blueprint('posts', __name__)







@posts.route("/post/new", methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f"Post has been created!", 'success')
        return redirect(url_for('main.home'))

    return render_template('create_post.html', form=form)

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post, legend='New Post')


@posts.route("/post/<int:post_id>/update", methods=["GET", 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        flash(f"Updating post!", 'success')
        db.session.commit()
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content


    return render_template('create_post.html', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f"Post has been deleted.", 'success')
    return redirect(url_for('main.home'))




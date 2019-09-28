
from flask import render_template,request,redirect,url_for,abort
from . import main
# from ..request import get_movies,get_movie,search_movie
from .forms import BlogForm,CommentForm,UpdateProfile
from .. import db,photos
from ..models import User,Blog,Comment
from flask_login import login_required,current_user
import markdown2
 




# Views
@main.route('/', methods = ['GET','POST'])
def index():

   
    blog = Blog.query.filter_by().first()
    title = 'HomePage'
    Music = Blog.query.filter_by(category="music")
    Lifestyle = Blog.query.filter_by(category = "lifestyle")
    Sports= Blog.query.filter_by(category = "sports")
    Fashion = Blog.query.filter_by(category = "fashion")

    return render_template('index.html', title = title, blog = blog, music=music, lifestyle= lifestyle, sports = sports, fashion = fashion)
    

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
 
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        user_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_blog = Blog(user_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('blog.html',form=form)



@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comment.html', form = form, comment = all_comments, pitch = pitch )



@main.route('/user/<uname>')
@login_required
def profile(uname):
 user = User.query.filter_by(username = uname).first()
 get_pitches = Pitch.query.filter_by(user_id = current_user.id).all()
 if user is None:
     abort(404)
 return render_template("profile/profile.html", user = user, pitches_content = get_pitches)

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



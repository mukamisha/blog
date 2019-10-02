from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager




    
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path =  db.Column(db.String(255))
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    '''
    a blog class
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment',backref='blog',lazy='dynamic')


    
    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.order_by(blog_id=id).desc().all()
        return blogs

    def delete_blog(self):
       db.session.delete(self)
       db.session.commit()

    def __repr__(self):
        return f'Blog {self.description}'



class Comment(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    description = db.Column(db.Text)

    
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"

class Random_Quotes:
  '''
  a class to define quote objects
  '''
  def __init__(self,id,author,quote,permalink):
      self.id =id
      self.author = author
      self.quote = quote
      self.permalink = "http://quotes.stormconsultancy.co.uk/quotes/31"









        

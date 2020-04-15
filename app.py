from flask import Flask , request, render_template
#from flask_sqlalchemy import SQLAlchemy
import sys


app = Flask(__name__)

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zzazzlogoeqjwv:42c24db7e704bf9cff26b54093f73e28d47dcc66b186fbfd773fe945636b9401@ec2-107-21-108-37.compute-1.amazonaws.com:5432/du1cdjsto37gr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Result(db.Model):
    __tablename__ = 'result'
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.String())
    emotions = db.Column(db.String())
  
 
    def __init__(self, playlist_id, emotions):
        self.playlist_id = playlist_id
        self.emotions = emotions
 '''
 
@app.route('/', methods=['GET','POST'])
def index():
    '''
    if request.method == 'POST':
        spotid = request.form['text'][17:]
    '''

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

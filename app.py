from flask import Flask , request, render_template
#from flask_sqlalchemy import SQLAlchemy
import sys
import subprocess

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
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    dels=[3,14,26]
    vidsaddr = []
    for i in range(1,34):
        if i not in dels:
            vidsaddr.append(str(i)+".mp4")
    '''
    res=""
    if request.method == 'POST':
        plink = request.form['text']
        res = subprocess.check_output(["wget","-O","static/p.mp4", plink])
        res = subprocess.check_output(["rm","-f","static/p.mp4"])
        res = subprocess.check_output(["youtube-dl","-o","static/p.mp4", plink])   
        print(res)
        
        return render_template('portfolio.html', vids=vidsaddr)
        
    '''
    print(vidsaddr)
    return render_template('portfolio.html', vids=vidsaddr)
    

@app.route('/mpor')
def por():

    return render_template('index.html', link="/static/p.mp4")


if __name__ == '__main__':
    app.run(debug=True)

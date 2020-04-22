from flask import Flask , request, render_template,redirect,url_for
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
#app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return redirect(url_for('vidspage',pagenum=1))


@app.route('/vids/<int:pagenum>')
def vidspage(pagenum):


    dels=[3,14,26,35,37,38,39,40,43,45,59,]
    vidsaddr = []
    
    for i in range(1,101):
        if i not in dels:
            vidsaddr.append(str(i)+".mp4")
            
                        
    if pagenum==1:
        vidsaddr=vidsaddr[:16]
    if pagenum==2:
        vidsaddr=vidsaddr[16:32]
    if pagenum==3:
        vidsaddr=vidsaddr[32:48]
    if pagenum==4:
        vidsaddr=vidsaddr[48:64]
    if pagenum==5:
        vidsaddr=vidsaddr[64:80]
    if pagenum==6:
        vidsaddr=vidsaddr[80:96]
    if pagenum==7:
        vidsaddr=vidsaddr[96:112]
            
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

    return render_template('portfolio.html', vidsaddr=vidsaddr,pagenum=pagenum)
    

@app.route('/mpor')
def por():

    return render_template('index.html', link="/static/p.mp4")


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask , request, render_template,redirect,url_for,jsonify
import sys
import subprocess
import json
from threading import Thread

app = Flask(__name__)




#Long_wrok
def work(plink):

    res=""
    title=""
    
    title = subprocess.check_output(["youtube-dl","--get-filename", plink])
    title = str(title).replace("b'","").replace("\\n'","")
    res = subprocess.check_output(["youtube-dl","-o","static/"+title, plink])    
   
    print("!!!!!!!!!!!!!!",res,"TITLE:",title)
       
    with open('static/result.txt','w') as file:
        file.write("{'current': 99.99, 'total': 100, 'status':'"+title+"','result': 42}")


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
            

    return render_template('portfolio.html', vidsaddr=vidsaddr,pagenum=pagenum)
    

@app.route('/stream' , methods=['GET', 'POST'])
def stream():

    with open('static/result.txt','w') as file:
        file.write("")
        
    
    if request.method == 'POST':
        plink = request.form['vidurl']
        thread = Thread(target=work,args=(plink,))
        thread.daemon = True
        thread.start()
        return render_template('index.html')
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/status')
def taskstatus():

    data = ""
    with open('static/result.txt','r') as file:
        data = file.read()
        if data !="":
            response = json.loads(data.replace("'","\""))
            return response
        else:
            return {
            'state': 'PENDING',
            'current': 10,
            'total': 100,
            'status': 'Pending...'
        }
 
 
if __name__ == '__main__':
    app.run(debug=True,threaded=True)

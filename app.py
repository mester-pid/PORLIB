from flask import Flask , request, render_template,redirect,url_for,jsonify
import sys
import subprocess
import json
from celery import Celery

app = Flask(__name__)


celery = Celery(app.name)
celery.conf.update(app.config)

celery.conf.update({
    'broker_url': 'filesystem://',
    'broker_transport_options': {
        'data_folder_in': 'app/broker/out',
        'data_folder_out': 'app/broker/out',
        'data_folder_processed': 'app/broker/processed'
    },
    
    'result_persistent': False,
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json']})


#Long_wrok
@celery.task(bind=True)
def work(self,plink):

    res=""
    title=""
    
    title = subprocess.check_output(["youtube-dl","--get-filename", plink])
    title = str(title).replace("b'","").replace("\\n'","")
    res = subprocess.check_output(["youtube-dl","-o","static/"+title, plink])    
   
    print("!!!!!!!!!!!!!!",res,"TITLE:",title)
       
    with open('static/result.txt','w') as file:
        file.write("{'current': 99.99, 'total': 100, 'status':'"+title+"','result': 42}")
    
    return {'current': 99.99, 'total': 100, 'status': title,'result': 42}


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
        
    if request.method == 'GET':
        return render_template('index.html')

    return redirect(url_for('stream'))

 

@app.route('/longtask', methods=['POST'])
def longtask():
    if request.method == 'POST':
        plink = request.form['vidurl']
        task = work.apply_async([plink])
    
    return jsonify({}),202, {'Location': url_for('taskstatus',
                                                  task_id=task.id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
    #return "done"

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
    app.run(debug=False)

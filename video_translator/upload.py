# from crypt import methods
from flask import Blueprint,render_template,request,flash,redirect,url_for,make_response
import os
from .speech_text import run
from .trans import trans
from .add_subs import add_subs
from config.definitions import ROOT_DIR

upload = Blueprint('upload',__name__)

@upload.route('/upload',methods= ['GET',"POST"])
def upload_page():
    if request.method == 'POST':
       #Get the video file
       f = request.files['file']
       # get the language they want to translate it to.
       lang = request.form.get('lang')

       #path to store the incoming video files
      
       store = ROOT_DIR+r"/static/video"
       path = os.path.join(store,f.filename)
       print(path)
       f.save(path)

       #Speech to text
       run(path)

       #Translate extracted text
       trans(lang)

       #add subs to the video
       name = f.filename.split('.')[0]
       add_subs(path,"static/Ai_video/"+name+"_subs"+"_"+lang)

       #Text to speech
      #  tts(lang,name)
       return render_template('output.html',out = "static/Ai_video/"+name+"_subs"+"_"+lang+".mp4")

    flash("Upload Again")
    return redirect(url_for('home.page'))
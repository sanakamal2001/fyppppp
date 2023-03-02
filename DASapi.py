import json
import werkzeug
from flask import Flask,request,jsonify
from datamodel import DASlabel
import speech_recognition
app=Flask(__name__)

@app.route('/api',methods=['GET'])
def DAS_text():
    print("in DAS function")
    query=str(request.args['text'])
    label=DASlabel(query)
    d={}
    d['label']=label    
    return jsonify(d)

# @app.route('/video',methods=['POST'])
# def convertvideo():
#   if(request.method=="POST"):
      
#     videofile = request.files["video"]
#     print("after videofile")
#     filename = werkzeug.utils.secure_filename(videofile.filename)
#         # print("\nReceived video File name : " + videofile.filename)
#     videofile.save(filename)
    
#     print("file saved!!!")
#     # text=videototext(filename)
#     label=DASlabel(text)
#     d={}
#     d['label']=label
#     return jsonify(d)

if __name__=="__main__":
    app.run()
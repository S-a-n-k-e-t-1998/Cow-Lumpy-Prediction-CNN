# from crypt import methods
# from re import template
# import tensorflow as tf
# from tensorflow.keras import models, layers
import email
import matplotlib.pyplot as plt
from IPython.display import HTML
import seaborn as sns
# from tensorflow import keras
from flask import Flask,jsonify,render_template,request

app=Flask(__name__)


# model= keras.models.load_model('CNN.h5')

@app.route('/',methods=['POST','GET'])
def home():
    email=request.form.get('email')
    mobile=request.form.get('mobile')
    comments=request.form.get('comments')
    # img=request.form['img']
    print(email)
    print(mobile)
    print(comments)
    # print(img)
    return render_template('index1.html')



if __name__=='__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 13:27:45 2017

@author: firefly
"""

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import challenge2.airlines as ra







app = Flask(__name__)


@app.route('/')

def main():
    return render_template('index.html') 
    

    
@app.route('/challenge2/', methods=['POST','GET'] )

def welcome2():
    return render_template('challenge2/main.html') 
    

@app.route ('/challenge2/search', methods=['POST'])  
def search2():
    code=request.form['code']
    fr=request.form['from']
    to=request.form['to']
    if(ra.validateCode(code)):
        return render_template('challenge2/code.html',fr=fr,to=to)
    else:
        return render_template('challenge2/main.html',err='Incorrect Code!')
   
    
app.run(host='0.0.0.0', port=8080)
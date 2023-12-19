from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import datetime
import os
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


f = open('model.pckl', 'rb')
data = pickle.load(f)
f.close()
scaler = data[0]
scaler1 = data[1]
label_encoder = data[2]
cols = data[3]
xg_model = data[4]

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def Aboutus(request):
    if request.method == 'GET':
       return render(request, 'Aboutus.html', {})

def UserLoginAction(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username == 'admin' and password == 'admin':
            context= {'data':'welcome '+username}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'Invalid login details'}
            return render(request, 'UserLogin.html', context)

def Predict(request):
    if request.method == 'GET':
        return render(request, 'Predict.html', {})
   
def PredictAction(request):
    if request.method == 'POST':
        global uname
        video_id = request.POST.get('t1', False)
        video_title = request.POST.get('t2', False)
        published_at = request.POST.get('t3', False)
        channel_id = request.POST.get('t4', False)
        channel_title = request.POST.get('t5', False)
        category_id = request.POST.get('t6', False)
        trending_date = request.POST.get('t7', False)
        tags = request.POST.get('t8', False)
        view_count = request.POST.get('t9', False)
        likes = request.POST.get('t10', False)
        dislikes = request.POST.get('t11', False)
        thumbnail = request.POST.get('t12', False)
        comments_disabled = request.POST.get('t13', False)
        rating_disabled = request.POST.get('t14', False)
        description = request.POST.get('t15', False)
        category_id = int(category_id.strip())
        view_count = int(view_count.strip())
        likes = int(likes.strip())
        dislikes = int(dislikes.strip())

        columns = ['video_id', 'title', 'publishedAt', 'channelId', 'channelTitle', 'categoryId', 'trending_date', 'tags', 'view_count', 'likes', 'dislikes',
                   'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'description']
        values = []
        values.append([video_id, video_title, published_at, channel_id, channel_title, category_id, trending_date, tags, view_count, likes, dislikes, thumbnail,
                       comments_disabled, rating_disabled, description])
        values = pd.DataFrame(values, columns = columns)
        temp = values.values
        for i in range(len(cols)):
            try:
                values[cols[i]] = pd.Series(label_encoder[i].transform(values[cols[i]].astype(str)))
            except Exception:
                le = LabelEncoder()
                values[cols[i]] = pd.Series(le.fit_transform(values[cols[i]].astype(str)))
                pass
        values = values.values
        values = scaler.transform(values)
        predict = xg_model.predict(values)
        predict = predict.reshape(-1, 1)
        predict = scaler1.inverse_transform(predict)
        predict = predict[0]
        output = "Test Data = "+str(temp[0])+" Predicted Comment Counts = "+str(predict[0])        
        context= {'data': output}
        return render(request, 'Predict.html', context)   
        



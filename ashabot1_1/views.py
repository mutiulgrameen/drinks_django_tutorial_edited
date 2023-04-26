from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework   import generics 
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import CreateAPIView
import sqlite3      # database
import sys
sys.path.insert(0, 'D:\chatbot\ASAbot-master')
from ashabot1 import chat_resp
from django.views.decorators.csrf import csrf_exempt
#import requests # for html





def add2_db(q, a, conf):
    if a == "I am sorry, but I do not understand.":
        flag = True
    else:
        flag = False
    database = 'D:\\chatbot\\ASAbot-master\\db_response.db'
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bot_response (Question, Answer, Conf, Flag) VALUES (?, ?, ?, ?)", (q, a, conf, flag))
        conn.commit()
        

def Welcome(request):
    if request.method == 'POST':
        query = request.POST['query']
    
        data_out, conf = chat_resp(query)
        response_text = data_out.text
        
        add2_db(query, response_text, conf)
        return render(request, 'index.html', {'query':query, 'ans':response_text})
    return render(request, 'index.html')

    

class ASHABot1(APIView):
    def __init__(self):
        self.data = ['Please state your microfinance-related query']
    
    def get(self, requests, format=None):
        return Response(self.data)
    
    def post(self, requests, format = None):
        data = requests.data   
        data_in = data.get("data", None)
        
        data_out, conf = chat_resp(data_in)
        response_text = data_out.text
        add2_db(data_in, response_text, conf)      # adding to db

        return Response({                     # changed
           'Response':200,
           "Data" :str(data_out),
           "Accuracy" :conf
        })
       

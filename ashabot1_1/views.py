from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
#from .models import Person 
#from .serializer import Personserializers
from rest_framework import status
from rest_framework   import generics 
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import CreateAPIView

import sqlite3      # database
#from E:\grameen\chatbot\my_code_1\ashabot1 import chat_reponse
# importing sys

import sys

sys.path.insert(0, 'D:\chatbot\ASAbot-master')
from ashabot1 import chat_resp

from django.views.decorators.csrf import csrf_exempt
import requests # for html

def index(request):
    messages = []
    context = {'messages': messages}
    return render(request, 'ashabot1_1/index.html', context)

def fast_app(request):
    return HttpResponse('<h1> Automated Sentient Health Assistant Robot (ASHABot1) </h1>')

def add2_db(q, a):
    #print(type(q))
    #print(type(a))
    database = 'D:\\chatbot\\ASAbot-master\\db_response.db'
    #database = 'db_response.db'
    with sqlite3.connect(database) as conn:
        #Id = 0
        cursor = conn.cursor()
               # cursor.close()
        # conn.close()
        # cursor = conn.cursor()
        #sql = "INSERT INTO wins (UName) VALUES ('{}')".format(slot_value)
        #query = 'INSERT INTO bot_response (Question, Answer) VALUES (?, ?)'
        #data = (q, a)
        #cursor.execute(query, data)
        cursor.execute("INSERT INTO bot_response (Question, Answer) VALUES (?, ?)", (q, a))
        conn.commit()
        #Id = Id + 1
        # cursor.close()
        # conn.close()
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM {}'.format(table))     # change 'Faq' with name of table
#         rows = cursor.fetchall()
#         b = []
#         for row in rows:
#             c = list(row)
#             a = c.pop(0)    # a contains id which we do not need
#         #b = []
#             b.append(c)
#         #print(row)
# #b = divByComa(b)        
#     b = np.array(b)
#     b = np.hstack(b)
#     b = b.tolist()
#    return()
"""
def my_view(requests):
    if requests.method == 'POST':

        data = requests.data   
        data_in = data.get("data", None)
        ###
#        asha = "E:\grameen\chatbot\my_code_1\ashabot1.py"
        data_out, conf = chat_resp(data_in)
        response_text = data_out.text
        add2_db(data_in, response_text)

        headers = {
            'Content-type': 'application/json'
        }
        response = requests.post('http://http://127.0.0.1:8000/', json=data, headers=headers)
        answer = response.json()['answer']
        return render(requests, 'index.html', {'answer': answer})
    else:
        return render(requests, 'index.html')

"""

"""
def my_view(requests):
        if requests.method == 'POST':

            data = requests.data   
            data_in = data.get("data", None)
        ###
#        asha = "E:\grameen\chatbot\my_code_1\ashabot1.py"
            data_out, conf = chat_resp(data_in)
            response_text = data_out.text
            add2_db(data_in, response_text)

            headers = {
                'Content-type': 'application/json'
            }
            response = requests.post('http://http://127.0.0.1:8000/', json=data, headers=headers)
            answer = response.json()['data']
            return render(requests, 'index.html', {'answer': answer})
        else:
            return render(requests, 'index.html')
    
"""

def Welcome(request):
    if request.method == 'POST':
        query = request.POST['query']
    #print(username)
    # chatbot response
        data_out, conf = chat_resp(query)
        response_text = data_out.text
        #print(response_text)
        add2_db(query, response_text)
        return render(request, 'index.html', {'query':query, 'ans':response_text})
    return render(request, 'index.html')
#def Chat1(request):
    

class ASHABot1(APIView):
    def __init__(self):
        self.data = ['Please state your mental health query']
    
    def get(self, requests, format=None):
        return Response(self.data)
    
    def post(self, requests, format = None):
        data = requests.data   
        data_in = data.get("data", None)
        ###
#        asha = "E:\grameen\chatbot\my_code_1\ashabot1.py"
        data_out, conf = chat_resp(data_in)
        response_text = data_out.text
        add2_db(data_in, response_text)      # adding to db

        #return render(requests, 'index.html')   # changed

#        print(data_out.type())

#        Name = data.get("Name", None)
#        Age = data.get("Age", None)
        #print("Data Received : {}".format(data))
#        return Response({"Desired File" : data_out})
        
        return Response({                     # changed
           'Response':200,
           "Data" :str(data_out),
           "Accuracy" :conf
        })
       
"""




from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Person
from .serializer import PersonSerializers
from rest_framework import generics

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class PersonView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('id', 'name')
"""

"""
class PersonView(APIView):

    def get(self, request):
        mdata = Person.objects.all()
 #       print("====", mdata)
        serializer = PersonSerializers(mdata, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            serializer = PersonSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
class Youtube(APIView):

    def __init__(self):
        self.data = ["Soumil"]

    def get(self, requests, format=None):
        return Response({"Message":self.data})
 #       return Response({"Message":"GET WORKS "})

    def post(self, requests, format=None):
        data = requests.data
        Name = data.get("Name", None)
        self.data.append(Name)

        return Response({
            'Response':200,
            "Data":Name,
            "Message":"Item was added to DataBase"})

    def put(self, requests, format=None):
        MyData = requests.data
        return Response(
            {"Response": "PUT WORKS "}
        )
"""

"""
        print("Data Received : {}".format(data))
        return Response({
            'Response':200,
            "Message":data})
"""



# Create your views here.
#def index(request):

#    return HttpResponse("<h1>Hello World</h1>")
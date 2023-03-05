from django.shortcuts import render, HttpResponse
import pyrebase


config={
  "apiKey": "AIzaSyA67PdB5S5ljBXXrdePtuQJ2ylBUOF6zWw",
  "authDomain": "dhtt-8a950.firebaseapp.com",
  "databaseURL": "https://dhtt-8a950-default-rtdb.firebaseio.com/",
  "projectId": "dhtt-8a950",
  "storageBucket": "dhtt-8a950.appspot.com",
  "messagingSenderId": "931655632276",
  "appId": "1:931655632276:web:098b43c57446c4adcbbb81",
 

}

# Create your views here.


firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()

valuebase={
        "channel_bool":"channel_bool",
        "channel_double":"channel_double",
        "channel_float":"channel_float",
        "channel_int":"channel_int"

    }


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def team(request):
    return render(request, 'team.html')
def datalist(request):
    return render(request, 'datalist.html')
    
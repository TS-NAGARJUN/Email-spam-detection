from django.shortcuts import render
from django.http import HttpResponse
import os
import joblib

model1 = joblib.load(os.path.dirname(__file__)+"\\myModel1.pkl")
model2 = joblib.load(os.path.dirname(__file__)+"\\mySVCModel1.pkl")

# Create your views here.
def index(request):
    return render(request,'index.html')

    
def checkSpam(request):
    if request.method == "POST":
        algo = request.POST.get("algo")
        rawdata = request.POST.get("rawdata")

        if algo == "algo1":
            finalans = model1.predict([rawdata])[0]
        elif algo == "algo2":
            finalans = model2.predict([rawdata])[0]
        else:
            finalans = "spam"  # Fallback in case of unknown algo

        return render(request, 'output.html', {"answer": finalans})
    
    return render(request, 'index.html')  # For GET request

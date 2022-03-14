
from urllib import request
from urllib.parse import parse_qs
from django.http import HttpResponse

from django.shortcuts import redirect, render
from mainpage.models import mainpageinfo,feedback
import joblib

import pandas as pd
import datetime

nd=pd.read_csv('testing.csv')

def input_argument(inpts):
    #cols.clear()
    cols=nd.columns
    cols=cols.tolist()
    del cols[132]
    
    for i in range(len(cols)):
        for j in range(len(inpts)):
            if cols[i]==inpts[j]:
                cols[i]=1
        if cols[i]!=1:
            cols[i]=0
    return cols


def myproject(request):
    return render(request,"myproject.html")
    


def home(request):
    '''
    if request.method=='POST':
        if request.POST.get('symp1') and request.POST.get('symp2') and request.POST.get('symp3') and request.POST.get('symp4') and request.POST.get('symp5'):
            saverecord=mainpageinfo()
            saverecord.symptm1=request.POST.get('symp1')
            saverecord.symptm2=request.POST.get('symp2')
            saverecord.symptm3=request.POST.get('symp3')
            saverecord.symptm4=request.POST.get('symp4')
            saverecord.symptm5=request.POST.get('symp5')
            saverecord.save()
            return render(request,"home.html")
    else:'''
    current_time = datetime.datetime.now()

    if request.method=='POST':
        if request.POST.get('fn') and request.POST.get('ln') and request.POST.get('edres') and request.POST.get('sgsns'):
            fdback=feedback()
            fdback.first_name=request.POST.get('fn')
            fdback.last_name=request.POST.get('ln')
            fdback.email_adrs=request.POST.get('edres')
            fdback.suggestions=request.POST.get('sgsns')
            fdback.date_time=current_time
            fdback.save()
            return render(request,"home.html")
    else:
        return render(request,"home.html")


    

    

    

def result(request):
    cls=joblib.load('finalized_model.sav')
    print('hello')
    ls=[]
    ls.append(request.POST['symp1'])
    ls.append(request.POST['symp2'])
    ls.append(request.POST['symp3'])
    ls.append(request.POST['symp4'])
    ls.append(request.POST['symp5'])
    
    ip=[]
    ip.append(input_argument(ls))
    print(ip[0])

    ans=cls.predict(ip)
    current_time = datetime.datetime.now()

    if request.method=='POST':
        if request.POST.get('symp1') and request.POST.get('symp2') and request.POST.get('symp3') and request.POST.get('symp4') and request.POST.get('symp5'):
            saverecord=mainpageinfo()
            saverecord.symptm1=request.POST.get('symp1')
            saverecord.symptm2=request.POST.get('symp2')
            saverecord.symptm3=request.POST.get('symp3')
            saverecord.symptm4=request.POST.get('symp4')
            saverecord.symptm5=request.POST.get('symp5')
            saverecord.Disease=ans
            saverecord.date_time=current_time
            saverecord.save()
            return render(request,"result.html",{'ans':ans})
    else:
        return render(request,"result.html",{'anss':ans})


def login(request):
    return render(request,"login.html")
    
def sqldta(request):
    if request.method=='POST':
        if request.POST.get('eml'):
            email=request.POST.get('eml')
            password=request.POST.get('pass')
            if email=='xyz@gmail.com' and password=="123":
               resultdisplay=mainpageinfo.objects.all()
               return render(request,"sqldta.html",{'mainpageinfo':resultdisplay})
            else:
                return render(request,"login.html")
          
            
        else:
            return render(request,"login.html")

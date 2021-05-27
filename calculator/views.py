from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    q={
        'ans':False,
        'error':False
    }
    if req.method=='GET':
        return render(req,'calculator/calculator.html',context=q)
    elif req.method=='POST':
        q['query']=req.POST['query']
        try:
            q['ans']=eval(q['query'])
        except:
            q['error']=True
        return render(req,'calculator/calculator.html',context=q)
        
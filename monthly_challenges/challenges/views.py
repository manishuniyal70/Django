from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def index(request, month_int):
    return HttpResponse(month_int)
    

d = {"january":"jan", 
    "feburary":"feb",
    "march":"mar", 
    "april":"apr",
    "may":"my",
    }


def redirect(request, month_int):
    k = list(d.keys())
    
    return  HttpResponseRedirect("/challenges/"+ k[month_int]  )
        
    
    
def hybrid(request, month):
    res = None
    
    if month=="march":
        res  = "march valid"
    elif month=="may":
        res  = "may valid"
    else :
        return HttpResponseNotFound("404 - Month Not found.")
    return HttpResponse(res)    
    
   
    
    
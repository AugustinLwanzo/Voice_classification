from django.shortcuts import render
import joblib
# Create your views here.
def voice(request):
	return render(request,'index.html')

def result (request):
    prediction=joblib.load('voice_model.sav')
    x=[]
    x.append(request.GET['meanfreq'])
    x.append(request.GET['median'])
    x.append(request.GET['centroid'])
    x.append(request.GET['meanfun'])
    x.append(request.GET['maxdom'])
    
    res=prediction.predict([x])
	#res=prediction.predict([list(map(float,x))])
	#a=int(res)
    return render(request, 'result.html',{'res':res}) 

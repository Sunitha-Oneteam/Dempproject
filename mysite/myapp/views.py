from django.shortcuts import render
from django.http import HttpResponse



def home(request):
	#return HttpResponse("Hello World")
	return render(request,"index1.html")

def display(request):
	name=int(request.POST["txt1"])
	res="Welcome "+name
	return render(request,'index1.html',{"msg":res}) #json



















	#dic1={}
	#dic1["Key"]="Welcome"
	#return render(request,'index.html',{"Key":"Welcome"})
	#return render(request,'sample.html')

def display(request):
	name=request.POST["txt1"]
	return render(request,"sample.html",{"msg":"Welcome"+" "+name})
'''













'''
def add(request):
	firstno=int(request.GET["num1"])
	secno=int(request.GET["num2"])
	res=firstno+secno
	return render(request,"hello.html",{"result":res})
'''
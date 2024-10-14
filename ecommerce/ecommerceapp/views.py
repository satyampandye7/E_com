from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request,"index.html")


def contect(request):
  return render(request,"contect.html")


def about(request):
  return render(request,"about.html")


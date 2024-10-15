from django.http import HttpResponse
from django.shortcuts import render
from .models import place

# Create your views here.
#def home(request):
   # return render(request, 'home.html')


#def about(request):
 #   return render(request, 'about.html')


# def addition (request):
#   return render(request,"RESULT.html")

#def contact(request):
 #   return HttpResponse("hello am contact")


#def detail(request):
 #   name = "India"
  #  return render(request, "detail.html", {'obj': name})


#def thank(request):
 #   return HttpResponse("THANK you for watching")


#def addition(request):
#    x = int(request.GET['num1'])
#    y = int(request.GET['num2'])
#    res=x + y,x - y,x * y,x / y
#    return render(request, "RESULT.html", {'result': res})


#def demo(request):
#    return render(request,"index.html")
def demo(request):
    obj = place.objects.all()
    return render(request,"index.html",{'result':obj})

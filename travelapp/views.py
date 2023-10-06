from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.
def demo(request):
    # return HttpResponse('<h1 style="color:red;text-align:center"> HELLO WORLD</h1>')
    obj = place.objects.all()
    obj1= team.objects.all()
    return render(request, "index.html", {'result': obj,'new':obj1})

# def about(request):
# return render(request,"about.html")

# def contact(request):
# return HttpResponse("IAM CONTACT")
# def addition(request):
# x=int(request.GET['num1'])
# y=int(request.GET['num2'])
# res=x+y
# return render(request,"result.html",{'result':res})

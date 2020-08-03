from django.shortcuts import render
from demo.models import User

# Create your views here.
def form(request):
    return render(request, "resultpage.html")

def store(request):
    data = {
        'name': request.POST.get('name'),
        'email': request.POST.get('email')
    }
    p=User(name=request.POST.get('name'), email=request.POST.get('email'))
    p.save()
    return render(request, "show.html", data)
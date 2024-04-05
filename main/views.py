from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    data =  {
        'title': 'Home page2',
        'values': ["Sharapat", "Goha", "Dinosh"],
        'obj': {
            'name': '<NAME>',
            'email': '<EMAIL>',
            'phone': '0123456789'

        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
# Create your views here.

from django.shortcuts import render
from .forms import HashForm

# Create your views here.
def home(request):
    return render(request, 'hashing/home.html')

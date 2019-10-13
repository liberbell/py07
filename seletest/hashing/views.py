from django.shortcuts import render
from .forms import HashForm

# Create your views here.
def home(request):
    forms = HashForm()
    return render(request, 'hashing/home.html', {'form':form})

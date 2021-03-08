from django.shortcuts import render
from myapp.models import *

# Create your views here.
def index(request):
    data1 = Slider.objects.all()
    dataaa = Post.objects.all()

    sliderdata ={
        'slidedata':data1,
        'data2':dataaa,
    }

    return render(request, 'base.html', sliderdata)

def contact(request):
    return render(request, 'contact.html')
from django.shortcuts import render
from .models import Place
from .models import Team

# Create your views here.
def demo(request):
    abc=Place.objects.all()
    cdf=Team.objects.all()

    return render(request,"index.html",{'hello':abc, 'hai':cdf})


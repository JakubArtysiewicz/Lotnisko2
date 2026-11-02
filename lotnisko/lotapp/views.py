from django.shortcuts import render

from .models import Odloty
def index(request):
    odloty = Odloty.objects.all()
    return render(request, 'lotapp/index.html', context={'odloty': odloty})
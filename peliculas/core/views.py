from django.shortcuts import render

# Create your views here.

context = { 
        "data" : ['caratula1','caratula2', 'caratula3', 'caratula4','caratula6','caratula4','caratula4'], 
    } 

def home(request):


    return render(request, 'core/home.html', context)


def galeria(request):


    return render(request, 'core/galeria.html', context)

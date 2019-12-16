from django.shortcuts import render

# Create your views here.

def home_view(request):
    kullanici = {
        'isim': 'Furkan',
    }

    return render(request, 'home.html', kullanici)
    


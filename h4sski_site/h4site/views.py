from django.shortcuts import render


def index(request):
    
    context = {
        'nickname': 'h4sski',
    }
    return render(request, 'index.html', context)
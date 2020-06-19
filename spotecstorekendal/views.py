from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Spotec Store - Kendal'
    }
    return render(request, 'index.html', context)

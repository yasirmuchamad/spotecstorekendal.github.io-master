from django.shortcuts import render

# Create your views here.
def running(request):
    context = {
        'title':'Category - Running',
    }
    return render(request, 'category/running.html', context)

def walking(request):
    context = {
        'title':'Category - Walking',
    }
    return render(request, 'category/walking.html', context)

def badminton(request):
    context = {
        'title':'Category - Badminton',
    }
    return render(request, 'category/badminton.html', context)

def tennis(request):
    context = {
        'title':'Category - Tennis',
    }
    return render(request, 'category/tennis.html', context)

def basket(request):
    context = {
        'title':'Category - Basket',
    }
    return render(request, 'category/basket.html', context)

def taekwondo(request):
    context = {
        'title':'Category - Taekwondo',
    }
    return render(request, 'category/taekwondo.html', context)

def vulcanized(request):
    context = {
        'title':'Category - Vulcanized',
    }
    return render(request, 'category/vulcanized.html', context)

def sneaker(request):
    context = {
        'title':'Category - Sneaker',
    }
    return render(request, 'category/sneaker.html', context)

def hiking(request):
    context = {
        'title':'Category - Hiking',
    }
    return render(request, 'category/hiking.html', context)

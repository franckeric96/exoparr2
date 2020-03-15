from django.shortcuts import render

# Create your views here.

def index(request):
    datas = {
        
    }
    return render(request, 'index.html', datas)

def about(request):
    datas = {
        
    }
    return render(request, 'about.html', datas)

def blog(request):
    datas = {
        
    }
    return render(request, 'blog.html', datas)

def contact(request):
    datas = {
        
    }
    return render(request, 'contact.html', datas)

def singleblog(request):
    datas = {
        
    }
    return render(request, 'single-blog.html', datas)

def elements(request):
    datas = {
        
    }
    return render(request, 'elements.html', datas)


def services(request):
    datas = {
        
    }
    return render(request, 'services.html', datas)


def rooms(request):
    datas = {
        
    }
    return render(request, 'rooms.html', datas)
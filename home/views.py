from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"Thankyou"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is NCC Sgsits")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about NCC")

def cc(request):
    return render(request, 'cc.html')
    #return HttpResponse("This is Cadets corner NCC")

def alumni(request):
    return render(request, 'alumni.html')
    #return HttpResponse("This is alumni NCC Sgsits")

def downloads(request):
    return render(request, 'downloads.html')
    #return HttpResponse("This is downloads NCC Sgsits")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is contact NCC Sgsits")
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # print(posts)
    msg = "Its work!"

    # return render(request, 'base.html', {'posts': posts})
    return HttpResponse(msg)

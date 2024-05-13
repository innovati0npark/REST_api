from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("이상없음")
    return render(request, 'index.html')
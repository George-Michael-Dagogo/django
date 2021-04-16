from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return HttpResponse("Hello Mentor from Zuri\n I hope youre having a nice day")
from django.shortcuts import render
from django.http import request


def home(request):
	import json, requests

	return render(request,'home.html')


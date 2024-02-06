from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def Home(request):
    return JsonResponse({"status":"Success","Message":"Welcome to the home page"})
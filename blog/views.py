from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
def post_list(request):
    return HttpResponse("Hello Django")
def view_date(request):
    return HttpResponse(str(timezone.now()))
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import StreamingHttpResponse
from django.http import JsonResponse
import json
from response import LSResponse
from models import LSUser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def movies(request):
    return HttpResponse("What's the fuck!")

@csrf_exempt
def register(request):
    # user_name = request.POST.get('user_name', '')
    # password = request.POST.get('password', '')
    # body_unicode = request.body.decode('utf-8')
    # print("Raw data: %s" % request.body)
    received_json_data = json.loads(request.body)
    user_name = received_json_data.get('user_name')
    password = received_json_data.get('password')
    user = LSUser()
    user.user_name = user_name
    user.password = password
    user.save()
    res_json = LSResponse().to_json()
    return JsonResponse(res_json)

def login(request):
    pass



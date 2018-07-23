from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.serializers import serialize
from life.models import User, Item
import json
from life.models import *

def index(request):
  return render(request, 'life/index.html')

def need(request):
  return render(request, 'life/need.html')

def history(request):
  return render(request, 'life/history.html')

def items(request):
  if request.method == 'POST':
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    owner = User.objects.get(pk=body['owner']);
    
    item = Item(name=body['name'], owner=owner, amount=body['amount'], description=body['description'], state=body['state'])
    item.save()
    return render(request, 'life/index.html')
  
  else:
    response = serialize('json', Item.objects.all())
    return HttpResponse(response, content_type='application/json')

def users(request):
  response = serialize('json', User.objects.all())
  return HttpResponse(response, content_type='application/json')
from django.shortcuts import render
from .models import Aiquest
from . serializers import AiquestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.
#Queryset
def aiquest_info(request):
    #complex_data
    ai = Aiquest.objects.all()
    serializer = AiquestSerializer(ai, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#model instant
def aiquest_info(request, pk):
    #complex_data
    ai = Aiquest.objects.get(id=pk)
    serializer = AiquestSerializer(ai)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def aiquest_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = AiquestSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully insert data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        serializer = AiquestSerializer(aiq, data = pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Successfully Update data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        aiq = Aiquest.objects.get(id=id)
        aiq.delete()
        res = {'msg': 'Successfully deleted data'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')   
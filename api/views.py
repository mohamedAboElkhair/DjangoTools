# from django.shortcuts import render
from django.http import JsonResponse 
import json
from produ.models import Produ
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from produ.serializers import ProduSerializer
# Create your views here.
# @api_view(["GET"])
# def api_tes(request, *args, **kwargs):
#     model_data = Produ.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['titel'] = model_data.titel
#         # data['content']= model_data.content
#         # data['price']= model_data.price
#         data= model_to_dict(model_data,fields=['id','titel'])
#     return Response(data)  
#     # return JsonResponse(data)
    
# @api_view(["GET"])
# def api_tes(request, *args, **kwargs):
#     instance = Produ.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         data = ProduSerializer(instance).data
#     return Response(data)  
#     # return JsonResponse(data)    
    
@api_view(["POST"])
def api_tes(request, *args, **kwargs):
   serializer = ProduSerializer(data=request.data)
   if serializer.is_valid():
       instance = serializer.save( )
       print(instance)
       return Response(serializer.data)      



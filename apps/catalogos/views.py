from django.shortcuts import render
from django.http import JsonResponse
from .models import Ubicacion
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def TheModelView(request):

    if (request.method == "GET"):
        #Serialize the data into json
        data = serializers.serialize("json", Ubicacion.objects.filter(pk=1))
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import base64


@csrf_exempt
def health_check(request):
    return JsonResponse({"status": 200})

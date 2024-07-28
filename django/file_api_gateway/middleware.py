from django.conf import settings
from django.http import JsonResponse


class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get('API-KEY')
        if api_key not in settings.API_KEYS:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response

import logging
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class APIKeyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        EXCLUDED_PATHS = ["/healthCheck/", "/healthCheck"]

        if request.path not in EXCLUDED_PATHS:
            api_key = request.headers.get('API-KEY')
            if api_key not in settings.API_KEYS:
                return JsonResponse({'error': 'Unauthorized'}, status=401)

        response = self.get_response(request)
        return response

# class APIKeyMiddleware:
#     EXCLUDED_PATHS = [r"^/healthCheck"]
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):

#         if not any(request.path.startswith(excluded_path) for excluded_path in self.EXCLUDED_PATHS):
#             api_key = request.headers.get('API-KEY')
#             if api_key not in settings.API_KEYS:
#                 return JsonResponse({'error': 'Unauthorized'}, status=401)

#         response = self.get_response(request)
#         return response


class DebugMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        logging.debug(f"Response type: {type(response)}")
        if isinstance(response, dict):
            logging.error("Response is a dictionary, which is not valid.")
        return response

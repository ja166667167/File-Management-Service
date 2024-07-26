from django.http import JsonResponse
from .grpc_client import get_user_records, upload_records
import grpc_code.fileManagementService_pb2 as pb2
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@csrf_exempt
def file_api_entry_point(request):

    if request.method == 'GET':
        user_name = request.GET.get('username', '')
        logging.info(f'GET request: user_name = {user_name}')
        response = get_user_records(user_name)
    elif request.method == 'POST':
        # print(request.body)

        logging.info(JsonResponse(request.POST))
        request_body = json.loads(request.body.decode('utf-8'))

        user_name = request_body.get('userName')
        file_path = request_body.get('filePath')
        file_name = request_body.get('fileName')
        logging.info(
            f'POST request: user_name = {user_name}, file_path ={file_path} ,file_name ={file_name}')
        response = upload_records(user_name, file_name, file_path)
    # print(requests)
    # if requests.method == 'GET':

    return JsonResponse(response)

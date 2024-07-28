from django.http import JsonResponse
from .grpc_client import grpc_client
import grpc_code.fileManagementService_pb2 as pb2
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import base64

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@csrf_exempt
def file_api_entry_point(request):
    client = grpc_client()
    if request.method == 'GET':
        user_name = request.GET.get('username', '')
        logging.info(f'GET request: user_name = {user_name}')
        response = client.get_user_records(user_name)
    elif request.method == 'POST':
        request_body = json.loads(request.body.decode('utf-8'))
        user_name = request_body.get('userName')
        file_path = request_body.get('filePath')
        file_name = request_body.get('fileName')
        logging.info(
            f'POST request: user_name = {user_name}, file_path ={file_path} ,file_name ={file_name}')
        response = client.upload_record(user_name, file_name, file_path)

    else:
        return {"status": 405}

    return JsonResponse(response)


@csrf_exempt
def list_users(request):
    client = grpc_client()
    if request.method == 'GET':
        response = client.list_users()
    else:
        return {"status": 405}
    return JsonResponse(response)


@csrf_exempt
def list_obj(request):
    client = grpc_client()
    if request.method == 'GET':
        user_name = request.GET.get('username', '')
        file_path = request.GET.get('filepath', '')
        response = client.list_obj(user_name=user_name, file_path=file_path)
    else:
        return {"status": 405}
    return JsonResponse(response)


@csrf_exempt
def delete_record(request):
    client = grpc_client()
    if request.method != 'DELETE':
        return {"status": 405}
    else:
        user_name = request.GET.get('username', '')
        file_name = request.GET.get('filename', '')
        file_path = request.GET.get('filepath', '')

        logging.info(
            f'DELETE request: user_name = {user_name}, file_path ={file_path} ,file_name ={file_name}')
        response = client.delete_record(
            user_name=user_name, file_name=file_name, file_path=file_path)
    return JsonResponse(response)

from django.test import TestCase, Client
from unittest.mock import patch
from django.urls import reverse
from django.http import HttpRequest
import grpc_code.fileManagementService_pb2 as pb2
from file_api_gateway.views import file_api_entry_point


class test_file_api_entry_point_(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @patch('file_api_gateway.grpc_client.grpc_client.upload_record')
    def test_POST_requests(self, mock_post):
        request = HttpRequest()
        request.method = 'POST'
        request._body = b'{"userName": "testUser","filePath": "/","fileName": "testFile"}'
        mock_post.return_value = {
            "status": "success",
            "message": "upload done"
        }
        response = file_api_entry_point(request)
        mock_post.assert_called_once_with('testUser', 'testFile', '/')

    @patch('file_api_gateway.grpc_client.grpc_client.get_user_records')
    def test_GET_requests(self, mock_get):
        request = HttpRequest()
        request.method = 'GET'
        request.GET = {'username': 'testUser'}
        mock_get.return_value = {}
        response = file_api_entry_point(request)
        mock_get.assert_called_once_with('testUser')

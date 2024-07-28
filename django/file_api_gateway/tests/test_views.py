from django.test import TestCase, Client
from unittest.mock import patch
from django.urls import reverse
from django.http import HttpRequest
import grpc_code.fileManagementService_pb2 as pb2
from file_api_gateway import views


class test_file_api_entry_point_(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @patch('file_api_gateway.grpc_client.grpc_client.upload_record')
    def test_file_api_entry_point_POST(self, mock_post):
        request = HttpRequest()
        request.method = 'POST'
        request._body = b'{"userName": "testUser","filePath": "/","fileName": "testFile"}'
        mock_post.return_value = {
            "status": "success",
            "message": "upload done"
        }
        response = views.file_api_entry_point(request)
        mock_post.assert_called_once_with('testUser', 'testFile', '/')

    @patch('file_api_gateway.grpc_client.grpc_client.get_user_records')
    def test_file_api_entry_point_GET(self, mock_get):
        request = HttpRequest()
        request.method = 'GET'
        request.GET = {'username': 'testUser'}
        mock_get.return_value = {}
        response = views.file_api_entry_point(request)
        mock_get.assert_called_once_with('testUser')

    @patch('file_api_gateway.grpc_client.grpc_client.get_user_records')
    def test_file_api_entry_point_UNKNOWN(self, mock_get):
        request = HttpRequest()
        request.method = 'DELETE'
        request.GET = {'username': 'testUser'}
        mock_get.return_value = {}
        response = views.file_api_entry_point(request)
        assert response == {"status": 405}

    @patch('file_api_gateway.grpc_client.grpc_client.list_users')
    def test_list_users(self, mock_list):
        request = HttpRequest()
        request.method = 'GET'
        mock_list.return_value = {}
        response = views.list_users(request)
        mock_list.assert_called_once()

    @patch('file_api_gateway.grpc_client.grpc_client.list_users')
    def test_list_users_UNKNOWN(self, mock_list):
        request = HttpRequest()
        request.method = 'DELETE'
        mock_list.return_value = {}
        response = views.list_users(request)
        assert response == {"status": 405}

    @patch('file_api_gateway.grpc_client.grpc_client.list_obj')
    def test_list_obj(self, mock_list):
        request = HttpRequest()
        request.method = 'GET'
        request.GET = {'username': 'testUser', 'filepath': '/'}
        mock_list.return_value = {}
        response = views.list_obj(request)
        mock_list.assert_called_once_with(user_name='testUser', file_path='/')

    @patch('file_api_gateway.grpc_client.grpc_client.list_obj')
    def test_list_obj_UNKNOWN(self, mock_list):
        request = HttpRequest()
        request.method = 'DELETE'
        mock_list.return_value = {}
        response = views.list_obj(request)
        assert response == {"status": 405}

    @patch('file_api_gateway.grpc_client.grpc_client.delete_record')
    def test_delete_record(self, mock_delete):
        request = HttpRequest()
        request.method = 'DELETE'
        request.GET = {'username': 'testUser',
                       'filepath': '/', 'filename': 'testFile'}
        mock_delete.return_value = {}
        response = views.delete_record(request)
        mock_delete.assert_called_once_with(
            user_name='testUser', file_name='testFile', file_path='/')

    @patch('file_api_gateway.grpc_client.grpc_client.delete_record')
    def test_delete_record_UNKNOWN(self, mock_delete):
        request = HttpRequest()
        request.method = 'POST'
        mock_delete.return_value = {}
        response = views.delete_record(request)
        assert response == {"status": 405}

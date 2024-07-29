from django.test import TestCase
from unittest.mock import MagicMock, patch, Mock
import grpc_code.fileManagementService_pb2 as pb2
import grpc_code.fileManagementService_pb2_grpc as pb2_grpc
from file_api_gateway.grpc_client import grpc_client

import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class test_grpc_client(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_upload_record(self, mock_stub):
        expected_requset = pb2.UploadRecordRequest(
            userName='testUser', fileName='testFile', filePath='/')
        mock_stub_instance = mock_stub.return_value
        mock_stub_instance.UploadRecord = MagicMock()
        client = grpc_client()
        response = client.upload_record('testUser', 'testFile', '/')
        mock_stub_instance.UploadRecord.assert_called_once_with(
            expected_requset)

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_get_records(self, mock_stub):
        expected_requset = pb2.GetRecordsRequest(userName='testUser')
        mock_stub_instance = mock_stub.return_value
        mock_stub_instance.GetRecords = MagicMock()
        client = grpc_client()
        response = client.get_user_records('testUser')
        mock_stub_instance.GetRecords.assert_called_once_with(
            expected_requset)

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_get_particular_record(self, mock_stub):
        expected_requset = pb2.GetPtclrRecordsRequest(
            userName='testUser', fileName='testFile', filePath='/')
        mock_stub_instance = mock_stub.return_value
        mock_stub_instance.GetParticularRecords = MagicMock()
        client = grpc_client()
        response = client.get_particular_record('testUser', 'testFile', '/')
        mock_stub_instance.GetParticularRecords.assert_called_once_with(
            expected_requset)

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_delete_record(self, mock_stub):
        expected_requset = pb2.DelRecordsRequest(
            userName='testUser', fileName='testFile', filePath='/')
        mock_stub_instance = mock_stub.return_value
        mock_stub_instance.DeleteRecord = MagicMock()
        client = grpc_client()
        client.get_particular_record = MagicMock()
        client.get_particular_record.return_value = {
            'files': [{'userName': 'UserA', 'fileName': 'FileA', 'filePath': '/'}]}
        response = client.delete_record('testUser', 'testFile', '/')
        mock_stub_instance.DeleteRecord.assert_called_once_with(
            expected_requset)

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_delete_record_not_exist(self, mock_stub):
        mock_stub_instance = mock_stub.return_value
        client = grpc_client()
        client.get_particular_record = MagicMock()
        client.get_particular_record.return_value = {}
        response = client.delete_record('testUser', 'testFile', '/')
        mock_stub_instance.DeleteRecord.assert_not_called()

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_list_users(self, mock_stub):
        mock_stub_instance = mock_stub.return_value
        client = grpc_client()
        response = client.list_users()
        mock_stub_instance.ListUsers.assert_called_once()

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_list_obj(self, mock_stub):
        expected_request = pb2.ListObjRequest(
            userName='testUser', filePath='/')
        mock_stub_instance = mock_stub.return_value
        client = grpc_client()
        response = client.list_obj('testUser', '/')
        mock_stub_instance.ListObj.assert_called_once_with(expected_request)

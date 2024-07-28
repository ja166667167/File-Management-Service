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
    def test_POST_upload_record(self, mock_stub):
        expected_requset = pb2.UploadRecordRequest(
            userName='testUser', fileName='testFile', filePath='/')
        mock_stub_instance = mock_stub.return_value
        mock_stub_instance.UploadRecord = MagicMock()
        client = grpc_client()
        response = client.upload_record('testUser', 'testFile', '/')
        mock_stub_instance.UploadRecord.assert_called_once_with(
            expected_requset)

    @patch('grpc_code.fileManagementService_pb2_grpc.FileManagementServiceStub')
    def test_GET_get_records(self, mock_stub):
        expected_requset = pb2.GetRecordsRequest(userName='testUser')
        mock_stub_instance = mock_stub.return_value
        mock_stub_instance.UploadRecord = MagicMock()
        client = grpc_client()
        response = client.get_user_records('testUser')
        mock_stub_instance.GetRecords.assert_called_once_with(
            expected_requset)

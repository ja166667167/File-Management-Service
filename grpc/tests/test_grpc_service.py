from unittest import TestCase
from unittest.mock import patch, MagicMock
from grpc_server import FileManagementService
import grpc_code.fileManagementService_pb2 as pb2
from google.protobuf.empty_pb2 import Empty


class testGrpcServer(TestCase):

    @patch('psycopg.Connection.cursor')
    def test_upload_records(self, mock_cursor):
        service = FileManagementService()
        request = pb2.UploadRecordRequest(
            userName='testUser', fileName='testFile', filePath='/')
        context = None
        mock_cursor_instance = mock_cursor.return_value
        response = service.UploadRecord(request, context)
        expected_query = f"INSERT INTO files(file_name,user_name,file_path) VALUES('testFile','testUser','/');"
        mock_cursor_instance.execute.assert_called_once_with(expected_query)

    @patch('psycopg.Connection.cursor')
    def test_get_records(self, mock_cursor):
        service = FileManagementService()
        request = pb2.GetRecordsRequest(userName='testUser')
        context = None
        mock_cursor_instance = mock_cursor.return_value
        mock_cursor_instance.fetchall.return_value = [('testFile', '/')]
        response = service.GetRecords(request, context)
        expected_query = f"SELECT file_name, file_path FROM files WHERE user_name = 'testUser';"
        mock_cursor_instance.execute.assert_called_once_with(expected_query)
        assert response == pb2.GetRecordResponse(
            files=[{'fileName': 'testFile', 'filePath': '/'}])

    @patch('psycopg.Connection.cursor')
    def test_delete_records(self, mock_cursor):
        service = FileManagementService()
        request = pb2.DelRecordsRequest(
            userName='testUser', fileName='testFile', filePath='/')
        context = None
        mock_cursor_instance = mock_cursor.return_value
        response = service.DeleteRecord(request, context)
        expected_query = f"DELETE FROM files WHERE user_name='testUser' and file_name='testFile' and file_path='/'"
        mock_cursor_instance.execute.assert_called_once_with(expected_query)

    @patch('psycopg.Connection.cursor')
    def test_get_particular_records(self, mock_cursor):
        service = FileManagementService()
        request = pb2.GetPtclrRecordsRequest(
            userName='testUser', fileName='testFile', filePath='/')
        context = None
        mock_cursor_instance = mock_cursor.return_value
        mock_cursor_instance.execute = MagicMock()
        mock_cursor_instance.fetchall.return_value = [
            ('testFile', 'testUser', '/')]
        response = service.GetParticularRecords(request, context)
        expected_query = f"SELECT * FROM files WHERE user_name='testUser' and file_name='testFile' and file_path='/';"
        mock_cursor_instance.execute.assert_called_once_with(expected_query)
        assert response == pb2.GetPtclrRecordsResponse(
            files=[{'fileName': 'testFile', 'userName': 'testUser', 'filePath': '/'}])

    @patch('psycopg.Connection.cursor')
    def test_ListUsers(self, mock_cursor):
        service = FileManagementService()
        request = Empty()
        context = None
        mock_cursor_instance = mock_cursor.return_value
        mock_cursor_instance.execute = MagicMock()
        mock_cursor_instance.fetchall.return_value = [
            ('testUser',)]
        response = service.ListUsers(request, context)
        expected_query = f"SELECT user_name FROM files;"
        mock_cursor_instance.execute.assert_called_once_with(expected_query)
        assert response == pb2.ListUsersResponse(users=['testUser'])

    @patch('psycopg.Connection.cursor')
    def test_ListObj(self, mock_cursor):
        service = FileManagementService()
        request = pb2.ListObjRequest(userName='testUser', filePath='/')
        context = None
        mock_cursor_instance = mock_cursor.return_value
        mock_cursor_instance.execute = MagicMock()
        response = service.ListObj(request, context)
        expected_query = f"SELECT file_path FROM files WHERE user_name='testUser' AND file_path LIKE '/%';"
        expected_query2 = f"SELECT file_name FROM files WHERE user_name='testUser' AND file_path ='/' OR file_path ='//';"
        assert mock_cursor_instance.execute.call_count == 2
        call_args_list = mock_cursor_instance.execute.call_args_list
        assert call_args_list[0] == ((expected_query,),)
        assert call_args_list[1] == ((expected_query2,),)

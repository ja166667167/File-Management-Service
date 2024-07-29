import grpc
import grpc_code.fileManagementService_pb2 as pb2
import grpc_code.fileManagementService_pb2_grpc as pb2_grpc
from google.protobuf.json_format import MessageToDict
from google.protobuf.empty_pb2 import Empty
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

GRPC_HOST = os.getenv('GRPC_HOST')
GRPC_PORT = os.getenv('GRPC_PORT')
# GRPC_HOST = 'localhost'


class grpc_client:
    def __init__(self) -> None:
        pass
        self.channel = grpc.insecure_channel(f"{GRPC_HOST}:{GRPC_PORT}")
        self.stub = pb2_grpc.FileManagementServiceStub(self.channel)

    def get_user_records(self, user_name: str) -> str:

        logging.info("Sending get_user_records request")
        GetRecords_response = self.stub.GetRecords(
            pb2.GetRecordsRequest(userName=user_name))
        GetRecords_response_Dict = MessageToDict(GetRecords_response)
        logging.info(
            f"get_user_records done with response:\n{GetRecords_response_Dict}")
        return GetRecords_response_Dict

    def upload_record(self, user_name: str, file_name: str, file_path: str) -> str:
        logging.info("Sending upload_records request")
        Upload_response = self.stub.UploadRecord(pb2.UploadRecordRequest(
            userName=user_name, fileName=file_name, filePath=file_path))
        logging.info(
            f"upload_records done with response:\n{Upload_response}")
        Upload_response_Dict = MessageToDict(Upload_response)
        return Upload_response_Dict

    def get_particular_record(self, user_name: str, file_name: str, file_path: str):
        ptclr_record_response = self.stub.GetParticularRecords(pb2.GetPtclrRecordsRequest(
            userName=user_name, fileName=file_name, filePath=file_path))
        ptclr_record_response_Dict = MessageToDict(ptclr_record_response)
        return ptclr_record_response_Dict

    def delete_record(self, user_name: str, file_name: str, file_path: str):
        logging.info("Sending Delete_records request")
        check_exist = self.get_particular_record(
            user_name=user_name, file_name=file_name, file_path=file_path)
        # logging.info(f"check_exist = {check_exist}")
        if not check_exist:
            return MessageToDict(pb2.DelRecordsResponse(status=pb2.statusType.Value('fail'), message="The record does not exist!!!"))
        Delete_response = self.stub.DeleteRecord(pb2.DelRecordsRequest(
            userName=user_name, fileName=file_name, filePath=file_path))
        logging.info(
            f"Delete_records done with response:\n{Delete_response}")
        Delete_response_Dict = MessageToDict(Delete_response)
        return Delete_response_Dict

    def list_users(self):
        logging.info("Sending List user request")
        request = Empty()
        list_user_response = self.stub.ListUsers(request)
        logging.info(f"List Users done with response: \n{list_user_response}")
        list_user_response_Dict = MessageToDict(list_user_response)
        return list_user_response_Dict

    def list_obj(self, user_name: str, file_path: str):
        logging.info("Sending List Objects request")
        list_user_response = self.stub.ListObj(
            pb2.ListObjRequest(userName=user_name, filePath=file_path))
        logging.info(
            f"List Objects done with response: \n{list_user_response}")
        list_user_response_Dict = MessageToDict(list_user_response)
        return list_user_response_Dict

    def __del__(self):
        self.channel.close()


if __name__ == "__main()__":
    grpc1 = grpc_client()
    grpc1.ListUsers()

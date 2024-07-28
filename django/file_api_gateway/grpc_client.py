import grpc
import grpc_code.fileManagementService_pb2 as pb2
import grpc_code.fileManagementService_pb2_grpc as pb2_grpc
from google.protobuf.json_format import MessageToDict
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

    def __del__(self):
        pass
        # self.channel.close()

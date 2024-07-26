import grpc
import grpc_code.fileManagementService_pb2 as pb2
import grpc_code.fileManagementService_pb2_grpc as pb2_grpc
from google.protobuf.json_format import MessageToJson, MessageToDict
import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

GRPC_HOST = os.getenv('GRPC_HOST')
# GRPC_HOST = 'localhost'


def get_user_records(user_name: str) -> str:
    with grpc.insecure_channel(f"{GRPC_HOST}:50051") as channel:
        stub = pb2_grpc.FileManagementServiceStub(channel)
        logging.info("Sending get_user_records request")
        GetRecords_response = stub.GetRecords(
            pb2.GetRecordsRequest(userName=user_name))
        GetRecords_response_Json = MessageToDict(GetRecords_response)
        logging.info(
            f"get_user_records done with response:\n{GetRecords_response_Json}")
        return GetRecords_response_Json


def upload_records(user_name: str, file_name: str, file_path: str) -> str:
    with grpc.insecure_channel(f"{GRPC_HOST}:50051") as channel:
        stub = pb2_grpc.FileManagementServiceStub(channel)
        logging.info("Sending upload_records request")
        Upload_response = stub.UploadRecord(pb2.UploadRecordRequest(
            userName=user_name, fileName=file_name, filePath=file_path))
        logging.info(f"upload_records done with response:\n{Upload_response}")
        Upload_response_Json = MessageToDict(Upload_response)
        return Upload_response_Json

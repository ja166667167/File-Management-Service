from concurrent import futures
import grpc
import grpc_code.fileManagementService_pb2 as pb2
import grpc_code.fileManagementService_pb2_grpc as pb2_grpc
import os
import logging
import psycopg

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class FileManagementService(pb2_grpc.FileManagementService):
    def __init__(self) -> None:
        try:
            self.conn = psycopg.connect(
                dbname=os.getenv('POSTGRES_DB'),
                user=os.getenv('POSTGRES_USER'),
                password=os.getenv('POSTGRES_PASSWORD'),
                host=os.getenv('POSTGRES_HOST'),
                port="5432"
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            raise (e)

# Required API
    def GetRecords(self, request, context):
        query = f"SELECT file_name, file_path FROM files WHERE user_name = '{request.userName}';"
        logging.info(f"Get Records query = {query}")
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            # logging.info(f"Get Records Result = {result}")
        except Exception as e:
            self.conn.rollback()
            raise (e)
        parsedResult = []
        for r in result:
            tmp = {}
            tmp['name'] = r[0]
            tmp['path'] = r[1]
            parsedResult.append(tmp)
        logging.info(f"Get Records Response = {parsedResult}")
        return pb2.GetRecordResponse(files=parsedResult)

    def UploadRecord(self, request, context):
        fixFilePath = request.filePath
        if request.filePath[0] == '':
            fixFilePath = '/'
        elif request.filePath[-1] != '/':
            fixFilePath = fixFilePath+'/'
        elif request.filePath[0] != '/':
            fixFilePath = '/'+fixFilePath

        query = f"INSERT INTO files(file_name,user_name,file_path) VALUES('{request.fileName}','{request.userName}','{fixFilePath}');"
        logging.info(f"Upload Records query = {query}")
        try:
            self.cursor.execute(query)
            self.conn.commit()
            # result=self.cursor.fetchall()
        except Exception as e:
            self.conn.rollback()
            logging.error(
                f"Error occur when uploading files: {pb2.UploadResponse(status=pb2.statusType.Value('fail'), message=f'Uploading Failed: {e}')}")
            return pb2.UploadResponse(status=pb2.statusType.Value('fail'), message=f'Uploading Failed: {e}')
        logging.info(
            f"Upload Records response: {pb2.UploadResponse(status=pb2.statusType.Value('success'), message='upload done')}")
        return pb2.UploadResponse(status=pb2.statusType.Value('success'), message='upload done')


# Extra API

    def GetParticularRecords(self, request, context):
        query = f"SELECT * FROM files WHERE user_name='{request.userName}' and file_name='{request.fileName}' and file_path='{request.filePath}';"
        logging.info(f"Getting Particular Records query = {query}")

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except Exception as e:
            raise (e)
        parsedResult = []
        for r in result:
            tmp = {}
            tmp['fileName'] = r[0]
            tmp['userName'] = r[1]
            tmp['filePath'] = r[2]
            parsedResult.append(tmp)
        logging.info(f"Get Records Response = {parsedResult}")
        return pb2.GetPtclrRecordsResponse(files=parsedResult)

    def DeleteRecord(self, request, context):
        query = f"DELETE FROM files WHERE user_name='{request.userName}' and file_name='{request.fileName}' and file_path='{request.filePath}'"
        logging.info(f"Deleting Records query = {query}")
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            logging.error(
                f"Error occur when deleting files: {pb2.DelRecordsResponse(status=pb2.statusType.Value('fail'), message=f'Deleting Failed: {e}')}")
            return pb2.DelRecordsResponse(status=pb2.statusType.Value('fail'), message=f'Deleting Failed: {e}')
        logging.info(
            f"Deleting Records response: {pb2.DelRecordsResponse(status=pb2.statusType.Value('success'), message='Deleting done')}")
        return pb2.DelRecordsResponse(status=pb2.statusType.Value('success'), message='Deleting done')

    def ListUsers(self, request, context):
        query = "SELECT user_name FROM files;"
        logging.info(f"List User query = {query}")

        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except Exception as e:
            logging.error(f"Error occur when Listing files: {e}")
            raise (e)
        output = []
        for r in result:
            output.append(r[0])
        logging.info(f"List User done with response: {result}")
        return pb2.ListUsersResponse(users=list(set(output)))

    def ListObj(self, request, context):
        query = f"SELECT file_path FROM files WHERE user_name='{request.userName}' AND file_path LIKE '{request.filePath}%';"
        query2 = f"SELECT file_name FROM files WHERE user_name='{request.userName}' AND (file_path ='{request.filePath}' OR file_path ='{request.filePath}/');"
        logging.info(f"List Object-folder query = {query}")
        logging.info(f"List Object-file query = {query2}")

        try:
            self.cursor.execute(query)
            folderResults = self.cursor.fetchall()
            self.cursor.execute(query2)
            filesResults = self.cursor.fetchall()
        except Exception as e:
            raise (e)
        folderList = []
        for r in folderResults:
            tmp = r[0][len(request.filePath):]
            if tmp == '':
                continue
            if tmp == '/':
                folderList.append('/')
                continue
            if tmp[0] == '/':
                tmp = tmp[1:]
            tmp = tmp.split('/')[0]
            if f"/{tmp}/" not in folderList:
                folderList.append(f"/{tmp}/")
        fileList = []
        for r in filesResults:
            fileList.append(r[0])
        logging.info(
            f"List Objescts Response = {folderList}, {fileList}")
        if not folderList:
            folderList = ['']
        if not fileList:
            fileList = ['']
        return pb2.ListObjResponse(folders=folderList, files=fileList)

# destructor

    def __del__(self):
        self.conn.close()
        self.cursor.close()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_FileManagementServiceServicer_to_server(
        FileManagementService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

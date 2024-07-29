# File-Management-Service

File Management Service for Wipro Asseccement

## Set up Enviroment

To set up enviroment run following command:

```
docker-compose up --build
```

## File API Spec

### Required API:

- GetRecords:

  - Description: Get file records by user name.
  - Endpoint: /api/files/?username={user_name}
  - Method: GET
  - Response Body:

    ```json
    {
      "files": [
        {
          "name": "string",
          "path": "string"
        }
      ]
    }
    ```

- UploadRecord:

  - Description: Upload one file to particular user and path.
  - Endpoint: /api/files
  - Method:
  - Request Body:
    ```json
    {
      "user_name": "string",
      "file_name": "string",
      "file_path": "string"
    }
    ```
  - Response Body:

    ```json
    {
      "status": "success" | "fail",
      "message": "string"
    }
    ```

- ListUsers:

  - Description: List all users.
  - Endpoint: /api/listUsers
  - Method: GET
  - Response Body:

    ```json
    {
      "Users": ["string"]
    }
    ```

- ListObjects:

  - Description: List folders or files with particular path and user
  - Endpoint: /api/listObj/?username={user_name}&filepath={file_path}
  - Method: GET
  - Response Body:

    ```json
    {
      "folders": ["string"],
      "files": ["string"]
    }
    ```

- DeleteRecord:

  - Description: Delete one particular file
  - Endpoint: /api/deleteRecord/?username={user_name}&filepath={file_path}&filename={file_name}
  - Method: DELETE
    - Response Body:
    ```json
    {
      "status": "success" | "fail",
      "message": "string"
    }
    ```

## Note

- The file path should starts and ends with '/', if not the service will automaticly fix it.
  > file path: "/a" and "a/" and "a" will be fix to "/a/"
- If the file path is empty it will be assumed as a root directory: '/'

FROM python:3.11-slim

# Set work directory
WORKDIR /file_management_service

# Install dependencies
COPY requirements.txt /file_management_service/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /file_management_service/

# Run gRPC server
CMD ["python", "your_grpc_server.py"]

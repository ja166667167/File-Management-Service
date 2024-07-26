FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /file_management_system

# Install dependencies
COPY requirements.txt /file_management_system/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /file_management_system/

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
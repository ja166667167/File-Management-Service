COPY files (user_name, file_path, file_name)
FROM 'E:\\Work\\File-Management-Service\\postgresql\\mock_data.csv'
DELIMITER ','
CSV HEADER;

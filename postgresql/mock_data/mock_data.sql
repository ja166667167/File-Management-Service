COPY files(user_name, file_path, file_name)
FROM './mock_data.csv'
DELIMITER ','
CSV HEADER;
-- \copy files (user_name, file_path, file_name) from ./mock_data.csv delimiter ',' CSV HEADER;

CREATE TABLE IF NOT EXISTS Files (

    file_name VARCHAR(50) NOT NULL,
    user_name VARCHAR(50) NOT NULL,
    file_path VARCHAR(200) NOT NULL,
    PRIMARY KEY (file_name,user_name,file_path)
    
);

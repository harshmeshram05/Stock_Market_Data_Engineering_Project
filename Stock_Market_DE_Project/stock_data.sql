CREATE DATABASE stock_db;
CREATE SCHEMA raw;

CREATE TABLE raw.stock_data (
    data VARIANT
);

USE ROLE ACCOUNTADMIN;

CREATE STORAGE INTEGRATION s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::519818057096:role/snowflake_s3_role'
STORAGE_ALLOWED_LOCATIONS = ('s3://stock-data-raw-harsh/');

DESC INTEGRATION s3_int;

CREATE FILE FORMAT json_format
TYPE = JSON;


CREATE STAGE stock_stage
STORAGE_INTEGRATION = s3_int
URL = 's3://stock-data-raw-harsh/';
FILE_FORMAT = (TYPE = JSON);

COPY INTO raw.stock_data
FROM @stock_stage/stock_data/
FILE_FORMAT = (TYPE = JSON);

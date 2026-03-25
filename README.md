A complete end-to-end data engineering pipeline that streams live stock data from an external API, processes it through a local Kafka cluster, stores it in an S3-compatible data lake, and transforms it within Snowflake using dbt.

# 📊 End-to-End Data Engineering Pipeline (Kafka + Snowflake + dbt)

## 🚀 Overview
This project demonstrates a **modern end-to-end data engineering pipeline** that ingests real-time data, stores it in a cloud data warehouse, and performs transformations using ELT principles.

The pipeline is designed using **Medallion Architecture (Bronze → Silver → Gold)** to simulate a production-grade data platform.

---

## 🏗️ Architecture

![Architecture_Diagram](https://github.com/user-attachments/assets/261f8d3c-60cc-411f-b6be-84dd9d3ae799)

---

## 📌 Key Highlights

- Built a **real-time streaming pipeline using Kafka**  
- Stored raw streaming data in **AWS S3 (JSON format) as a data lake**  
- Designed **ELT pipeline using Snowflake and dbt**  
- Implemented **Medallion Architecture (Bronze, Silver, Gold)**  
- Enabled **data reprocessing capability using S3**  

---

## 🛠️ Tech Stack

- Data Source: Alpha Vantage API
- Apache Kafka – Real-time data streaming
- Python – Producer & Consumer scripts  
- AWS S3 – Data lake for storing raw JSON data  
- Snowflake – Cloud data warehouse  
- dbt (Data Build Tool) – Data transformation  
- SQL – Data modeling  
- Docker – Containerization   

---

## 🔄 How the Pipeline Works

### 1. Data Generation
A Python-based Producer polls the Alpha Vantage API (TIME_SERIES_INTRADAY) for real-time stock quotes.

### 2. Kafka Producer
The producer sends streaming data into Kafka topics.

<img width="1366" height="608" alt="Image" src="https://github.com/user-attachments/assets/33a5cf0e-29f4-4c9d-a3cc-639829a70c57" />

### 3. Kafka Broker
Kafka handles high-throughput real-time data streaming.

### 4. Kafka Consumer
The consumer reads data from Kafka and performs two operations:
- Stores raw data in **AWS S3 (JSON format)** → Data Lake  
- Loads data into Snowflake for further processing  

### 5. AWS S3 (Data Lake)
- Stores raw streaming data in **JSON format**  
- Acts as a backup and source of truth  
- Enables reprocessing if needed

### 6. Snowflake (Bronze Layer)
- Stores raw ingested data  
- Can be loaded directly from S3

![Image](https://github.com/user-attachments/assets/cf5a0ead-02b3-4b5a-bcc6-472b69902685)

### 7. dbt Transformations
- Transforms raw data into structured datasets  

### 8. Snowflake (Silver & Gold Layers)
- Silver → Cleaned data  
- Gold → Business-level insights

---

## 🧱 Data Modeling (Medallion Architecture)

### 🥉 Bronze Layer
- Raw data ingested from Kafka
- Stored without transformation

### 🥈 Silver Layer
- Cleaned and structured data
- Removed duplicates and handled null values

### 🥉 Bronze Layer
- Aggregated Data
- Ready for analytics and reporting

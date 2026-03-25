SELECT
    data:"Global Quote":"01. symbol"::STRING AS symbol,
    data:"Global Quote":"05. price"::FLOAT AS price,
    CURRENT_TIMESTAMP() AS processed_time
FROM stock_db.raw.stock_data
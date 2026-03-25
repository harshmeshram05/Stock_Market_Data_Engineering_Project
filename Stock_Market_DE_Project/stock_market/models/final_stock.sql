SELECT
    symbol,
    AVG(price) AS avg_price,
    COUNT(*) AS total_records
FROM {{ ref('stg_stock') }}
GROUP BY symbol
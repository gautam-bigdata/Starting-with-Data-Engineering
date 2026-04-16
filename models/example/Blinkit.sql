
WITH CUSTOMER_DS AS (
    SELECT 
        CUSTOMER_ID,
        AREA,
        CUSTOMER_SEGMENT,
        TOTAL_ORDERS,
        AVG_ORDER_VALUE
    FROM 
        raw.blinkit_dataset.customers_data
),

ORDERS_DS AS (
    SELECT 
        ORDER_ID,
        CUSTOMER_ID,
        ORDER_DATE,
        DELIVERY_STATUS,
        ORDER_TOTAL,
        PAYMENT_METHOD
    FROM 
        raw.blinkit_dataset.orders
),

CUS_FEEDBACK AS (
    SELECT 
        FEEDBACK_ID,
        ORDER_ID,
        CUSTOMER_ID,
        RATING,
        FEEDBACK_CATEGORY,
        SENTIMENT,
        FEEDBACK_DATE
    FROM 
        raw.blinkit_dataset.customer_feedback
)

DELIVERY_PERFORMANCE AS (
    SELECT 
        ORDER_ID,
        DELIVERY_TIME_MINUTES,
        DISTANCE_KM,
        DELIVERY_STATUS
    FROM 
        raw.blinkit_dataset.delivery_performance
)
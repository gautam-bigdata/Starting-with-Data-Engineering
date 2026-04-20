
WITH CUSTOMER_DS AS (
    SELECT * FROM {{ ref('blinkit_Customers') }} 
),

ORDERS_DS AS (
    SELECT * FROM {{ ref('blinkit_orders') }}
),

CUS_FEEDBACK AS (
    select * from {{ ref('blinkit_cus_feedback') }}  
),

DELIVERY_PERFORMANCE AS (
    select * from {{ ref('blinkit_delivery_performance') }}    
)
select 
    CUSTOMER_DS.customer_id,
    CUSTOMER_DS.area,
    CUSTOMER_DS.total_orders,
    CUSTOMER_DS.avg_order_value,
    ORDERS_DS.delivery_status,
    ORDERS_DS.order_total,
    ORDERS_DS.payment_method
from
    CUSTOMER_DS, ORDERS_DS
where 
    CUSTOMER_DS.customer_id = ORDERS_DS.customer_id
order by 
    total_orders desc,
    order_total desc,
    avg_order_value desc
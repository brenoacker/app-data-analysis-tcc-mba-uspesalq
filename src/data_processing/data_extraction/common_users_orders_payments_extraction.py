import os
import sys

from save_to_csv import save_to_csv

from src.database.fetch_data import fetch_data

SQL_QUERY = '''
SELECT 
    u.age,
    u.gender,
    CASE 
        WHEN o.offer_id IS NOT NULL THEN true
        ELSE false
    END AS has_offer,
    o."type" as order_type,
    o.total_price,
    p.payment_method,
    CASE 
        WHEN p.payment_card_gateway IS NOT NULL THEN 'adyen'
        ELSE ' '
    END AS payment_card_gateway
FROM 
    tb_users u
JOIN 
    tb_orders o ON u.id = o.user_id
JOIN 
    tb_payments p ON o.user_id = p.user_id
where p.status = 'PAID' and o.status = 'CONFIRMED'
'''

if __name__ == "__main__":
    data = fetch_data(SQL_QUERY)
    save_to_csv(data, 'common_users_orders_payments_extraction.csv', 'data\database')
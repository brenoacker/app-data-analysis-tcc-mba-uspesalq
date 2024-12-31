import os
import sys

from src.data_processing.data_extraction.save_to_csv import save_to_csv
from src.database.fetch_data import fetch_data


SQL_QUERY = "SELECT * FROM public.tb_payments;"

if __name__ == "__main__":
    data = fetch_data(SQL_QUERY)
    save_to_csv(data, 'tb_payments.csv', 'data\database')
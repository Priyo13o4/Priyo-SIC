import pandas as pd
from models import FoodRecord, FOOD_RECORD_FIELDS 
from typing import List
import os
import csv

def read_food_records(filename: str) -> pd.DataFrame:
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return pd.DataFrame(columns=FOOD_RECORD_FIELDS)

def append_food_record(filename: str, record: FoodRecord):
    df = read_food_records(filename)
    df = pd.concat([df, pd.DataFrame([record.__dict__])], ignore_index=True)
    df.to_csv(filename, index=False)

def write_food_records(filename: str, records: List[FoodRecord]):
    df = pd.DataFrame([r.__dict__ for r in records], columns=FOOD_RECORD_FIELDS)
    df.to_csv(filename, index=False)

def read_ngos(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)

def log_redistribution(log_filename: str, date: str, food_item_name: str, total_wasted: float, ngo_row: pd.Series):
    log_exists = os.path.exists(log_filename)
    with open(log_filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'date', 'food_item_name', 'total_wasted',
            'ngo_unique_id', 'ngo_name', 'registered_district', 'sectors'])
        if not log_exists:
            writer.writeheader()
        writer.writerow({
            'date': date,
            'food_item_name': food_item_name,
            'total_wasted': total_wasted,
            'ngo_unique_id': ngo_row['unique_id'],
            'ngo_name': ngo_row['ngo_name'],
            'registered_district': ngo_row['registered_district'],
            'sectors': ngo_row['sectors']
        })

def ngo_redistribution_summary(log_filename: str):
    import pandas as pd
    if not os.path.exists(log_filename):
        print("No redistribution log found.")
        return pd.DataFrame()
    df = pd.read_csv(log_filename)
    summary = df.groupby(['ngo_unique_id', 'ngo_name', 'registered_district'])['total_wasted'].agg(['sum', 'count']).reset_index()
    summary = summary.rename(columns={'sum': 'total_redistributed_kg', 'count': 'num_donations'})
    return summary

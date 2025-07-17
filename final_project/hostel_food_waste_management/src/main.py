import sys
import os
from file_handler import read_food_records,log_redistribution , ngo_redistribution_summary, read_ngos
from analysis import daily_wastage_report, high_wastage_items, wastage_trend_over_time, surplus_items, total_wastage_cost, high_cost_wastage_items
from plotting import plot_wastage_trend, plot_high_wastage_items
import pandas as pd
import random
"""For a more robust path handling of the datafile we use the following logic """
# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the absolute path to the data file
datafile = os.path.join(BASE_DIR, '..', 'data', 'food_records.csv')
datafile = os.path.abspath(datafile)

NGO_CSV = os.path.join(BASE_DIR, '..', 'data', 'food_donation_ngos_bangalore.csv')
REDIST_LOG_CSV = os.path.join(BASE_DIR, '..', 'data', 'redistribution_log.csv')

from utils import add_record_interactive

def show_redistribution_log():
    import os
    import pandas as pd
    if not os.path.exists(REDIST_LOG_CSV):
        print("No redistribution log found.")
        return
    df = pd.read_csv(REDIST_LOG_CSV)
    if df.empty:
        print("Redistribution log is empty.")
    else:
        print("\nRedistribution Log:")
        print(df.to_string(index=False))

def check_specific_day():
    df = read_food_records(datafile)
    date = input("Enter date (YYYY-MM-DD): ")
    day_df = df[df['date'] == date]
    if day_df.empty:
        print(f"No records found for {date}.")
    else:
        print("\nRecords for", date)
        print(day_df.to_string(index=False, header=True))

def predict_prep_amount_menu():
    df = read_food_records(datafile)
    available_items = sorted(df['food_item_name'].dropna().unique())
    if not available_items:
        print("No food item data available.")
        return
    print("Data is available for the following items, please choose one:")
    print(", ".join(available_items))
    food_item_name = input("Enter food item name: ")
    days_input = input("Enter number of days to average (default 30): ")
    try:
        days = int(days_input) if days_input.strip() else 30
    except ValueError:
        days = 30
    from analysis import predict_preparation_amount
    avg = predict_preparation_amount(df, food_item_name, days)
    if avg > 0:
        print(f"Predicted average preparation amount for '{food_item_name}' over last {days} days: {avg:.2f} kg")
    else:
        print(f"No data found for '{food_item_name}' in the last {days} days.")

def auto_redistribute():
    df = read_food_records(datafile)
    ngos = read_ngos(NGO_CSV)
    threshold_input = input("Enter wastage threshold (kg) for redistribution: ")
    try:
        threshold = float(threshold_input)
    except ValueError:
        print("Invalid threshold. Using default of 10 kg.")
        threshold = 10.0
    updated = False
    for idx, row in df.iterrows():
        if row['total_wasted'] > threshold and (not row.get('redistributed_to') or pd.isna(row['redistributed_to']) or row['redistributed_to'] == ''):
            ngo_row = ngos.sample(1).iloc[0]
            df.at[idx, 'redistributed_to'] = ngo_row['unique_id']
            log_redistribution(REDIST_LOG_CSV, row['date'], row['food_item_name'], row['total_wasted'], ngo_row)
            print(f"Redistributed {row['total_wasted']} kg of {row['food_item_name']} on {row['date']} to NGO: {ngo_row['ngo_name']}")
            updated = True
    if updated:
        df.to_csv(datafile, index=False)
        print("Redistribution complete and records updated.")
    else:
        print("No items met the threshold for redistribution or all already redistributed.")

def print_menu():
    print("\nFood Wastage Management System")
    print("1. Show all records")
    print("2. Add a new record")
    print("3. Daily wastage report")
    print("4. Plot daily breakdown (by date)")
    print("5. High wastage items")
    print("6. Wastage trend graph")
    print("7. High wastage items graph")
    print("8. Surplus items")
    print("9. Predict preparation amount")
    print("10. NGO redistribution summary")
    print("11. Show redistribution log")
    print("12. Total cost of food wasted")
    print("13. Top high-cost wastage items")
    print("0. Exit")

def menu():
    while True:
        print_menu()
        try:
            choice = input("Enter choice: ")
        except (EOFError, KeyboardInterrupt):
            print("\nThank you for using the Hostel Food Wastage Management App. Remember: Every plate counts—let's reduce food waste together!")
            sys.exit(0)
        match choice:
            case '1':
                df = read_food_records(datafile)
                print(df)
            case '2':
                add_record_interactive(datafile, NGO_CSV, REDIST_LOG_CSV)
            case '3':
                df = read_food_records(datafile)
                print(daily_wastage_report(df))
            case '4':
                df = read_food_records(datafile)
                date = input("Enter date (YYYY-MM-DD): ")
                from plotting import plot_daily_breakdown
                plot_daily_breakdown(df, date)
            case '5':
                df = read_food_records(datafile)
                print(high_wastage_items(df))
            case '6':
                df = read_food_records(datafile)
                plot_wastage_trend(df)
            case '7':
                df = read_food_records(datafile)
                plot_high_wastage_items(df)
            case '8':
                df = read_food_records(datafile)
                print(surplus_items(df))
            case '9':
                predict_prep_amount_menu()
            case '10':
                summary = ngo_redistribution_summary(REDIST_LOG_CSV)
                if not summary.empty:
                    print(summary)
            case '11':
                show_redistribution_log()
            case '12':
                df = read_food_records(datafile)
                print(f"Total cost of all food wasted: ₹{total_wastage_cost(df):,.2f}")
            case '13':
                df = read_food_records(datafile)
                print("Top high-cost wastage items:")
                print(high_cost_wastage_items(df))
            case '0':
                print("Thank you for using the Hostel Food Wastage Management App. Remember: Every plate counts—let's reduce food waste together!")
                sys.exit(0)
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    print("Hello !! Welcome to Hostel Food Wastage Management App")
    menu() 
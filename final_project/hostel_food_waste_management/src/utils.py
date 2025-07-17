from file_handler import read_food_records, append_food_record, read_ngos, log_redistribution
from models import FoodRecord
import random

def add_record_interactive(datafile, NGO_CSV, REDIST_LOG_CSV):
    """
    Interactive function to add a new record.
    - Prompts user for input.
    - Validates input (e.g., consumed <= prepared).
    - Auto-calculates wastage.
    - Prompts for redistribution if wastage detected.
    - Shows record before and after redistribution.
    - Appends the record to the data file.
    """
    df = read_food_records(datafile)
    if df.empty:
        next_id = 1
    else:
        next_id = int(df['id'].max()) + 1
    date = input("Enter date (YYYY-MM-DD): ")
    food_item_name = input("Enter food item: ")
    try:
        total_prepared = float(input("Quantity prepared (kg): "))
        total_consumed = float(input("Quantity consumed (kg): "))
        price = float(input("Price per kg: "))
    except ValueError:
        print("Error: Please enter valid numeric values. Record discarded.")
        return
    #  Consumed cannot exceed prepared
    if total_consumed > total_prepared:
        print("Error: Consumed amount cannot be greater than prepared amount. Record discarded.")
        return

    total_wasted = total_prepared - total_consumed
    # Create the record (before redistribution)
    record = FoodRecord(
        id=next_id,
        date=date,
        food_item_name=food_item_name,
        total_prepared=total_prepared,
        total_consumed=total_consumed,
        total_wasted=total_wasted,
        price=price,
        redistributed_to=''
    )
    print("\nRecord before redistribution:")
    print(record.__dict__)
    # If wastage detected, prompt for redistribution
    if total_wasted > 0:
        choice = input("Do you want to redistribute this now? (y/n): ").strip().lower()
        if choice == 'y':
            ngos = read_ngos(NGO_CSV)
            ngo_row = ngos.sample(1).iloc[0]  # Randomly select an NGO
            record.redistributed_to = ngo_row['unique_id']
            # Log the redistribution
            log_redistribution(REDIST_LOG_CSV, date, food_item_name, total_wasted, ngo_row)
            print(f"Redistributed {total_wasted} kg of {food_item_name} to NGO: {ngo_row['ngo_name']}")
            print("\nRecord after redistribution:")
            print(record.__dict__)
    # Save the record
    append_food_record(datafile, record)
    print("Record added.") 
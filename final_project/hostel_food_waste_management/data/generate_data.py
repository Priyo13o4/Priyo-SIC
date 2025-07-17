#Since we couldn't find a dataset which met our requirements, we have generated a sample dataset with random data using this script
#The values will be a bit absurd 
import csv
import random
from datetime import datetime, timedelta

filename = "/Volumes/My Drive/Priyodip/college notes and stuff/Coding stuff (Vs code)/sic/Priyo-SIC/final_project/hostel_food_waste_management/data/food_records.csv"

#Some random food items that are avilable in a hostel
food_items1 = [
    "Rice", "Chapati", "Chicken Biryani", "Naan","Fried Rice"
]
food_items2 = [
    "Mixed Veg","Dal", "Chicken Curry", "Egg Curry", "Paneer Butter Masala", "Aloo Gobi", "Sambar"
]

# Generate sample data
def generate_data(num_rows):
    start_date = datetime.strptime("2025-06-01", "%Y-%m-%d") 
    rows = []
    id = 1

    for day in range(num_rows):
        date = (start_date + timedelta(days=day)).strftime("%Y-%m-%d") 
        
        num_items = random.randint(2, 4) # Choose number of items for the day (2-4)
        
        n1 = random.randint(1, num_items - 1) # Ensure at least one from each list
        n2 = num_items - n1
        items1 = random.sample(food_items1, n1)
        items2 = random.sample(food_items2, n2)
        items_today = items1 + items2
        random.shuffle(items_today)

        for food_item_name in items_today: # Generate data for each item
            total_prepared = round(random.uniform(10,30), 2) 
            total_consumed = round(total_prepared * random.uniform(0.7, 0.95), 2) # Consumed a percentage of prepared
            total_wasted = round(total_prepared - total_consumed, 2) 
            price = round(random.uniform(40, 120), 2) 
            rows.append([
                id, date, food_item_name, total_prepared, total_consumed, total_wasted, price
            ])
            id += 1
    
    return rows

# Generate data
data = generate_data(50)

# Write to CSV
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "date", "food_item_name", "total_prepared", "total_consumed", "total_wasted", "price"])
    writer.writerows(data)
print(f"Data has been written to {filename}")
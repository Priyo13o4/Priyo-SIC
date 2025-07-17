import pandas as pd
from typing import Dict

#total wastage per day.
def daily_wastage_report(df: pd.DataFrame) -> pd.DataFrame:              
    
    return df.groupby('date')['total_wasted'].sum().reset_index(name='total_wasted')

# total wastage per food item, sorted descending.
def high_wastage_items(df: pd.DataFrame) -> pd.DataFrame:                
    return df.groupby('food_item_name')['total_wasted'].sum().reset_index(name='total_wasted').sort_values(by='total_wasted', ascending=False)

#total wastage per day (for plotting trends).
def wastage_trend_over_time(df: pd.DataFrame) -> pd.DataFrame:         

    return df.groupby('date')['total_wasted'].sum().reset_index()

# Items with surplus (prepared > consumed).
def surplus_items(df: pd.DataFrame) -> pd.DataFrame:                
    
    df['surplus'] = df['total_prepared'] - df['total_consumed']
    return df[df['surplus'] > 0][['date', 'food_item_name', 'surplus']]

#Predict the preparation amount for a food item using a weighted average of the last N days.
def predict_preparation_amount(df: pd.DataFrame, food_item_name: str, days: int = 30) -> float:
  
    recent = df[df['food_item_name'] == food_item_name].sort_values(by='date', ascending=False).head(days) 
    if recent.shape[0] == 0:
        return 0.0
    #If less than 3 records, falls back to simple average.
    if recent.shape[0] < 3: 
        return round(recent['total_consumed'].mean(), 2)
    # Weighted average: more recent days have higher weight
    weights = list(range(recent.shape[0], 0, -1))
    weighted_sum = (recent['total_consumed'] * weights).sum()
    total_weight = sum(weights)
    return round(weighted_sum / total_weight, 2)

#Returns the total monetary value of all food wasted.
def total_wastage_cost(df: pd.DataFrame) -> float:

    return round((df['total_wasted'] * df['price']).sum(), 2)

#Returns the top N food items by total wastage cost.
def high_cost_wastage_items(df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    df['wastage_cost'] = df['total_wasted'] * df['price']
    items = df.groupby('food_item_name')['wastage_cost'].sum().reset_index()
    items = items.sort_values(by='wastage_cost', ascending=False).head(top_n)
    return items

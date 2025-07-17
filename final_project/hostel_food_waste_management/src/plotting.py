import matplotlib.pyplot as plt
import pandas as pd

def plot_wastage_trend(df: pd.DataFrame):
    trend = df.groupby('date')['total_wasted'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    plt.plot(trend['date'], trend['total_wasted'], marker='o')
    plt.title('Food Wastage Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Wasted (kg)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_high_wastage_items(df: pd.DataFrame, top_n: int = 5):
    items = df.groupby('food_item_name')['total_wasted'].sum().reset_index()
    items = items.sort_values(by='total_wasted', ascending=False).head(top_n)
    plt.figure(figsize=(8, 5))
    plt.bar(items['food_item_name'], items['total_wasted'])
    plt.title(f'Top {top_n} High Wastage Food Items')
    plt.xlabel('Food Item')
    plt.ylabel('Total Wasted (kg)')
    plt.tight_layout()
    plt.show()

def plot_daily_breakdown(df: pd.DataFrame, date: str):
    day_df = df[df['date'] == date]
    if day_df.empty:
        print(f"No records found for {date}.")
        return
    plt.figure(figsize=(8, 5))
    plt.bar(day_df['food_item_name'], day_df['total_wasted'])
    plt.title(f'Wastage Breakdown for {date}')
    plt.xlabel('Food Item')
    plt.ylabel('Wasted (kg)')
    plt.tight_layout()
    plt.show() 
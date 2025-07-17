from dataclasses import dataclass

FOOD_RECORD_FIELDS = [
    'id',
    'date',
    'food_item_name',
    'total_prepared',
    'total_consumed',
    'total_wasted',
    'price',
    'redistributed_to' 
]

@dataclass
class FoodRecord:
    id: int
    date: str
    food_item_name: str
    total_prepared: float
    total_consumed: float
    total_wasted: float
    price: float
    redistributed_to: str = ''  # default empty if not redistributed 
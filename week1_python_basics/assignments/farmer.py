# Mahesh's land and crops
# Total land = 80 acres, divided into 5 segments
# 1: Tomatoes, 2: Potatoes, 3: Cabbage, 4: Sunflower, 5: Sugarcane

# Each segment size
segment_size = 80 // 5  # 16 acres per crop

# Tomato calculations
# 30% of tomato land: 10 tonnes/acre, 70%: 12 tonnes/acre, price: Rs. 7/kg
# 1 tonne = 1000 kg

tomato_land = segment_size

tomato_30 = 0.3 * tomato_land  # acres

tomato_70 = 0.7 * tomato_land  # acres

tomato_yield_30 = tomato_30 * 10  # tonnes

tomato_yield_70 = tomato_70 * 12  # tonnes

tomato_total_yield = tomato_yield_30 + tomato_yield_70  # tonnes

tomato_total_kg = tomato_total_yield * 1000

tomato_sales = tomato_total_kg * 7

# Potato calculations
# yield: 10 tonnes/acre, price: Rs. 20/kg
potato_land = segment_size
potato_yield = potato_land * 10  # tonnes
potato_kg = potato_yield * 1000
potato_sales = potato_kg * 20

# Cabbage calculations
# yield: 14 tonnes/acre, price: Rs. 24/kg
cabbage_land = segment_size
cabbage_yield = cabbage_land * 14  # tonnes
cabbage_kg = cabbage_yield * 1000
cabbage_sales = cabbage_kg * 24

# Sunflower calculations
# yield: 0.7 tonnes/acre, price: Rs. 200/kg
sunflower_land = segment_size
sunflower_yield = sunflower_land * 0.7  # tonnes
sunflower_kg = sunflower_yield * 1000
sunflower_sales = sunflower_kg * 200

# Sugarcane calculations
# yield: 45 tonnes/acre, price: Rs. 4000/tonne
sugarcane_land = segment_size
sugarcane_yield = sugarcane_land * 45  # tonnes
sugarcane_sales = sugarcane_yield * 4000

# a. Overall sales from 80 acres
overall_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

print("a. Overall sales from 80 acres: Rs.", int(overall_sales))

# b. Sales realisation from chemical-free farming at the end of 11 months
# Chemical-free: All vegetables (tomato, potato, cabbage) after 6 months
# + Sunflower after 10 months (6+4)
# + Sugarcane after 14 months (6+4+4), but only 11 months passed, so sugarcane is NOT included
# So, chemical-free sales after 11 months: tomato + potato + cabbage + sunflower

chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales

print("b. Sales from chemical-free farming at end of 11 months: Rs.", int(chemical_free_sales))

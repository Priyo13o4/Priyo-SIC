#program9.py

import pandas as pd

def read_csv_file():
    #Define the path to the Excel file
    file_path = "/Users/priyodip/Desktop/Jupyter /AIML-SEM4/students.csv"

    # Read the Excel file into a pandas DataFrame
    df = pd.read_csv(file_path)

	# Display the first few rows of the DataFrame
    print(df.count())
    print(df.head())
    print(df.tail())

def read_csv_file1():
    file_path = "/Users/priyodip/Desktop/Jupyter /AIML-SEM4/students.csv"
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        print(row[0], '  ', row[1])

def read_csv_file2():
    file_path = "/Users/priyodip/Desktop/Jupyter /AIML-SEM4/students.csv"
    df = pd.read_csv(file_path)
    for row in df.iterrows():
       print(row[1][0], row[1][1])

read_csv_file()
read_csv_file1()
read_csv_file2()

# ------------------------------------------------------------
# program10.py

#Difference between np.arange() and np.linspace()

# Explanation: np.arange() generates values with a fixed step, while np.linspace() generates a set number of equally spaced values
import numpy as np
sequence_arange = np.arange(1, 10, 3)  # Generates values from 1 to 10 with a step of 3
sequence_linspace = np.linspace(0, 100, 5)  # Generates 5 equally spaced values between 0 and 100
print("Using arange:", sequence_arange)
print("Using linspace:", sequence_linspace)
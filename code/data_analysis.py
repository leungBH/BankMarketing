import pandas as pd
import pandas as numpy

original_data_path = "../original_data/bank-additional.csv"
processed_data_path = "../processed_data/bank-additional.csv"

bank_data_small = pd.read_csv("original_data_path") 

print(bank_data_small.head())

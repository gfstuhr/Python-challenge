#Importing modules
import os
import csv

#Assigning Empty Lists
Month_Count = []
Revenue = []
avg = []
increase = []
decrease = []

#assigning file path
PyBank_data = os.path.join("Resources", "budget_data.csv")

with open(PyBank_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    


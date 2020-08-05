import os
import csv
from decimal import *

with open('Resources/budget_data.csv') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter = ',')

    # skip header row
    next(csvreader)

    months = 0
    total = 0

    # variable to be used in determining average changes. Takes values of column 2 ('Profits/Losses')
    col2_list = []

    profit_loss = []

    

    for row in csvreader:

        # numbers are formatted as strings. Changes them into integers
        row[1] = int(row[1])

        # total number of months included in dataset
        months = months + 1

        # net total amount of "Profits/Losses" over entire period
        total = total + row[1]

        # creates a list of all values in "Profits/Losses" column. to be used in finding average changes
        col2_list.append(row[1])


    temp_val = 0

    # average of the changes in "Profits/Losses" over entire period
    for x in range(len(col2_list) - 1):

        diff_val = col2_list[x+1] - col2_list[x]
        temp_val += diff_val

    prof_loss = round(temp_val/months, 2)



    # min/max
    col2_sorted = sorted(col2_list)
    min1 = col2_sorted[0]
    max1 = col2_sorted[-1]

    #Print to terminal
    print(f"""
    John's Financial Analysis
    ------------------------------------
    total months: {months}
    net total: ${total}
    average change: ${prof_loss}
    greatest profit: ${max1[1]}
    greatest loss: ${min1[1]}
        """)


#Export to text file

file = open('budge_file.txt', 'w')

file.write('Financial Analysis\n')
file.write('------------------------------------\n')
file.write(f'total months: {months}\n')
file.write(f'net total: ${total}\n')
file.write(f'average change: ${prof_loss}\n')
file.write(f'greatest profit: ${max1[1]}\n')
file.write(f'greatest loss: ${min1[1]}\n')

file.close()
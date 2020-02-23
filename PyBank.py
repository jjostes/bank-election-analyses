import os
import csv
from decimal import *

with open('../budget_data.csv') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter = ',')

    next(csvreader)

    months = 0
    total = 0
    profit_loss = []

    for row in csvreader:

        row[1] = int(row[1])

        #Total number of months
        months = months + 1

        #Net total
        total = total + row[1]

        #Average (limiting decimal to 2 places will not work for numbers <> 8 figures)
        getcontext().prec = 8
        average = Decimal(total) / Decimal(months)

        #Max/Min
        profit_loss.append((row[0], row[1]))

    profit_loss = sorted(profit_loss, key=lambda profit_loss: profit_loss[1])

    max1 = profit_loss[-1]
    min1 = profit_loss[0]

    #Print to terminal
    print(f"""
    John's Financial Analysis
    ------------------------------------
    total months: {months}
    net total: ${total}
    average change: ${average}
    greatest profit: {max1[0]} ${max1[1]}
    greatest loss: {min1[0]} ${min1[1]}
        """)


#Export to text file

file = open('budge_file.txt', 'w')

file.write('Financial Analysis\n')
file.write('------------------------------------\n')
file.write(f'total months: {months}\n')
file.write(f'net total: ${total}\n')
file.write(f'average change: ${average}\n')
file.write(f'greatest profit: {max1[0]} ${max1[1]}\n')
file.write(f'greatest loss: {min1[0]} ${min1[1]}\n')

file.close()
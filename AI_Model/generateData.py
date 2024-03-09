import xlsxwriter
import random
from datetime import datetime, timedelta
import numpy as np

size = 10000

outWorkbook = xlsxwriter.Workbook("aankooplijst.xlsx")
outSheet = outWorkbook.add_worksheet()


# generate headers
outSheet.write("A1","Am_prod")
outSheet.write("B1","Retour_ratio")
outSheet.write("C1","Price")
outSheet.write("D1","Risk")

#amount of products
median = 4
std_deviation = 2
max_prod = 15

# Generate random values with a normal distribution (mean=median, std=std_deviation)
am_products = np.random.normal(loc=median, scale=std_deviation, size=size)

# Ensure all values are higher than 1
am_products = np.maximum(am_products, 1)
am_products = np.minimum(am_products, max_prod)
am_products = am_products.astype(int)


for t in range(size):
    outSheet.write(t+1,0,am_products[t])
   


# retour ratio
median = 40
std_deviation = 20    

ratios = np.random.normal(loc=median, scale=std_deviation, size=size)

# Ensure all values are higher than 1
ratios = np.maximum(ratios, 1)
ratios = np.minimum(ratios, 100)
ratios = ratios.astype(int)



for t in range(size):
    outSheet.write(t+1,1,ratios[t])
    

#kostprijs producten
median = 100
std_deviation = 30
max_cost = 300

total_cost = np.random.normal(loc=median, scale=std_deviation, size=size)

ratios = np.maximum(ratios, 1)
ratios = np.minimum(ratios, 200)
ratios = ratios.astype(int)

for m in range(size):
    outSheet.write(m+1,2,total_cost[m])

#risk
    
risks = (total_cost/max_cost+am_products/max_prod)*ratios
risks = np.maximum(risks, 0)
risks = np.minimum(risks, 100)
ratios = ratios.astype(int)

for m in range(size):
    outSheet.write(m+1,3,risks[m])
   
   

outWorkbook.close()

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 23:59:15 2024

@author: Karl
"""

import xlsxwriter
import random
from datetime import datetime, timedelta
import numpy as np

outWorkbook = xlsxwriter.Workbook("personenlijst.xlsx")
outSheet = outWorkbook.add_worksheet()


# maak titels aan

#specificatie aankoop 
outSheet.write("B1","Specificatie aankoop ")

outSheet.write("A2","Aankoop")
outSheet.write("B2","Tijdstip")
outSheet.write("C2","datum")
outSheet.write("D2","aantal producten")
outSheet.write("E2","kostprijs producten")
outSheet.write("F2","welke producten") #schoenen, broek , t shirt , pull , jas 
outSheet.write("G2","aantal keer gekochte producten bekeken(24h)")
outSheet.write("H2","op verlanglijstje?") # 0:nee 1:ja



#voorgeschiedenis
outSheet.write("J1","Voorgeschiedenis")

outSheet.write("J2","aantal retours")
outSheet.write("K2","aantal producten gekocht")
outSheet.write("L2","aantal jaar klant")


#achteraf info 
outSheet.write("N1","Info achteraf")

outSheet.write("N2","aantal producten retour")  # nee:0 ja:1
outSheet.write("O2","aantal producten bekeken(if)")
outSheet.write("P2","aantal producten in verlanglijstje(if)")
outSheet.write("Q2","zelfde product gehouden?")               # -1:nee 1:ja 0: niet van toepassing
outSheet.write("R2","kostprijs retour")
outSheet.write("S2","duur tot retour")


#
## specificatie aankoop
#



# persoon
persons_list = [f"aankoop {i}" for i in range(1, 201)]

for m in range(len(persons_list)):
    outSheet.write(m+2,0,persons_list[m])


# tijdstip
random_times = []

for _ in range(len(persons_list)):
    hour = random.randint(0, 23)  # Random hour between 0 and 23
    minute = random.randint(0, 59)  # Random minute between 0 and 59
    time_str = f"{hour:02d}{minute:02d}"  # Format hour and minute as two digits
    outSheet.write(_+2,1,int(time_str))
    random_times.append(int(time_str))  # Convert the time to an integer and add to the list




# datum
random_dates = []
start_date = datetime(2022, 1, 1)  # Start date
end_date = datetime(2022, 12, 31)   # End date

for _ in range(len(persons_list)):
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    random_dates.append(random_date)
    
for t in range(len(persons_list)):
    date = random_dates[t]
    outSheet.write(t+2,2,date.strftime("%Y/%m/%d"))
    
    
    
    
#aantal producten 
median = 3
std_deviation = 2

# Generate random values with a normal distribution (mean=median, std=std_deviation)
aantal_producten = np.random.normal(loc=median, scale=std_deviation, size=len(persons_list))

# Ensure all values are higher than 1
aantal_producten = np.maximum(aantal_producten, 1)
aantal_producten = aantal_producten.astype(int)


for t in range(200):
    outSheet.write(t+2,3,aantal_producten[t])
    

#kostprijs producten 
median = 30
std_deviation = 30

for m in range(len(persons_list)):
    q = aantal_producten[m]
    lijst = []
    for z in range(q):
        getal = np.random.normal(loc=median, scale=std_deviation)
        getal = round(getal)
        if getal < 20:
            getal = 20
        lijst.append(getal)
    outSheet.write(m+2,4,str(lijst))
    
    
    
#welke producten
choices = ['schoenen', 'broek','t-shirt','pull','jas']
weights = [0.20, 0.20, 0.20, 0.20, 0.20]


for m in range(len(persons_list)):
    lijst = []
    aantal = aantal_producten[m]
    for z in range(aantal):
        lijst.append(random.choices(choices, weights=weights ))
    outSheet.write(m+2,5,str(lijst))

#aantal keer product bekeken 
median = 4
std_deviation = 2

for m in range(len(persons_list)):
    lijst = []
    aantal = aantal_producten[m]
    for z in range(aantal):
        getal = np.random.normal(loc=median,scale=std_deviation)
        getal = round(getal)
        if getal < 1:
            getal = 1
        lijst.append(getal)
    outSheet.write(m+2,6,str(lijst))
    
#op verlanglijstje
choices = [0, 1] # 0:nee 1:ja
weights = [0.75, 0.25]

for m in range(len(persons_list)):
    lijst = []
    aantal = aantal_producten[m]
    for z in range(aantal):
        getal = random.choices(choices, weights=weights)
        lijst.append(getal)
    outSheet.write(m+2,7,str(lijst))
    




#Meerdere aankopen kunnen aan 1 persoon gelinkt worden
#nijgevolg is de voorgeschiedenis bij deze quasi hetzelfde
# neem als een assumptie aan dat dit hetzelfde is


# aantal aankopen 1 persoon 
median = 4
std_deviation = 2 

aantal_aankopen = 0

if aantal_aankopen < 200:
    aantal = np.random.normal(loc=median,scale=std_deviation)
    aantal = round(aantal)
    if 6 < aantal:
        aantal = 6 
        







   
        
#
## voorgeschiedenis
#

    


    
    
    
    
  
    
    
    
    
    
    















    
# Define the choices and their respective probabilities
choices = ['ja', 'nee']
weights = [0.25, 0.75]

# Generate a random list with 'ja' occurring 25% of the time and 'nee' occurring 75% of the time
random_list = random.choices(choices, weights=weights, k=200)

for t in range(len(persons_list)):
    outSheet.write(t+2,54,random_list[t])


    
#aantal keer website 
# Set the parameters
median = 4
std_deviation = 3
num_values = 200

# Generate random values with a normal distribution (mean=median, std=std_deviation)
random_values = np.random.normal(loc=median, scale=std_deviation, size=num_values)

# Round the values to the nearest integer
random_values = np.round(random_values)

# Ensure all values are positive
random_values = np.abs(random_values)

# Convert to integer type
random_values = random_values.astype(int)

for t in range(200):
    outSheet.write(t+2,55,random_values[t])


#aantal keer niet naar product gekocht gekeken
# Set the parameters
median = 2
std_deviation = 1
num_values = 200

# Generate random values with a normal distribution (mean=median, std=std_deviation)
less_value = np.random.normal(loc=median, scale=std_deviation, size=num_values)

# Ensure all values are positive and round to the nearest integer
less_value = np.abs(np.round(less_value))

# Clip any negative values to 0
less_value = np.clip(less_value, 0, np.inf)


# Subtract 'less_value' from 'random_values'
result = random_values - less_value

# Ensure all values are at least 1
result[result < 1] = 1

for t in range(200):
    outSheet.write(t+2,57,result[t])





# Define the choices and their respective probabilities
choices = ['ja', 'nee']
weights = [0.50, 0.50]

# Generate a random list with 'ja' occurring 25% of the time and 'nee' occurring 75% of the time
random_list_2 = random.choices(choices, weights=weights, k=200)

for t in range(200):
    outSheet.write(t+2,67,random_list_2[t])



#kostprijs bestelling
# Set the parameters
median = 60
std_deviation = 60
num_values = 200

# Generate random values with a normal distribution (mean=median, std=std_deviation)
random_values_2 = np.random.normal(loc=median, scale=std_deviation, size=num_values)

# Ensure all values are positive
random_values_2 = np.abs(random_values_2)

# Round the values to the nearest integer
random_values_2 = np.round(random_values_2)

# Convert to integer type
random_values_2 = random_values_2.astype(int)

# Ensure all values are positive and non-zero
random_values_2[random_values_2 <= 0] = 1

# Ensure all values are higher than 20
random_values_2[random_values_2 <= 20] = 21

for t in range(200):
    outSheet.write(t+2,77,random_values_2[t])

# Print the generated list
print(random_values_2)

























#vul al de namen in

#for n in range(len(lijst)):
#    outSheet.write(n+1,0,lijst[n])
#    outSheet.write(n+1,3,materiaal[n])
#    outSheet.write(n+1,4,gewicht[n])
#    outSheet.write(n+1,5,demurrage[n])

#for m in range(len(lijst)):
#    jaar = data[m][0]
#    maand = data[m][1]
#    dag = data[m][2]
#    uur = data[m][3]
#    minuut = data[m][4]
#    MaandNul = ""
#    DagNul = ""
#    UurNul = ""
#    MinuutNul = ""
#    if maand < 10:
#        MaandNul = "0"
#    if dag < 10:
#        DagNul = "0"
#    if uur < 10:
#        UurNul = "0"
#    if minuut<10:
#        MinuutNul = "0"
    
    
#    DeDatum = DagNul + str(dag) + "/" + MaandNul + str(maand) + "/" + str(jaar)
#    HetTijdstip = UurNul + str(uur) + ":" + MinuutNul + str(minuut)
#    outSheet.write(m+1,1,DeDatum)
#    outSheet.write(m+1,2,HetTijdstip)
#    print(DeDatum)
  



outWorkbook.close()

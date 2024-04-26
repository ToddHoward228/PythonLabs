import csv
import os

try:
    
    with open("DataBase.csv","r") as input_base:
        reader = csv.DictReader(input_base, delimiter = ";")
    
        print("Country", ': ', "Most Recent Value")
    
        for row in reader:
            print(row["Country"], ': ', row["Most Recent Value"])
            
    
    input_base.close()
    output_base = open("OutputBase.csv", "w")
    writer = csv.writer(output_base, delimiter = ";")
    
    searching_item = " "
    
    while(searching_item != ""):
        searching_item = input ("Введіть країну, або натисніть ентер для виходу: ")
        
        input_base = open("DataBase.csv","r")
        reader = csv.reader(input_base, delimiter = ";")
        
        crutch = True 
    
        for row in reader:
            if(row[0] == searching_item):
                writer.writerow(row)            
                print("Дані занесені в базу даних")
                crutch = False
                
        if crutch:
            print("Даних не дзнайдено в базі даних")
    
except:
    print("Все накрилось, бази даних нема")

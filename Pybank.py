#Dependencies
import os
import csv

#csv file wasn't opening properly from my OS so I googled how to overpass the pathname as absolute typically it would be file path as follows: "..", "Resources", "budget.csv"

csvpath = os.path.join(os.getcwd(), "budget.csv.txt")

#openthe CSV with new line for lists when outputting new data set in csv.txt file

with open(csvpath, newline="") as csvfile:
    
#read CSV File
 
    csv_reader = csv.reader(csvfile, delimiter=",")

#skip header row so it doesn't affect data calculations

    csv_header_row = next(csvfile)
 
#define exsisting variables and store data in lists[]
  
    Net_Months = []
    Net_Profit_Loss = []
    Greatest_Increase_PL=[]
    Greatest_Decrease_PL=[]

#define variables needed to proceed with calculations
    Total_PL = []
    PL_Entries = 0
    Average_PL = 0
    
#define loop and output total number of months in dataset (row 0 is column 1 and row 1 is column 2 in csv file)

    for row in csv_reader:
        Net_Months.append(row[0])   
        Net_Profit_Loss.append(int(row[1]))

#Calculations needed to obtain average, min & max

        Total_PL=sum(Net_Profit_Loss)
        PL_Entries=len(Net_Profit_Loss)
    
#Caculate average of P&L data

        Average_PL=(Total_PL)/(PL_Entries)
 
# calculate the greatest increase/decrease for P&L 

        Greatest_Increase_PL = max(Net_Profit_Loss)
        Greatest_Decrease_PL = min(Net_Profit_Loss)
        
#print findings to python - gitbash output

    print("Financial Data Analysis, PyBank")
    print("_________________________________")
    print("Total Months: ", len(Net_Months))
    print("Net Total: $", sum(Net_Profit_Loss))
    print("Average Change: $", round(Average_PL))  
    print("Greatest P&L Increase: $", Greatest_Increase_PL)
    print("Greatest P&L Decrease: $", Greatest_Decrease_PL)

#Output data analysis as new CSV.Txt File

output_file=os.path.join("Financial Data Analysis, PyBank.csv")

#open output file

with open(output_file, "r") as csvfile: 
    writer=csv.reader(csvfile)


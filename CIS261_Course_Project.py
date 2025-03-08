"""
Name :  N'din Assi 
Course: CIS 216 
Course name: Object Oriented Programming 1. 

"""

print("Welcome to Payrol system") 
"""This program automates the payrol system 
"""
print("Developed by Assi")

def main():
    number_of_employees=0
    total_hourss=0
    total_gross_pay=0 
    total_net_pay=0
    total_tax=0
    FromDate=[]
    ToDate=[]
    employeeNAME=[]
    totalHOURS=[]
    hourlyRATES=[]
    incomeTAX=[]
    details={"Number of Employees":number_of_employees,
             "total hours":total_hourss, 
             "total tax":total_tax,
             "Total net pay": total_net_pay
             
             
             }
    
    program_terminator="start"
    while program_terminator !="end": 
        
        program_terminator = input(" Do you wish to add another employee?").lower()
        #taking user input and changing it to lowercase, I should implement exception for handling integer entry
        if program_terminator=="end":
            employeesdetails(FromDate,ToDate,employeeNAME,totalHOURS,hourlyRATES,incomeTAX)
            details={"Number of Employees":number_of_employees,
             "total hours":total_hourss, 
             "total tax":total_tax,
             "Total net pay": total_net_pay
             
             
             }
            print(details)
            break 
        fromdate,todate=dateFromTo()
        employeename=employeeName()
        total_hours= totalHours()
        hourly_rates=hourlyRates()
        income_tax=incomeTax()
        grosspay,income_tax,net_pay=grossPay(total_hours,hourly_rates,income_tax)
        displayInfo(employeename,total_hours,hourly_rates,grosspay,income_tax,net_pay)
        number_of_employees= number_of_employees +1 
        total_hourss=total_hours+total_hours
        total_gross_pay=total_gross_pay + grosspay 
        total_net_pay=total_net_pay+net_pay
        total_tax= total_tax+income_tax


        #summary(details)
        details={"Number of Employees":number_of_employees,
             "total hours":total_hourss, 
             "total tax":total_tax,
             "Total net pay": total_net_pay
             
             
             }
        FromDate.append(fromdate)
        ToDate.append(todate)
        employeeNAME.append(employeename)
        totalHOURS.append(total_hours)
        hourlyRATES.append(hourly_rates)
        incomeTAX.append(income_tax)
        #print(f"{FromDate},\n {ToDate}, \n {employeeNAME}, \n {totalHOURS}, \n{incomeTAX}")
        summary(details)
   
    
    
def employeeName():
    employee = input("Enter Employee name: ").capitalize()
    
    return employee

def totalHours():
    total_hours= float(input("Enter number of hours worked:  " ))
    return total_hours
def hourlyRates():
    hourly_rates= float(input("Enter hourly rates: "))
    return hourly_rates
def incomeTax():
    income_tax=float(input("Enter IncomeTax: "))
    return income_tax

def grossPay(total_hours,hourly_rates,tax_rate):
    
    grosspay= total_hours *hourly_rates
    income_tax=grosspay*tax_rate
    net_pay = grosspay-income_tax
    
    return grosspay,income_tax,net_pay

def displayInfo(employeename,totalhours,hourlyrates,grosspay,incometax,netpay):
    print("--------------------------")
    print("Added Employee information ")
    print(f"Employee Name: {employeename}")
    print(f"Total Hours: {totalhours}")
    print(f"Hourly rates: {hourlyrates}")
    print(f"Gross pay:  {grosspay}")
    print(f"Income Tax: {incometax}")
    print(f" Net Pay: {netpay} ")
    print("------------------------------")
    
def summary(dict_details):
    #modify this function to take in dictionary 
    print("--------------------------")
    print("PAYROL SUMMARY")
    #loop over the dictionary
    for x,y in dict_details.items():
        print(x,y)

    
  
def dateFromTo():
    FromDate=input("Enter from date (i.e mm/dd//yyyy: )")
    ToDate=input("Enter to date (i.e mm/dd/yyyy): ")
    return FromDate,ToDate
    

def employeesdetails(fromdate,todate,employeename,totalhours,hourlyrates,incometax):
    for i, name in enumerate(employeename):
        print(f"Employee Name: {name} \n From Date: {fromdate[i]} \n TO Date {todate[i]} \n Total Hours {totalhours[i]}\n Hourly Rate: {hourlyrates[i]} \n Income tax {incometax[i]}")

#employeesdetails(FromDate,ToDate,employeeNAME,totalHOURS,hourlyRATES,incomeTAX)
   
    
    
if __name__=="__main__":
    main()

    
                  

    

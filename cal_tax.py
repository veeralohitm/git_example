#Assigning values using muliple assignments
s,r,a = 300001,32,60400
# Function that caluclates tax
def calculate_tax(income):
  tax = ((income-s)*(r/100))+a
  print('$',tax)

salary = 350000
calculate_tax(salary)

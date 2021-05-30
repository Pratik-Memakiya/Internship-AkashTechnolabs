print("1======================================================================")
#calculate average of 5 numbers.
print("enter the five numbers")
sum=0
for i in range(5):
    number=int(input("enter the numbers :"))
    sum=sum+number
print("average is :",sum/5)

#check whether number is even or odd
print("2======================================================================")

print("enter the number to check even or odd")
num=int(input("the number is: "))
if num%2==0:
    print( num," is even " )
else:
    print( num," is odd ")


#  program to check if year is a leap year or not
print("3======================================================================")

print("the year to check for  the leap year ")
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

   print("4======================================================================")

print("gratest number of the two")

number = []
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] == number[1]:
    print(f'{number[0]} and {number[1]} are equal.')
elif number[0] > number[1]:
    print(f'{number[0]} is greater than {number[1]}.')
else:
    print(f'{number[1]} is greater than {number[0]}.')

print("6======================================================================")

print("factorial of a number")

number = int(input('Enter the number: '))
fact = 1

if number < 0:
    print("Factorial doesn't exists for negative number.")
elif number == 0:
    print('Factorial of 0 is 1.')
else:
    for i in range(1, number+1):
        fact = fact * i
    print('Factorial of {} is {}.'.format(number,fact))

print("7======================================================================")

print("swap two numbers")

number = []
temp = 0
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

temp = number[0]
number[0] = number[1]
number[1] = temp

print(f'number1 is {number[0]}')
print(f'number2 is {number[1]}')

print("8======================================================================")
print("smallest number")
number = []
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] == number[1]:
    print(f'{number[0]} and {number[1]} are equal.')
elif number[0] > number[1]:
    print(f'{number[1]} is smaller than {number[0]}.')
else:
    print(f'{number[0]} is smaller than {number[1]}.')
for i in range(3):

    print("9======================================================================")

    print("number less than 100 and check even or odd")
    number = int(input(f'Enetr the number: '))
    if number > 100:
        print(f'Number is greater than 100.')
    elif number == 100:
        print(f'Number is a 100.')
    else:
     if number % 2 == 0:
        print(f'Number is less than 100 and even.')
     else:
        print(f'Number is less than 100 and odd.')
print("10======================================================================")
print("square of a number :")
  
for i in range(3):
    number = int(input(f'Enter the number: '))
    if number > 10:
        print(f'Number is not less than 10.')
    elif number == 10:
        print(f'Number is a 10.')
    else:
        print(f'Square of {number} is a {number*number}')
print("11======================================================================")
print("check the number whether zero,positive or negative")
for i in range(1):
    number = int(input(f'Enter the number: '))
    if number >= 0:
        if number == 0:
            print(f"{number} is Zero.")
        else:
            print(f"{number} is Positive.")
    else:
        print(f"{number} is Negative.")
print("12======================================================================")
print("take 3 numbers  and find the gratest")
number = []
for i in range(1, 4):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] > number[1]:
    if number[1] > number[2]:
        print(f'{number[0]} is a greatest number.')
    else:
        print(f'{number[2]} is a greatest number.')
elif number[1] > number[0]:
    if number[1] > number[2]:
        print(f'{number[1]} is a greatest number.')
    else:
        print(f'{number[2]} is a greatest number.')
print("13======================================================================")
print("smallest of three numbers :")
number = []
for i in range(1, 4):
    number.append(int(input(f'Enter the number{i}: ')))

if number[0] < number[1]:
    if number[1] < number[2]:
        print(f'{number[0]} is a smallest number.')
    else:
        print(f'{number[2]} is a smallest number.')
elif number[1] < number[0]:
    if number[1] < number[2]:
        print(f'{number[1]} is a smallest number.')
    else:
        print(f'{number[2]} is a smallest number.')

print("14======================================================================")
print("swap two numbers :")  
number = []
for i in range(1, 3):
    number.append(int(input(f'Enter the number{i}: ')))

number[0], number[1] = number[1], number[0]

print(f'number1 is {number[0]}')
print(f'number2 is {number[1]}')

print("15======================================================================")
print("the seqeuence 30 27 24 21.....")

start = int(input(f'Enter the starting number: '))
end = int(input(f'Enter the ending number: '))

for i in range(start, end-1, -3):
    print(i)

inputOne = int(input('Enter the first value you want to input: '))
inputTwo = int(input('Enter the second value you want to input: '))

#Entering a choice
print('Please input "sum " if you want to perform addition ')
print('Please input "substract " if you want to perform addition ')
print('Please input "division " if you want to perform addition ')
print('Please input "multiplication " if you want to perform addition ')

choice = input('Enter the operation you wanna make: ')

if choice == 'sum':
    #Calculating for addition of two numbers
    sum = inputOne + inputTwo
    print('The sum is ', sum)
elif choice == 'substract':
    #Calculating for the substraction of two numbers
    substract = inputOne - inputTwo
    print('The substraction of the value is: ', substract)
elif choice == 'division':
    #Calculating for the Division of two numbers
    division = inputOne/inputTwo
    print('The Division of the two numbers is ', division)
elif choice == 'multiplication':
    #Calculating for the Multiplication of two numbers
    multiplication = inputOne*inputTwo
    print('The Multiplication of the two numbers is ', multiplication)
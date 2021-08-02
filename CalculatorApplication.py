
while True:
    operator = input('Enter operator(+ , -, *, /, squre, cupe, power, //, %, >, stop)... ')
    if operator =='stop':
        break

    first_number = int(input("Enter your first value... "))
    second_number = int(input("Enter your second value... "))

    if operator == "+":
        result = first_number + second_number
        print('Your Result: ', first_number, '+', second_number, '=', result)

    if operator == "-":
        result = first_number - second_number
        print('Your Result: ', first_number, '-', second_number, '=', result)

    if operator == "*":
        result = first_number * second_number
        print ('Your Result: ', first_number, '*', second_number, '=', result)

    if operator == "/":
        result = first_number / second_number
        print ('Your Result: ', first_number, '/', second_number, '=', result)

    if operator == "squre":
        result = first_number * first_number
        print ('Your Result: ', first_number, 'squre', second_number, '=', result)

    if operator == "cupe":
        result = first_number * first_number * first_number
        print ('Your Result: ', first_number, 'cupe', '=', result)

    if operator == "power":
        result = first_number ** second_number
        print ('Your Result: ', first_number, 'power', second_number, '=', result)

    if operator == "//":
        result = first_number // second_number
        print ('Your Result: ', first_number, '//', second_number, '=', result)

    if operator == "%":
        result = first_number % second_number
        print ('Your Result: ', first_number, '%', second_number, '=', result)

    if operator == ">":
        result = first_number > second_number
        print('Your Result is: ',result)
    

print('\n',"Your Task Has Been Finished.....THANK YOU..")
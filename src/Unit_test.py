def calculator(num1, num2, operation):
    if operation == '+':
        answer = num1 + num2
        return answer
    elif operation == '-':
        answer = num1 - num2
        return answer
    elif operation == '*':
        answer = num1 * num2
        return answer
    elif operation == '/':
        if num2 != 0:
            answer = num1 / num2
            return answer
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"


num1 = 2
num2 = 2
operation = '+'
result = calculator(num1, num2, operation)
print(result)
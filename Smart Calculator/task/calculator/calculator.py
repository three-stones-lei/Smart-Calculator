# write your code here
from _collections import deque
class Calculator:
    saved_variables = {}
    is_exit = 0
    def __init__(self):
        pass
    def deal_with_command(command):
        if command == '/exit':
            print('Bye!')
            Calculator.is_exit = 1

        elif command == '':
            pass
        elif command == '/help':
            print('The program can support variables, multiplication, division and parentheses to calculate.')
        else:
            print('Unknown command')

    def deal_with_assignment(assignment_string):
        li = [str(i).strip() for i in assignment_string.split('=', 1)]
        if li[0].isalpha() == False:
            print('Invalid identifier')
        elif li[1].isdigit() == False:
            if li[1].isalpha():
                if li[1] not in Calculator.saved_variables:
                    print('Unknown variable')
                else:
                    Calculator.saved_variables[li[0]] = Calculator.saved_variables[li[1]]
            else:
                print('Invalid assignment')
        else:
            Calculator.saved_variables[li[0]] = int(li[1])


    def deal_with_variable_display(variable):
        if str(variable).isalpha() == False:
            print('Invalid identifier')
        elif str(variable) not in Calculator.saved_variables:
            print('Unknown variable')
        else:
            print(Calculator.saved_variables[str(variable)])

    def deal_with_operator(input_string):
        operator_priority = {'+':1, '-':1, '*':2, '/':2}
        postfix_deque = deque()
        operator_stack = deque()
        result_stack = deque()
        if str(input_string).isnumeric():
            print(input_string)
            return
        infix = list(str(input_string).replace(' ', ''))

        for i in range(len(infix)):
            if i+1 <= len(infix)-1:
                if str(infix[i]).isdigit():
                    if str(infix[i+1]).isdigit():
                        infix[i] = str(infix[i])+str(infix[i+1])
                        del infix[i+1]

        try:
            for element in infix:
                if str(element).isdigit():
                    postfix_deque.append(element)
                elif str(element).isalpha():
                    if str(element) in Calculator.saved_variables:
                        postfix_deque.append(Calculator.saved_variables[element])
                    else:
                        print('Unknown variable')
                        return
                elif str(element) in ('+', '-', '*', '/'):
                    if len(operator_stack) == 0 or operator_stack[-1] == '(':
                        operator_stack.append(element)
                    elif operator_priority[element] > operator_priority[operator_stack[-1]]:
                        operator_stack.append(element)
                    elif operator_priority[element] <= operator_priority[operator_stack[-1]]:
                        postfix_deque.append(operator_stack.pop())
                        operator_stack.append(element)
                elif element == '(':
                    operator_stack.append(element)
                elif element == ')':
                    postfix_deque.append(operator_stack.pop())
                    operator_stack.pop()
            for _ in range(len(operator_stack)):
                postfix_deque.append(operator_stack.pop())

            for element in postfix_deque:
                if str(element).isdigit():
                    result_stack.append(int(element))
                elif '+' in str(element):
                    result_stack.append(result_stack.pop() + result_stack.pop())
                elif '-' in str(element):
                    if str(element).count('-') % 2 == 0:
                        result_stack.append(result_stack.pop() + result_stack.pop())
                    else:
                        result_stack.append(- result_stack.pop() + result_stack.pop())
                elif str(element) == '*':
                    result_stack.append(result_stack.pop() * result_stack.pop())
                elif str(element) == '/':
                    result_stack.append((1/result_stack.pop()) * result_stack.pop())
                else:
                    print('Invalid expression')
                    return
        except Exception:
            print('Invalid expression')
        else:
            print(int(result_stack.pop()))

        '''
        try:
            # input_list =[i for i in input_string.split(' ') if i != '']
            input_list = list(filter(lambda i: i!='', input_string.split(' ')))
            for i in range(len(input_list)):
                if i % 2 == 0:
                    if str(input_list[i]).isalpha():
                        if str(input_list[i]) in Calculator.saved_variables:
                            input_list[i] = Calculator.saved_variables[str(input_list[i])]
                        else:
                            print('Unknown variable')
                            return
            # input_list = list(map(lambda i: Calculator.saved_variables[i] if str(i).isalpha() and i in Calculator.saved_variables else print('Unknown variable'), input_list))
            numbers = [int(input_list[0])]
            for i in range(1, len(input_list), 2):
                if '+' in input_list[i]:
                    numbers.append(int(input_list[i + 1]))
                elif '-' in input_list[i]:
                    if input_list[i].count('-') % 2 == 0:
                        numbers.append(int(input_list[i + 1]))
                    else:
                        numbers.append(-1 * int(input_list[i + 1]))

        except Exception:
            print('Invalid expression')
        else:
            print(sum(numbers))
        '''



while True:
    input_content = input()
    if input_content == '':
        pass
    elif input_content.startswith('/'):
        Calculator.deal_with_command(input_content)
        if Calculator.is_exit == 1:
            break
    elif '=' in input_content:
        Calculator.deal_with_assignment(input_content)
    elif len(input_content.split()) == 1 and str(input_content).isalpha():
        Calculator.deal_with_variable_display(input_content)

    elif '+' or '-' or '*' or '/' in input_content:
        Calculator.deal_with_operator(input_content)





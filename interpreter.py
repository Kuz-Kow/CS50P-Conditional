expression = input("Expression: ").strip()

expression = expression.split(" ")

match expression[1]:
    case "*":
        print(int(expression[0])*int(expression[2]))
    case "/":
        print(int(expression[0])/int(expression[2]))
    case "+":
        print(int(expression[0])+int(expression[2]))
    case "-":
        print(int(expression[0])-int(expression[2]))
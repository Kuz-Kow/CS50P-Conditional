answer = input("What is the Answer: ")

match answer:
    case "42" | "fourty-two" | "fourty two":
        print("Yes")
    case _: 
        print("It's not the answer")
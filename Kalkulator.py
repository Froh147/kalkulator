import math
while True:
    print("Выберите операцию: + - * / ** sqrt ! sin cos tg Выход")
    operation = input('')
    if operation == "+" or operation == "-" or operation == "*" or operation== "**":
        try: 
            num1 = float(input('Ввести первое число:'))
        except:
            print("Данные не являются числами")
            exit()
        try: 
                num2 = float(input('Ввести первое число:'))
        except:
            print("Данные не являются числами")
            exit()
        if operation == "+":
                resultat=num1 + num2
                print(resultat)
        elif operation == "-":
                resultat=num1 - num2
                print(resultat)
        elif operation == "*":
                resultat=num1 * num2
                print(resultat)
        elif operation == "**":
                resultat=num1 ** num2
                print(resultat)
    if operation == "/":
            try: 
               num1 = float(input('Ввести первое число:'))
            except:
             print("Данные не являются числами")
             exit()
            try: 
                num2 = float(input('Ввести второе число:'))
            except:
             print("Данные не являются числами")
             exit()
            try:
               result= num1 / num2
               print(resultat)
            except:
                print('Нельзя делить на ноль')
                exit()
    if operation == "sqrt" or operation =="!" or operation=="sin" or operation =="cos" or operation=="tg":
        try: 
            num = int(input('Ввести число:'))
        except:
             print("Данные не являются числами")
             exit()
        if operation == "!":
            try:
                num>0
                resultat=math.factorial(num)
                print(resultat)
            except:
                 print("Не существует отрицательного факториала")
                 exit()
        elif operation == "sqrt":
            try:
                num>0
                resultat=math.sqrt(num)
                print(resultat)
            except:
                 print("Не существует отрицательного корня")
                 exit()
        elif operation == "sin":
            resultat=math.sin(math.radians(num))
            print(resultat)
        elif operation == "cos":
            resultat=math.cos(math.radians(num))
            print(resultat) 
        elif operation == "tg":
            resultat=math.tan(math.radians(num))
            print(resultat)
    if operation == "Выход":
            exit()
        
        
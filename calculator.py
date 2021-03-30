variables = {}
while True:
    user = input().strip()
    if user == "/exit":
        print("Bye!")
        exit()
    elif user == "":
        pass
    elif user == "/help":
        print("The program calculates the sum and difference of numbers")
    elif user.startswith("/"):
        print("Unknown command")
    elif "=" in user:
        if user.count("=") > 1:
            print("Invalid assignment")
            continue
        inputs = user.split("=")
        if "=" in inputs:
            inputs.remove("=")
        var = inputs[0].strip()
        val = inputs[1].strip()
        if not var.isalpha():
            print("Invalid identifier")
        elif val.isalpha() and val not in variables:
            print("Unknown variable")
        elif val.isalpha() and val in variables:
            variables[var] = variables[val]
        elif val.isnumeric():
            variables[var] = val
        else:
            print("Invalid assignment")
    else:
        t = 1
        for i in user.split():
            if i.isalpha():
                try:
                    user = user.replace(i, str(variables[i]))
                except KeyError:
                    print("Unknown variable")
                    t = 0
                    break
        if t:
            if "//" in user:
                print("Invalid expression")
                continue
            try:
                print(int(eval(user)))
            except (SyntaxError, NameError, TypeError, ZeroDivisionError):
                print("Invalid expression")

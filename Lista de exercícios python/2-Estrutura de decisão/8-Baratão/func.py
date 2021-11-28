def economiza(num1, num2, num3):
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    
    if num1 < num2:
        if num1 < num3:
            return "{}".format(num1)
        else:
            return "{}".format(num3)
            
    if num2 < num1:
        if num2 < num3:
            return "{}".format(num2)
        else:
            return "{}".format(num3)
    if num3 < num1:
        if num3 < num2:
            return "{}".format(num3)
        else:
            return "{}".format(num2)
    else:
        return "todos os produtos tem o mesmo valor"
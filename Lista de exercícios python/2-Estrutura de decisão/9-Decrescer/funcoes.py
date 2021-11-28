def verifica(num1, num2, num3, tipo="maior".lower()):
    
    if tipo == "maior":
        if num1 > num2:
            if num1 > num3:
                return "{}".format(num1)
            else:
                return "{}".format(num3)
        if num2 > num1:
            if num2 > num3:
                return "{}".format(num2)
            else:
                return "{}".format(num3)
        if num3 > num1:
            if num3 > num2:
                return "{}".format(num3)  
            else:
                return "{}".format(num2)
        else:
            return "numeros iguais"
            
    if tipo == "medio":
        if num1 > num2:
            if num1 > num3:
                if num2 > num3:
                    return "{}".format(num2)
                else:
                    return "{}".format(num3)
            else:
                return "{}".format(num1)
                
        if num2 > num1:
            if num2 > num3:
                if num3 > num1:
                    return "{}".format(num3)
                else:
                    return "{}".format(num1)
            else:
                return "{}".format(num2)
                
        if num3 > num1:
           if num3 > num2:
               if num2 > num1:
                   return "{}".format(num2)
               else:
                   return "{}".format(num1)
           else:
               return "{}".format (num3)
               
        else:
           return "São iguais"
           
    if tipo == "menor":
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
            return "Iguais"
            
def autor():
    return """
    Autor Clayton Nero Silva
    """    
        
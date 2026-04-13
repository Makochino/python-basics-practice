def number_pattern(n):
    result = ""
    if not isinstance(n,int):
        return "Argument must be an integer value."
    elif n <= 0:
        return "Argument must be an integer greater than 0."
    else:
        for num in range(n+1):
            if num == 0:
                continue
            else:
                result += str(num) + " "
        return result

print(number_pattern(-1))
        
        

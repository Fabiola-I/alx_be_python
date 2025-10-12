def safe_divide(numerator, denominator):
    
    try:
        num1=numerator
        num2=denominator
        result= num1/num2
    except ZeroDivisionError:
        return "Error: Can't divide by zero"
    else:
        print(f"The result is {result}")
        
        
    
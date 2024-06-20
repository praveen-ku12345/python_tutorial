'''def int_to_roman(num):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM"]
    
    return thousands[num // 1000] + hundreds[(num % 1000) // 100] + tens[(num % 100) // 10] + ones[num % 10]

# Example usage:
number = 90
roman = int_to_roman(number)
print(f"The Roman numeral representation of {number} is: {roman}")
'''
'''def result(number):
    number.sort()
number=list(map(str,input("enter the string :").split(",")))
x=result(number)
print(x)'''

'''x=['flower','flow','flight','fl']
x.sort()
print(x)
'''
x=(-5)
print(abs(x))
             
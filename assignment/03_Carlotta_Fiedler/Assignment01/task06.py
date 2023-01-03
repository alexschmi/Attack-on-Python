# Task 06 - Decimal to Octal Conversion
# a) Converting Integers
def int_dec2oct(dec):
    octal = ""
    while dec > 0:
        rest = dec % 8
        dec = dec // 8
        octal = str(rest) + octal
    return int(octal)

# b) Converting Floats (DOES NOT WORK PROPERLY)
def float_dec2oct(dec):
    print("ValueError in float_dec2oct() - returned number is decimal:")
    return(dec)
    whole, comma = str(dec).split(".")
    whole = int(whole)
    comma = int(comma)
    octal = int_dec2oct(whole)

    for x in range(3):
        while comma > 1:
            comma = comma // 10
        whole, comma = str(comma * 8).split(".")
        comma = int(comma)

        octal = octal + whole

    return octal

# Conversion
print('Give a decimal number (integer or float): ')
x = input()
if "." in x:
    octal = float_dec2oct(x)
else:
    x = int(x)
    octal = int_dec2oct(x)
print('Converted into octal number: ' + str(octal))

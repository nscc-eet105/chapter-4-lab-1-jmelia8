#Joe Melia EET-107

def main():
    temp = float(input("What is the current temperature? "))

    scale = input("Did you enter the temerapture in (c)elcius or (f)ahrenheit? ")
    if scale == "c":
        celcius(temp)
    elif scale == "f":
        result = fahrenheit(temp)
        print(f"The current temperature is {temp} fahrenheit this temperature in celcius is {result:.2f}")
    else:
        print("Invalid input, please try again...")

def celcius(degree):
    result = (degree * 9/5) + 32
    print(f"The current temperature is {degree} celcius this temperature in fahrenheit is {result:.2f}")

def fahrenheit(degree):
    result = (degree - 32) * 5/9
    return result
main()

import unittest

#kelvin = str(input("Enter kelvin: "))
#celcius = str(input("Enter celcius: "))
#fahrenheit = str(input("Enter fahrenheit: "))

kelvin = None
celcius = 4
fahrenheit = 1


values = []

class Test(unittest.TestCase):
    values = [x for x in [kelvin, celcius, fahrenheit] if x]
    print(len(values))
    def tester(self):
        #if int(len(values)) < 1:
        #    print("Need argument")
        if int(len(values)) > 1:
            print("only one argument")

        

if __name__ == "__main__":
    unittest.main()

      
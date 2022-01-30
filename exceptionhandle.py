a = 5
b = ''

try:
    print(a/b)

   
except ZeroDivisionError as e:
     print("error.",e)
except Exception as e:
     print("Invalid input.",e)
print("hello")
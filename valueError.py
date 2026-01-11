try :
    num = int(input("enter a number : "))
    print(num)
except ValueError as ex:
    print("exception: ",ex)
print("i am outside the try block")
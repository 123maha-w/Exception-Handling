try:
    num1 = int(input("enter a number : "))
    num2 = int(input("enter a number : "))
    result = num1/num2
    print("result is ",result)
    print("result is ",result)

except ZeroDivisionError:
    print("divsion is not allowed")
except ValueError:
    print("please enter a numrical value: ")
except NameError:
    print("the exception is ",ex)

except:
    print("some error occurred")
finally:
    print("I will execute no mater what happens")
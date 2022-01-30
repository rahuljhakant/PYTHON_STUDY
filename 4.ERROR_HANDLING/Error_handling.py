# Error and In-built Exception in Python

# There are two types of exceptions in Python
# Runtime Error
# Syntax Error also known as compiler time error or exception.

class ExceptionHandle():

    def division(self):
        try:
            a = 10
            b = 0
            print(a/b)

        except ZeroDivisionError:
            print("ZeroDivisionError")
        except Exception as e:
            print("Name of exception is: ", e)
        finally:
            print("Finally block is executed")

    def rasing_Exception(self):
        try:
            raise NameError("Hi there")
        except NameError:
            print("An exception")
        finally:
            print("Finally block is executed")


obj = ExceptionHandle()
obj.division()
obj.rasing_Exception()

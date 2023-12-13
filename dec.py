
def newDecorator(originalFun):

    def wrapFun():
        print("Some Extra code before orginal Function.")

        originalFun()

        print("some Extra code after the orginal Function.")

    return wrapFun


# new function
'''
def  func_needs_decorator():
    print("I want to be the decorated")


func_needs_decorator()

decorated_Fun = newDecorator(func_needs_decorator)

print(decorated_Fun())
'''

@newDecorator
def tryThis():
    print("this is message to all the professional who are not happy in their life.")


tryThis()
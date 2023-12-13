
def hello(name="Akshay"):
    print("hello function has been executed.")

    def greet():
        print("Hi GOodMorning !")

    def Welcome():
        print("Hi, Welcome to the Akshay's Workplace !!")

    print("I am going to return function!")

    if name=="Akshay":
        return greet
    else:
        return Welcome
    

newfun=hello("Akshay")
newfun()



def cool():

    def super_cool():
        return "I am  very cool!"
    
    return super_cool
  
somefun=cool()

print(somefun())


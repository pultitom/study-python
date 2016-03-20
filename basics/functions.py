def hello(name = "everybody"):
    """ Greets person """
    print("Hello " + name + "!")

hello("Peter")
print("function hello has docstring: " + hello.__doc__)

print("\n-- global and local vars in functions --------")
def function1():
    print(global_s)

global_s = "Python"
function1()

def function2():
    global_s = "Perl"
    print(global_s)

function2()
print(global_s)

def function3():
    try:
        print(global_s)
    except UnboundLocalError:
        print("ERROR in function3: global_s is not locally inicialized. app will break!")
    global_s = "something local"
    print(global_s)

function3()
print(global_s)

print("\n-- recursive functions -----------------------")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial_input = 5
print("Factorial of " + str(factorial_input) + " is " + str(factorial(factorial_input)))

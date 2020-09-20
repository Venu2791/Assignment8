# Session 8 – Closures
## Closures :
A closure is a nested function which has access to a free variable from an enclosing function that has finished its execution. Three characteristics of a Python closure are:

it is a nested function
it has access to a free variable in outer scope
it is returned from the enclosing function
A free variable is a variable that is not bound in the local scope. In order for closures to work with immutable variables such as numbers and strings, we have to use the nonlocal keyword.

Python simple closure example:
def make_printer(msg) :
    
    msg = "hi there"
    
    def printer() :
        print(msg)

    return printer


myprinter = make_printer("Hello there")
myprinter()
myprinter()
myprinter()

In the example, we have a make_printer() function, which creates and returns a function . The nested printer() function is the closure .

myprinter = make_printer("Hello there")
The make_printer() function returns a printer() function and assigns it to the myprinter variable . At this moment , it has finished its execution. However , the printer() closure still has access to the msg variable .

## Output :
hi there
hi there
hi there

## Q1 Write a closure that takes a function and then check whether the function passed has a doc string with more than 50 characters . 50 is stored as a free variable .

Here we pass a function to the closure and count the characters in doc string . If the number of characters in the doc string is greater than 50 then the closure returns True . Else it returns False .

## Q2 Write a closure that gives you the next Fibonacci number

This is a classic example of closure , where when a number is given as input , it finds the next fibonacci number . If the closure function is called again it will remeber the previous fibonacci number that it returned as result and will generate and give the next fibonacci number automatically .

## Q3 Write a CLOSURE that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts

A global dictonary is created which keeps track of the number of times each of add or mul or div functions are called . Every time the function is called , the global dictionary is updated . 

## Q4 Modify above such that now we can pass in different dictionary variables to update different dictionaries

Here we create two dictionaries with the add , mul and div function names as keys and when the closure of that particular dictionary is called , only that dictionary gets updated and not the other dictionary . In this way we can differentiate between what function called the closure .


## Test Cases
1)  README exists
2)  README has at least 500 words
3)  Methods mentioned in README
4)  README file formatting 
5)  Code Indentation and spaces
6)  Function name should be in small letters
7)  Docstring in a function has more than 50 characters or not
8)  Whether the closure gives the next fibonacci number or not
9)  Whether the dictionary is updated with the correct number of times each of add or mul or div functions are called
10) Whether each dictionary is updated with the correct number of times each of add or mul or div functions are called

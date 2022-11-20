1. What is Python?
Python is a high-level, interpreted, interactive, and object-oriented scripting language. It uses English keywords frequently. Whereas, other languages use punctuation, Python has fewer syntactic constructions.
Python is designed to be highly readable and compatible with different platforms such as Mac, Windows, Linux, Raspberry Pi, etc.
2. Python is an interpreted language. Explain.
An interpreted language is any programming language that executes its statements line by line. Programs written in Python run directly from the source code, with no intermediary compilation step.

3. What is the difference between lists and tuples?
Lists	Tuples
Lists are mutable, i.e., they can be edited	Tuples are immutable (they are lists that cannot be edited)
Lists are usually slower than tuples	Tuples are faster than lists
Lists consume a lot of memory	Tuples consume less memory when compared to lists
Lists are less reliable in terms of errors as unexpected changes are more likely to occur	Tuples are more reliable as it is hard for any unexpected change to occur
Lists consist of many built-in functions.	Tuples do not consist of any built-in functions.
Syntax:
list_1 = [10, ‘Intellipaat’, 20]

Syntax:
tup_1 = (10, ‘Intellipaat’ , 20)

4. What is pep 8?
PEP in Python stands for Python Enhancement Proposal. It is a set of rules that specify how to write and design Python code for maximum readability.

5. What are the Key features of Python?
The key features of Python are as follows:

Python is an interpreted language, so it doesn’t need to be compiled before execution, unlike languages such as C.
Python is dynamically typed, so there is no need to declare a variable with the data type. Python Interpreter will identify the data type on the basis of the value of the variable.

Python follows an object-oriented programming paradigm with the exception of having access specifiers. Other than access specifiers (public and private keywords), Python has classes, inheritance, and all other usual OOPs concepts.
Python is a cross-platform language, i.e., a Python program written on a Windows system will also run on a Linux system with little or no modifications at all.
Python is literally a general-purpose language, i.e., Python finds its way in various domains such as web application development, automation, Data Science, Machine Learning, and more.

6. How is Memory managed in Python?
Memory in Python is managed by Python private heap space. All Python objects and data structures are located in a private heap. This private heap is taken care of by Python Interpreter itself, and a programmer doesn’t have access to this private heap.
Python memory manager takes care of the allocation of Python private heap space.
Memory for Python private heap space is made available by Python’s in-built garbage collector, which recycles and frees up all the unused memory.
7. What is PYTHONPATH?
PYTHONPATH has a role similar to PATH. This variable tells Python Interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by Python Installer.

8. What are Python Modules?
Files containing Python codes are referred to as Python Modules. This code can either be classes, functions, or variables and saves the programmer time by providing the predefined functionalities when needed. It is a file with “.py” extension containing an executable code.

Commonly used built modules are listed below:

os
sys
data time
math
random
JSON
9. What are python namespaces?
A Python namespace ensures that object names in a program are unique and can be used without any conflict. Python implements these namespaces as dictionaries with ‘name as key’ mapped to its respective ‘object as value’.

Let’s explore some examples of namespaces:

Local Namespace consists of local names inside a function. It is temporarily created for a function call and gets cleared once the function returns.
Global Namespace consists of names from various imported modules/packages that are being used in the ongoing project. It is created once the package is imported into the script and survives till the execution of the script.
Built-in Namespace consists of built-in functions of core Python and dedicated built-in names for various types of exceptions.
Want to become a master in Python programming? Check out this Python Training for Data Science and excel in your Python career!

10. Explain Inheritance in Python with an example?
As Python follows an object-oriented programming paradigm, classes in Python have the ability to inherit the properties of another class. This process is known as inheritance. Inheritance provides the code reusability feature. The class that is being inherited is called a superclass or the parent class, and the class that inherits the superclass is called a derived or child class. The following types of inheritance are supported in Python:

Inheritance in Python
Single inheritance: When a class inherits only one superclass
Multiple inheritance: When a class inherits multiple superclasses
Multilevel inheritance: When a class inherits a superclass, and then another class inherits this derived class forming a ‘parent, child, and grandchild’ class structure
Hierarchical inheritance: When one superclass is inherited by multiple derived classes


11. What is scope resolution?
A scope is a block of code where an object in Python remains relevant.Each and every object of python functions within its respective scope.As Namespaces uniquely identify all the objects inside a program but these namespaces also have a scope defined for them where you could use their objects without any prefix. It defines the accessibility and the lifetime of a variable.

Let’s have a look on scope created as the time of code execution:

A local scope refers to the local objects included in the current function.
A global scope refers to the objects that are available throughout execution of the code.
A module-level scope refers to the global objects that are associated with the current module in the program.
An outermost scope refers to all the available built-in names callable in the program.


12. What is a dictionary in Python?
Python dictionary is one of the supported data types in Python. It is an unordered collection of elements. The elements in dictionaries are stored as key-value pairs. Dictionaries are indexed by keys.

For example, below we have a dictionary named ‘dict’. It contains two keys, Country and Capital, along with their corresponding values, India and New Delhi.

Syntax:

dict={‘Country’:’India’,’Capital’:’New Delhi’, }
Output: Country: India, Capital: New Delhi

13. What are functions in Python?
A function is a block of code which is executed only when a call is made to the function. def keyword is used to define a particular function as shown below:

def function():
print("Hi, Welcome to Intellipaat")
function(); # call to the function
Output:
Hi, Welcome to Intellipaat

14. What is __init__ in Python?
Equivalent to constructors in OOP terminology, __init__ is a reserved method in Python classes. The __init__ method is called automatically whenever a new object is initiated. This method allocates memory to the new object as soon as it is created. This method can also be used to initialize variables.

Syntax

(for defining the __init__ method):
class Human:
# init method or constructor
def __init__(self, age):
self.age = age
# Sample Method
def say(self):
print('Hello, my age is', self.age)
h= Human(22)
h.say()
Output:

Hello, my age is 22

15. What are the common built-in data types in Python?
Python supports the below-mentioned built-in data types:

Immutable data types:

Number
String
Tuple
Mutable data types:

List
Dictionary
set

16. What are local variables and global variables in Python?
Local variable: Any variable declared inside a function is known as Local variable and it’s accessibility remains inside that function only.

Global Variable: Any variable declared outside the function is known as Global variable and it can be easily accessible by any function present throughout the program.

g=4                #global variable
def func_multiply():
l=5       #local variable
m=g*l
return m
func_multiply()
Output: 20
If you try to access the  local variable outside the multiply function then you will end up with getting an error.

17. What is type conversion in Python?
Python provides you with a much-needed functionality of converting one form of data type into the needed one and this is known as type conversion.

Type Conversion is classified into types:

1. Implicit Type Conversion: In this form of type conversion python interpreter helps in automatically converting the data type into another data type without any User involvement.

2. Explicit Type Conversion: In this form of Type conversion the data type inn changed into a required type by the user.

Various Functions of explicit conversion are shown below:

int() –  function converts any data type into integer.
float() –   function converts any data type into float.
ord() – function returns an integer representing the Unicode character

hex() –  function converts integers to hexadecimal strings.

oct() –   function converts integer to octal strings.

tuple() – function convert to a tuple.

set() – function returns the type after converting to set.

list() – function converts any data type to a list type.

dict() – function is used to convert a tuple of order (key,value) into a dictionary.

str() –  function used to convert integer into a string.

complex(real,imag) – function used to convert real numbers to complex(real,imag) numbers.
18. How to install Python on Windows and set a path variable?
For installing Python on Windows, follow the steps shown below:



After that, install it on your PC by looking for the location where PYTHON has been installed on your PC by executing the following command on command prompt;
cmd python.
Visit advanced system settings and after that add a new variable and name it as PYTHON_NAME and paste the path that has been copied.
Search for the path variable -> select its value and then select ‘edit’.
Add a semicolon at the end of the value if it’s not present and then type %PYTHON_HOME%
19. What is the difference between Python Arrays and lists?
List	Array
Consists of elements belonging to different data types	Consists of only those elements having the same data type
No need to import a module for list declaration	Need to explicitly import a module for array declaration
Can be nested to have different type of elements	Must have all nested elements of the same size
Recommended to use for shorter sequence of data items	Recommended to use for longer sequence of data items
More flexible to allow easy modification (addition or deletion) of data	Less flexible since addition or deletion has to be done element-wise
Consumes large memory for the addition of elements	Comparatively more compact in memory size while inserting elements
Can be printed entirely without using looping	A loop has to be defined to print or access the components
Syntax:
list = [1,”Hello”,[‘a’,’e’]]	Syntax:
import array
array_demo = array.array(‘i’, [1, 2, 3])
(array  as integer type)
20. Is python case sensitive?
Yes, Python is a case sensitive language. This means that Function and function both are different in pythons like SQL and Pascal.


21. What does [::-1] do?
[::-1] ,this is an example of slice notation and helps to reverse the sequence with the help of indexing.

[Start,stop,step count]
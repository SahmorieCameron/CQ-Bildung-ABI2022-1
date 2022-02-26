# ##### Object Orientated programming in python
#
# # Aims:
# # Gain an understanding of classes and their handling of attributes
# # Give an overview of the generation of graphical user interface via Tkinter
# # Buttons, entry fields etc. etc.
#
# # Classes and objects
#
# # attributes, methods and functions
#
# # generating our own Classes
#
# # Working with Tkinter
# # Widgets
# # Types of objects
# # Arrangement of Widgets
# # Events
#
# #### Classes
#
# # Int is a data type that contains a number with which you can do several things
# # A class is a user-defined data type which contains information and define the operations which can be done with it.
# # This is used to combine all code of one object (e.g. a list)
# # list is a class in python.
# # we create an object in this class when we define something as a list
#
#
#
# # Class: Human, Object: Sahmorie
#
# # Python is an object-orientated language.
# # This means that it can deal with classes and objects to model the real world.
#
# #For example, we could create a abstract class called Car.
#
# #Car would contain properties such as: brand, model, colour, fuel etc.
#
# #This could be written in Python thusly:
#
# #class Car:
#           # def __init__(self,brand,model,color,fuel):
#           #         self.brand=brand
#           #         self.model=model
#           #         self.color=color
#           #         self.fuel=fuel
#           #  def start(self):
#           #         pass
#           #  def halt(self):
#           #         pass
#           #  def drift(self):
#           #         pass
#           #  def speedup(self):
#           #         pass
#           #  def turn(self):
#           #         pass
#
# #### Python Objects
#
# # blackverna=Car('Hyundai','Verna','Black','Diesel')
#
# # the above script creates an object within the class Car.
#
# #As we have already defined class Car, we can use the class like a function to create these objects.
#
# # The strings within the brackets are the ATTRIBUTES of our object.
# # Attributes are characteristics of an object
# #These can be accessed within Python by calling object.attribute
# # in our car example blackverna.fuel par example
# # the output of us running blackverna.fuel will be 'Diesel'.
#
# #### Member-methods
#
# # A python method is like a Python function, but it is called on an object.
# # Usage:object.function()
# # or in our example blackverna.drift()
#
# #In our Car class, we have 5 methods already defined:
#
# #start()
# #halt()
# #drift()
# #speedup()
# #turn()
#
# #We left them empty using a pass statement because we hadn't yet decided what to do with them
#
#  #  def start(self):
#  #         pass
#  #  def halt(self):
#  #         pass
#  #  def drift(self):
#  #         pass
#  #  def speedup(self):
#  #         pass
#  #  def turn(self):
#  #         pass
#
# # These methods are a bit like functions:
#
#  # class Try:
#  #        def __init__(self):
#  #                pass
#  #        def printhello(self,name):
#  #                print(f"Hello, {name}")
#  #                return name
#  # obj=Try()
#  # obj.printhello('Ayushi')
#
# #Here we have created a class called Try.
# # We have created a method called printhello() like our drift()
# #our printhello method takes parameters, in this instance a name and prints Hello, Ayushi'Ayushi
#
#
#
# #### Constructor
#
# #Constructors are required to inititialize the class' ATTRIBUTES
# #In Python, it is our method __init__()
# # e.g.
# >>> class Animal:
#        def __init__(self,species,gender):
#                  self.species=species
#                  self.gender=gender
# >>> fluffy=Animal('Dog','Female')
# >>> fluffy.gender
#
# #Here, we used __init__ to initialize the attributes ‘species’ and ‘gender’.
# #However, you don’t need to define this function if you don’t need it in your code.
# # Init is a magic method, which is why it has double underscores before and after it.
#
# >>> class Try2:
#         def hello(self):
#             print("Hello")
# >>> obj2=Try2()
# >>> obj2.hello()
#
# #### Python Self Parameter
#
# # You would have noticed until now that we’ve been using the ‘self’ parameter with every method, even the __init__().
# # This tells the interpreter to deal with the current object.
#
#  # Let’s take another code to see how this works.
#
# >>> class Fruit:
#         def printstate(self,state):
#                print(f"The orange is {state}")
# >>> orange=Fruit()
# >>> orange.printstate("ripe")
#
# # Output
# # The orange is ripe
#
# # As you can see, the ‘self’ parameter told the method to operate on the current object,
# # that is, orange.
#
# Let’s take another example.
#
# >>> class Result:
#             def __init__(self,phy,chem,math):
#                           self.phy=phy
#                           self.chem=chem
#                           self.math=math
#             def printavg(self):
#                           print(f"Average={(self.phy+self.chem+self.math)/3}")
# >>> rollone=Result(86,95,85)
# >>> rollone.chem
#
# # Output
# # 95
#
# >>> rollone.printavg()
#
# # Output
# # Average=88.66666666666667
#
# #You can also assign values directly to the attributes, instead of relying on arguments.
#
# >>> class LED:
#         def __init__(self):
#                   self.lit=False
# >>> obj=LED()
# >>> obj.lit
#
# # Output
# # False
#
# #You can also assign values directly to the attributes, instead of relying on arguments.
#
# >>> class LED:
#         def __init__(self):
#                   self.lit=False
# >>> obj=LED()
# >>> obj.lit
#
# # Output
# # False
#
# Finally, we’d like to say that ‘self’ isn’t a keyword.
#
# You can use any name instead of it, provided that it isn’t a reserved keyword, and follows the rules for naming an identifier.
#
# >>> class Try3:
#          def __init__(thisobj,name):
#                    thisobj.name=name
# >>> obj1=Try3('Leo')
# >>> obj1.name
# Output
#
# ‘Leo’
#
# This was all about the Python Self Parameter
#
# Python Functions vs Method
# We think we’ve learned enough about methods by now to be able to compare them to functions.
#
# A function differs from a method in the following ways.
#
# While a method is called on an object, a function is generic.
# Since we call a method on an object, it is associated with it. Consequently, it is able to access and operate on the data within the class.
# A method may alter the state of the object; a function does not, when an object is passed as an argument to it. We have seen this in our tutorial on tuples.
# Python Magic Methods
# Another construct that Python provides us with is Python magic methods. Such a method is identified by double underscores before and after its name.
#
# Another name for a magic method is a dunder.
#
# A magic method is used to implement functionality that can’t be represented as a normal method.
#
# __init__() isn’t the only magic method in Python; we will read more about it in a future lesson.
#
# But for now, we’ll just name some of the magic methods:
#
# __add__ for +
#
# __sub__ for –
#
# __mul__ for *
#
# __and__ for &
#
# #The list, however, does not end here.
# #This was all about the Python Method.
#
#
# # Special Member-Method that is called when a new object of the class is generated
# # Has normally the same name as the class
# # Arguments of the constructor are used to define specific parameters during the creation of the object
#
# # e.g.
#
# #### Classes in Python
#
# # In python everything is a class
# # Encapesulation: The attributes of objects can only be accessed via Member-methods
#
# # Set()/Get()
# # With the help of dir(object) the Members-Methods of an object can be displayed.
#
# #### Magic functions
#
# # Can tell how the Object should behave in conjunction with:
# #    operators, print, casting functions, len, ...
#
# #### Own class: date
#
# # What kind of attributes will this class have?
# # What member-methods
# # Megic functions
# # Defining class
#
# # looks exactly like a function definition but with the keyword class instead of def
# # no arguments are given here and We can create classes without arguments.
#
# # Here it can be said if the new class should be inherited from another class.
# # e.g.
# #     class date():
# #         attributes
# #         member functions
# #
# # #we want to define a class Date that contains day, month and year.
# #
# # class date():
# #     day=0
# #     month=0
# #     year=0
#
# # To shorten the code the attributes are part of the Constructor
#
# # class():
# #     def__init__(self):
# #         self.day=0
# #         self.month=0
# #         self.year=0
# #
# # #Now we want to give a certain data, when a new object of type date is created so we have to give the construcor some arguments:
# # class date():
# #     def__init__(self,arg_day,arg_month,arg_year):
# #         self.day=arg.day
# #         self.month=arg_month
# #         self.year=arg_year
# #
# # def set_year(self, new_year):
# #     if new_year < 0:
# #         print("please enter a positive number")
# #     else:
# #         self.__year=new_year
# #         print("The year was changed")
#
# ####
#
# # class_date(): #class is date
# #     def__init__(self): # #this sets up magic function with (self):
# #         self.day=0
# #         self.month=0
# #         self.year=0
# #
# # #have created class date
# #
# # today=date() #object = today
# # yesterday = date()
# # print(today)
#
# # Private, protected and public attributes
#
# # Python differentiates between public, protected and private attributes of Classes
#
# # self.day =arg_day > public can be changed
# # self._day=arg_day > Protected, changes are not desireable
# # self.__day= arg_day > Private can't be changed, accessed etc
#
#
# #### Exercise 1 - Class Bike
#
# # Generate your own class called "Bike" that has the following five attributes:
#
# # brand: a string(private)
# # nr_sprockets: a positive whole number (private)
# # nr_pinion: a positive whole number (private)
# # sprocket:a positive whole number (protected)
# # _pinion: a positive whole number (protected)
#
# # All attributes should be given to the constructor of the class
# # if a new object is generated.
#
#
# class bike:
#     # Now we set up our contructor. This time we have five attributes, so we
#     # have to hand over five parameters to our contructor asside of the self
#     # keyword.
#     def __init__(
#         self, arg_Brand, arg_nr_sprockets, arg_nr_pinions, arg_sprocket, arg_pinion
#     ):
#     # To make sure I get the correct values, I cast each argument of the
#     # contructor to the respective datatype (string for brand and int for
#     # everything else).
#     #Please keep in mind that the first three attributes are private and the last two are protected.
#         self.__brand = str(arg_Brand)
#         self.__nr_sprockets = int(arg_nr_sprockets)
#         self.__nr_pinions = int(arg_nr_pinions)
#         self._sprocket = int(arg_sprocket)
#         self._pinion = int(arg_pinion)
#
#
# #### Exercise 2 - Class Bike 2
#
# # Expand the class from the first exercise by adding several methods to it.
# # One getter() for each attribute defined in the class(get_brand() and so on).
# # The methods up_sprocket(), down_sprocket(),up_pinion() accordingly but only if possible
# # That means if a bike has two sprockets and is alraedy in sprocket2 the unctino up_sprocket() will do nothing
#
# # Create a method print_state() that prints out the name of the bike the used sprocket and the used pinion
# # In the second exercise you should create five Getter() methods, one for
#     # each attribute. I will eyplain it on one example, because the syntax is
#     # the same vor each method, only the name of the corresponding method and
#     # the return value change. A getter() is a method that allows us to access
#     # the value of an otherwise not accessible attribute. You can name them how
#     # you want, but let's try to work with a standard syntax that is put
#     # together from the word get and the name of the attribute you want to
#     # return. The syntax is the simple function shown below. So you initiate the
#     # fucntion with the object itself and than simpl add the return command with
#     # the attribute you want to access. So the method below allows you to access
#     # the __brand attribute of your Bike class.
#     def get_brand(self):
#         return self.__brand
#
#     def get_sprocket(self):
#         return self._sprocket
#
#     def get_pinion(self):
#         return self._pinion
#
#     def get_NrSprocket(self):
#         return self.__nrsprockets
#
#     def get_NrPinion(self):
#         return self.__nrpinions
#
#     # After the definition of our five getter() methods, the exercise 2 asks us
#     # to define four methods called up_sprocket, up_pinion, down_sprocket and
#     # down_pinion to be able to change our current sprocket or pinion. We have
#     # to keep in mind that the attributes __nr_sprockets and __nr_pinions set
#     # the maximum number of sprockets and pinions that are available for us. So
#     # we have to make sure that we change our attributes _sprocket and _pinion
#     # not to values that are bigger than this maximum number here. So to set up
#     # our up_sprocket() method (and up_pinion() is pretty similiar again, so I
#     # will exclude it from explanations here), we have to define a function that
#     # again takes only itself as a parameter.
#     def up_sprocket(self):
#         # Now we check if we are currently at the biggest sprocket. If this is
#         # true we tell the user, that he can't change his sprocket.
#         if self._sprocket == self.__nrsprockets:
#             print("You already are in the biggest sprocket")
#         # If we cann change the sprocket, we simply add 1 to our _sprocket
#         # attribute and tell the user that his sprocket was changed.
#         else:
#             self._sprocket += 1
#             print("You're sprocket was increased.")
#
#     # The construction of up_pinion follows the same rules as shown for
#     # up_sprocket
#     def up_pinion(self):
#         if self._pinion == self.__nrpinions:
#             print("You already are in the biggest pinion")
#         else:
#             self._pinion += 1
#             print("You're pinion was increased.")
#
#     # For the down_sprocket() and down_pinion() methods we can use a similiar
#     # logic as we saw for our up methods. But this time we have to make sure
#     # that the sprocket or pinion don't become smaller than 1, so that we can
#     # make sure to stay at the lowest sprocket or pinion. So we define our
#     # method again as a simple function witht he object itself as parameter
#     def down_sprocket(self):
#         # Now we check if we aren't at the lowest sprocket currently. If the
#         # check below is true we tell the user that he can't change his sprocket
#         if self._sprocket == 1:
#             print("You already are in the lowest sprocket")
#         # If we can change the sprocket, we simply subtract 1 from our current
#         # sprocket and print out that the sprocket was changed.
#         else:
#             self._sprocket -= 1
#             print("You're sprocket was decreased.")
#
#     # The construction of down_pinion follows the same rules as shown for
#     # down_sprocket.
#     def down_pinion(self):
#         if self._pinion == 1:
#             print("You already are in the lowest pinion")
#         else:
#             self._pinion -= 1
#             print("You're pinion was decreased.")
#
#     # Last but not least the exercise asks us to create a method that displays
#     # The current status of our object. Since I created this method after our
#     # course its a simple combination of several prints. I will try to create
#     # a more complex one tomorrow.
#     def print_state(self):
#         print("")
#         print("The brand of your bike is", self.__brand)
#         print(
#             "You're currently at sprocket",
#             self._sprocket,
#             "of",
#             self.__nrsprockets,
#             "sprockets",
#         )
#         print(
#             "You're currently at pinion",
#             self._pinion,
#             "of",
#             self.__nrpinions,
#             "pinions",
#         )
#         print("")
#
#
# # Now we can create a new object of our Bike class as shown below. Remember to
# # hand over the five necessary parameters for the construction
# MyBike = Bike("Yamaha", 2, 10, 1, 1)
# # Afterwards we can use our newly created member methods as it is shown below.
# # If you have any questions about the usage of these methods, we can discuss
# # them during our course.
# MyBike.up_sprocket()
# MyBike.up_sprocket()
# MyBike.down_sprocket()
# MyBike.up_sprocket()
# MyBike.print_state()
# MyBike.down_pinion()
# MyBike.up_pinion()
# MyBike.up_pinion()
# MyBike.up_pinion()
# MyBike.print_state()
#
#
# #### Setter()
#
# # Private variables should only be accessible through setter methods:
# # class Motorrad:
# #     def __init__(self, marke, hubraum, ps):
# #         self.marke = marke
# #         self.__hubraum = hubraum
# #         self._ps = ps
# #
# #     def set_hubraum(self, kubrik):  # function to change value of function hubraum
# #         if kubrik <= 0:
# #             print("Error:Negativer Wert für den Hubraum!")
# #         else:
# #             self.__hubraum = kubrik
# #             print("Hubraum wurde geändert.")
# #
# #
# # #### Getter ()
# # # used to read out the values of our private attributes.
# # def get_hubraum(self):
# #     return(self.__hubraum)
# #
# # # Other simple methods:
# #
# # #You can also create methods to modify protected variables
# # #def add_ps(self)
# # #   self.__ps+=1
# #
# # def add_ps(self,addition):
#
#
# #### The function == in the class date
# #allows us to compare two objects of the same class.
#
# #### Tkinter
#
# #Toolkit interface
#
# #Each GUI should be it's own class
#
# Class App():
#     def member_function(self):
#         pass
#     def__init__(self):
#         pass
#
# App()
# #
#
# Class App():
#     def member_function(self):
#         self.some_attribut += 1
#     def__init__(self):
#         self.some_attribut=1
#
# App()
# print App.some_attribut
# App.member_function()
# print App

#### Widgets

# Definition: A widget is a graphical component on the screen
# (button, text label, drop down menu, scroll bar, image, etc...)
# GUIs are generated by combining different widgets and arranging them on the screen
# Default form of constructors in TKinter:
#    widget= <widgetname>(parent, attributes...) #parent = class for example

# Standard attributes

# background
# foreground
# height
# width
# state

# Attributes of Widgets in Tkinter

# Get values of widget attributes
#   Widget.cget(attribute)
#       Button1.cget("text")

# Set values of widget attribute:
#    Widget.config(attribut=word)
#       Button1.config(width =12 )

# Root

# The widget that contains nearly all other widgets (parent)
# Widgets generate a tree-like structure

# Hello WOrld
import tkinter as tk

#
#
# class hello1:  # Define Class
#     def __init__(self, arg_Text):
#         self.root = (
#             tk.Tk()
#         )  # Setting up the root, empty frame where we can put our other widgets
#         self.w = tk.Label(
#             self.root, text=arg_Text, height=30, width=40, font=20, fg="blue"
#         )
#         self.w.pack()
#         self.root.mainloop()  # used to open the GUI
#
#
# hello1("Hold the cold one like he hold a old gun.")
#
#
# class hello2:  # Define Class
#     def __init__(self, arg_Text):
#         self.root = (
#             tk.Tk()
#         )  # Setting up the root, empty frame where we can put our other widgets
#         self.w = tk.Label(
#             self.root, text=arg_Text, height=30, width=40, font=20, fg="red"
#         )
#         self.w.pack()
#         self.root.mainloop()  # used to open the GUI
#
#
# hello2("Like he hold the microphone and stole the show for fun.")
#
#
# class hello3:  # Define Class
#     def __init__(self):
#         self.root = (
#             tk.Tk()
#         )  # Setting up the root, empty frame where we can put our other widgets
#         self.w = tk.Label(
#             self.root,
#             text="Hold the cold one like he hold a old gun.",
#             background="red",
#             height=30,
#             width=40,
#             font=20,
#             fg="blue",
#         )
#         self.w2 = tk.Label(
#             self.root,
#             text="Like he hold the microphone and stole the show for fun",
#             background="blue",
#             height=30,
#             width=40,
#             font=20,
#             fg="red",
#         )
#         self.w.pack()
#         self.w2.pack()
#         self.root.mainloop()  # used to open the GUI
#
#
# hello3()

#### Button

#
# class hello3:  # Define Class
#     def __init__(self):
#         self.root = (
#             tk.Tk()
#         )  # Setting up the root, empty frame where we can put our other widgets
#         self.w = tk.Label(
#             self.root,
#             text="Hold the cold one like he hold a old gun.",
#             background="red",
#             height=30,
#             width=100,
#             font=10,
#             fg="blue",
#         )
#         self.w2 = tk.Label(
#             self.root,
#             text="Like he hold the microphone and stole the show for fun",
#             background="blue",
#             height=50,
#             width=100,
#             font=10,
#             fg="red",
#         )
#         self.w.pack(side="left")
#         self.w2.pack()
#         self.button1 = tk.Button(self.root, text="Click Me", command=self.root.destroy)
#         self.button2 = tk.Button(
#             self.root,
#             text="remove me",
#             command=lambda: print("Fly you fools"),
#             fg="red",
#         )
#         self.button1.pack()
#         self.button2.pack()
#         self.root.mainloop()  # used to open the GUI
#
#
# hello3()


# Inputs

# Widget for short inputs and outputs
# Saves his value in a specific variable

# Varvars

# special variables in Tktinter
# saves the values of Inputs

import tkinter as tk
from tkinter import ttk


# Creating a clickcounter
class clickcounter:
    def __init__(self):  # Constructor
        self.root = tk.Tk()
        self.count = 0
        self.root.title("click counter")
        # label
        self.w = tk.Label(self.root, text=self.count)
        # button
        self.button2 = tk.Button(
            self.root, text="Click Me", command=lambda: self.countup()
        )
        # stores the attributes in the class
        self.w.pack()
        self.button2.pack()

        self.root.mainloop()

    # Here is the function! Each time it is called, self.count increased by one-
    # New value of self.count is written in my label (text=self.count)
    # FUNCTIONS MUST NOT BE IN THE CONSTRUCTOR, WATCH THE TABS
    def countup(self):
        self.count += 1
        self.w.config(
            text=self.count
        )  # config used to change attributes of label or button etc.


clickcounter()

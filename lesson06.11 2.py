import requests
import inspect
import tkinter as tk




print(type(tk))
for method in dir(tk):
    print(method)

print(hasattr(tk, "append"))
print(hasattr(tk, "mainloop"))

print(inspect.isclass(tk))

name = "Oleg"
age = 12
list1 = []
dict = {}


print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.getmodule(requests))

print(type(requests))
print(type(name))
print(type(age))
print(type(list))
print(type(dict))

print("/n")
for method in dir(list):
    print(method)


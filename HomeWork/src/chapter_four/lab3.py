# Write a program that asks the user to enter an object’s mass, then calculates its weight.
# If the object weighs more than 500 newtons, display a message indicating that it is too heavy to be lifted; otherwise,
# display a message that it can be lifted.
# If the object weighs less than 100 newtons, display an additional message indicating that the object is quite light.

# weight = mass x 9.8

mass = float(input("Please enter in the objects mass: "))
weight = mass * 9.8

if weight > 500.0:
    print("This object is too heavy to be lifted.")
else:
    print("This object can be lifted.")

if weight < 100.0:
    print("The object is quite light.")

name = 'Jianyuan Bo'
age = 26
height = 179 # cm
height_in_inches = height * 0.3937
weight = 90 # kg
weight_in_pounds = weight * 2.2046
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.") 
# embeded variable inside a string by using special {} sequence 
# and then put the variable you want inside the {} characters.
# You also must start the string with the letter f for "format"
print(f"He's {height} cm tall.")
print(f"He's {weight} kg.")
print("Actually he is working on losing some weight.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on whether he brushed his teeth yesterday.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")



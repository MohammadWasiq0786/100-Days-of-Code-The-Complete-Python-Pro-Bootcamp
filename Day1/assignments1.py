"""
Printing Practice --- 1
Write a program that uses print statements to print the following recipe into the 
Output console. The text to print is already there, you just need to make it into code. 
Your code should print all five lines exactly the same as the example output below. 
Make sure that you don't change any of these existing text as everything, punctuation 
and casing all need to match!   

1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes. 
"""

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# ========================= OR ==========================

aa= """
1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
2. Knead the dough for 10 minutes.
3. Add 3g of Salt.
4. Leave to rise for 2 hours.
5. Bake at 200 degrees C for 30 minutes. 
"""
print(aa)

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n2. Knead the dough for 10 minutes.\n3. Add 3g of Salt.\n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes. ")

""""
Practice --- 2

# Fix the code below 👇

print(Notes from Day 1")
 print("The print statement is used to output strings")
print("Strings are strings of characters"
priint("String Concatenation is done with the + sign")
print(("New lines can be created with a \ and the letter n")
"""

# Fix the code below 👇

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

"""
Practice --- 3

Variables
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
Write 3 lines of code to switch the contents of the variables. 
You are not allowed to type the words "milk" or "juice". 
You are only allowed to use variables to solve this exercise.    
"""

glass1 = "milk"
glass2 = "juice"

temp= glass1
glass1=glass2
glass2= temp

print(glass1, glass2)
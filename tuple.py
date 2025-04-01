# Coding Exercise:
# 1. Create a Tuple:
#  Write a program that creates a tuple containing three
# elements: your name, your age, and your favorite color. Then print the tuple.
# tuple_1=('sam','30','blue')
# print(tuple_1)
# output:('sam', '30', 'blue')

# 2. Access Tuple Elements: Write a program that creates a tuple containing 
# the days of the week. Then, print the third element of the tuple.
# tuple_1=('mon','tues','wednes','thurs','fri','satur')
# print(tuple_1[2])
# output:wednes

# 3. Tuple Concatenation: Write a program that creates two tuples, onecontaining odd 
# numbers from 1 to 5 and another containing even numbers
# from 2 to 6. Concatenate these two tuples and print the result.
# tuple_1=(1,3,5)
# tuple_2=(2,4,6)
# result=tuple_1+tuple_2
# print(result)
# output:(1, 3, 5, 2, 4, 6)


# 4. Tuple Unpacking: Write a program that defines a tuple containing the
# dimensions of a rectangle (length and width). Then, unpack this tuple into 
#  two variables and calculate the area of the rectangle.
# tuple1=(15,10)
# length=(tuple1[0])
# width=(tuple1[1])
# result=length*width
# print(result)
# output:150

# 5. Check if an Element Exists: Write a program that checks if a given element
# exists in a tuple.
# tuple=(1,22,55,44,99,88)
# print(55 in tuple)


# 6. Write a Python program to generate a bill for a supermarket purchase. The
# program should store the items and their prices in a list of tuples. It should
# then iterate over this list to print out each item along with its price. Finally,
# calculate and print the total cost of all the items

# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# total=0
# print(f"Item     Price")
# print('-'*20)
# for item,price in items:
#     print(f"{item:<10} {price}")
#     total += price
# print('-'*20)
# print(f"Total      {total}")

#  Output:
# print(f"Item           Price")
# print('-'*20)

# for item,price in items:
#     print(f"{item:<15} {price}")
#     total += price

# print('-'*20)
# print(f"Total          {total}")

# output:
# Item     Price
# --------------------
# Apple      99
# Banana     99
# Milk       49
# --------------------
# Total      247

string= 'Interview'
new_str= string.replace('e','_',1)
print(new_str)
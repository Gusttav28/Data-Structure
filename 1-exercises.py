# Create and traversal 

# Write a function that creates an array of integers and prints each element using both a for-loop and a while-loop.

# Example: Input [1, 2, 3, 4, 5] → Output 1 2 3 4 5.

def create_array(*args):
    numberList = list(args)
    print(f"Principal list: {numberList}")
    insert_element(2, 10, numberList)
    
    
    print("With a for loop:")
    for i in numberList:
        print(i)
    
    print("With a while:")
    count = 0
    while count < len(numberList):
        print(numberList[count])
        count += 1
    
    
    return numberList

# Implement functions to insert a new element at a given index and to delete an element at a given index.
# Example: Insert 10 at index 2 in [1, 2, 3, 4] → [1, 2, 10, 3, 4].

def insert_element(listpossition, desireNumber, *args):
    print("Inserting a number at index two:")
    lisst = list(args)
    listTwo = list(lisst[0])
    listTwo.insert(listpossition, desireNumber)
    print(listTwo)
    delete_element(3, listTwo)
    
def delete_element(element_to_delete, *args):
    print("Deleting a number at index three: ")
    lisst = list(args)
    listTwo = list(lisst[0])
    print(element_to_delete)
    remove = listTwo.remove(element_to_delete)
    print(listTwo)
    reversingList(listTwo)
    max_min(listTwo)
    

# Reverse an Array
# Given an array, reverse it in place without using extra space.
# Example: [1, 2, 3, 4] → [4, 3, 2, 1].
    
def reversingList(*args):
    lisst = list(args)
    listTwo = list(lisst[0])
    listTwo.reverse()
    print(listTwo)
    

# Find Maximum and Minimum
# Write a function to find the largest and smallest elements in an array.

def max_min(*args):
    lisst = list(args)
    listTwo = list(lisst[0])
    maxx = max(listTwo)
    minn = min(listTwo)
    print(f"max: {maxx}")
    print(f"min: {minn}")



if __name__ == "__main__":
    create_array(1, 2, 3, 4, 5)
# intermidiate level ------------------------------------------------


# Rotate the array
# Rotate the elements of an array to the right by k steps.
# Example: [1, 2, 3, 4, 5, 6, 7], k=3 → [5, 6, 7, 1, 2, 3, 4].

def rotate_array(*args):
    num = list(args)
    k = num[3]
    for i in num[:k]:
        num.remove(i)
        print(f"list alredy eliminited {num}")
        print(f"numbers that were removed: {i}")
        num.append(i)
        print(f"the list again: {num}")


# Remove Duplicates
# Remove duplicate elements from a sorted array in place and return the new length.
# Example: [1, 1, 2, 2, 3, 4, 4] → [1, 2, 3, 4].

def removed_duplicate(*args):
    num_list = list(args)
    print(f"duplicate list: {num_list}")
    for index, item in enumerate(num_list):
        print(f'index: {index}, item: {item}')
        try: 
            if index == item:
                num_list.remove(item)
                print("sucessfully remove duplicate items")
        except:
            print("error")
            
    print(f"List without the duplicates: {num_list}")
        # for e in num_list2:
        #     print(f"this is e: {num_list2}")      

        #     if i in num_list2 and e in num_list:
        #         num_list2.remove(i)
        #         print(num_list2)



if __name__ == "__main__":
    # intermidiate level
    # rotate_array(1, 2, 3, 4, 5, 6, 7)
    removed_duplicate(1, 1, 2, 2, 3, 4, 4)
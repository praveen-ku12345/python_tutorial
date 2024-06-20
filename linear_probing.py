def hash_function_1(key, size):
    return key%size
def linear_probing(hash_table, key, size):
    index = hash_function_1(key, size)
    i=1
    while hash_table[index] is not None:
        index=(index+i)%size
        i+=1
    return index
def hash_function(hash_table,key,size):
    index=hash_function_1(key,size)
    if hash_table[index] is None:
        hash_table[index]=key
    else:
        index=linear_probing(hash_table,key,size)
        hash_table[index]=key
def main():
    size=int(input("Enter the size of the hash table: "))
    hash_table=[None] * size
    while True:
        key=int(input("Enter the value to insert or -1 to exit: "))
        if key==-1:
            break
        hash_function(hash_table,key,size)
    print(hash_table)
if __name__ == "__main__":
    main()
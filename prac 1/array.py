#Program to perform Creation, insertion, Deletion and searching operatons in 1D array
#Linear searching 
  
from operator import index

def find(arr, n, key):
    for i in range(n):
        if(arr[i]==key):
            return i
        return-1
    if __name__ =='__main__':
        arr=[10, 12, 15, 6,40]
        key = 40
        pos= find(arr, n, key)
        n == len(arr)
        if index != -1:
            print(" Element Found at "+ str(pos+1))
        else:
            print("element not found")

#Insertion 
def insert(arr1, element):
    arr1.append(element)
    if __name__== '__main__':
        arr1= [12, 16, 20, 40]
        key1 = 27
        print("Before Inserting: ")
        print(arr1)
        insert(arr1, key1)
        print("After insertion: ")
        print(arr1)

#Deletion 
if __name__=='__main__':
    arr2 = [ 10, 50, 30, 40, 20]
    key2 =30
    print("array before deletion: ")
    print(arr2)
    arr2.remove(key2)
    print(" Array after deletion: ")
    print(arr2)

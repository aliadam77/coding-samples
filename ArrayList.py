#arrayList (Dynamically Resizing Array)
#an array that resizes itself as needed while still providing O(1)

def arrayList_Merge(arrWords,arrMore):
    newArray = []               #initalize the new array
    newArray += arrWords        #adding the two arrays 
    newArray += arrMore
    return newArray
def main():
    arr1 = ["hello","world","hello"]
    arr2 = ["foo","Bar","bow"]
    final = arrayList_Merge(arr1,arr2)
    print(final)
main()


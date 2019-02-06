# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total = 0 
    dict1 = dict.fromkeys(ar,0)
    for i in ar:
        dict1[i] += 1
    for key in dict1:
        total += (dict1[key]//2) 
    return total
def main():
    ar = [10,20,10,10,30,50,10,20]
    n = 9
    result = sockMerchant(n,ar)
    print (result)
main()

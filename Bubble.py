a = list(map(int, input("Enter The array ").split()))
for j in range (0,len(a)):                  #the first loop to check the whole loop many times as its lenth
    for i in range(0,len(a)-j-1):           #the second loop to check the values inside the loop
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print ("The Sorted array is", a)
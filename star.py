# n = int(input("Number: "))

# for ind in range(1, n+1):
#     print(f"{ind}"* (n-ind), end="")
#     print("*"* (2*ind-1), end="")
#     print("")



#     '''
#     n==12


    
    
#     '''


num = int(input("Enter Number: "))


for i in range(1, num+1):
    if(i == 1 or i == num):
        print(" * "*num, end="")
    else:
        for ind in range(1, num+1):
            if(ind==num or ind == 1):
                print(" * ", end="")
            else:
                print("   ", end="")
    print("")
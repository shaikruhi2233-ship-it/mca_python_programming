
nums=[2,5,8,11,15]
for n in nums:
    print(n)
    print("loop completed")


    nums=[2,5,8,11,18]
    for n in nums:
        if n>10:
            break
        print(n)
        print("loop completed")


        value=int(input("enter breakpoint"))
        nums=[1,2,3,4,5,6,11,15,20,25]
        for n in nums:
            if value>n:
                print("loop broken")
                break
        else:
            print("loop completed")

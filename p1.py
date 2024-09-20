mark1=int(input("enter mark 1"))
mark2=int(input("enter mark 2"))
mark3=int(input("enter mark 3"))
if(mark1>mark2 and mark1>mark3):
    if(mark2>mark3):
        print("mark1 and mark2 is bigger")
        print("the avg of both is",(mark1+mark2)/2)
    else:
        print("mark1 and mark3 is bigger")
        print("the avg of both is",(mark1+mark3)/2)
elif (mark2>mark1 and mark2>mark3):
    if(mark1>mark3):
        print("mark2 and mark1 is bigger")
        print("the avg of both is",(mark2+mark1)/2)
    else:
        print("mark2 and mark3 is bigger")
        print("the avg of both is",(mark2+mark3)/2)
else:
    print("mark3 and mark2 is bigger")
    print("the avg of both is",(mark3+mark2)/2)

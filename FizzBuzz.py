num = int(input())
i=0
while(i<num):
    i=i+1
    if(i%3==0 | i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    else:
        if(i%5==0):
            
            print("Buzz")
        else:
            print(i)
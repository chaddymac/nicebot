my_list = range(1,101)

for i in my_list:
    if i%3==0 and i%5==0:
        print("Contraband")
    elif i %3 ==0:
        print("Contra")
    elif i %5==0:
        print("Band")
    
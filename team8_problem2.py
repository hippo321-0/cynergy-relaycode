a={"xiv":14 , "xx":20 ," ix": 9, "v":5, "xl":40, "x":10, "c":100 , "cd":400 , "m":1000,"d":500 ,"xc":90,"cm": 900, "md":1500, "xxxiv":34 }
def sum(rom1,rom2):
    num1=a[rom1]
    num2=a[rom2]
    result=num1+num2
    print(result)

ip1=input("Enter first roman number")
ip2=input("Enter second roman number")
sum(ip1,ip2)

#python program to find factorial of a number
num=int(input ("Enter the number :"))
fact=1
for i in range (1,num+1):
  fact=fact*i
print("Factorial of given number::",fact)
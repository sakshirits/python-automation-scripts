def collatz(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

def main():
   try:
     n=int(input("Enter the number:"))
     d=n

     while True:
         val = collatz(d)
         print(val)
         d = val

         if val == 1:
             break
   except ValueError:
       print(" You must enter an integer.")



main()



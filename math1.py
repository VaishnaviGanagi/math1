try:
  a=float(input("first number:"))
  b=float(input("second number:"))
  print(f"add:{a+b}")
  print(f"sub:{a-b}")
  print(f"mul:{a*b}")
  if b!=0:
     print(f"div:{a/b}")
  else:
    print("not divisible")
except ValueError:
  print("enter valid input")
                

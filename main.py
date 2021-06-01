print("Я, Іларія-Болгарія")
math = True
is_a_cool = False
is_b_cool = False

#name = input("а як тебе звуть?")
#print(f"Привіт гавнюк,  {name}")
while math:
   while not is_a_cool:
        try:
            a = float(input("введіть а=").replace(",","."))
            is_a_cool = True
        except:
            print("а має бути числом")


   while not is_b_cool:
        try:
            b = float(input("введіть b=").replace(",","."))
            is_b_cool = True
        except:
            print("b має бути числом")

   is_a_cool = False
   is_b_cool = False

   print(f"a-b={a-b}")
   print(f"a+b={a+b}")
   print(f"a*b={a*b}")
   try:
       print(f"a/b={round(a/b, 2)}")
   except:
       print("a/b= Ділити на нуль не можна")
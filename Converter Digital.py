import math as m

def ke_desimal(langsung):
    print("To Decimal Converter\n")
    base = int((input("input your base: ")))
    num = input("input your number: ")
    lst = []
    num_lst = []
    use_num = num[::-1]
    use_num = use_num.upper()
    n = 0
    if "." in use_num:
            x, y = use_num.split(".")
            n = len(x)
            use_num = use_num.replace(".","")
    for i in range(len(use_num)):
        if use_num[i].isdigit() == False:
            data_store = float(ord(use_num[i]) - 55)
        else:
            data_store = float(use_num[i])
        num_lst.append(data_store)
    for i in range(len(num_lst)):
        data = float(num_lst[i])*base**(i-n)
        lst.append(data)
    if langsung == False:
         print(sum(lst))
    else:
         return str(sum(lst))

def dari_desimal(langsung):
    if langsung is None:
         print("From Decimal Converter")
    num = input("input your base 10 number: ") if langsung is None else langsung
    base = int(input("input your destined base: "))
    num_lst = []
    if "." in num:
         num, fraction = num.split(".")
         fraction_lst = []
         fraction = float(fraction)*10**-(len(fraction))
         for i in range(0, 7):
              temp = fraction*base
              if m.floor(temp) > 9:
                   fraction_lst.append(chr(m.floor(temp)+55))
              else:
                   fraction_lst.append(m.floor(temp))
              temp-=m.floor(temp)
              if temp == 0:
                   break
              fraction = temp
    else:
         fraction_lst = None
    num = int(num)
    while True:
         temp = num//base
         rem = num - temp*base
         if rem > 9:
              rem = chr(rem+55)
         num_lst.append(rem)
         num//=base
         if num == 0:
              break
    num_lst.reverse()
    if fraction_lst is None:
         print("".join(map(str, num_lst)))
    else:
         print("".join(map(str, num_lst))+"."+"".join(map(str, fraction_lst)))

while True:
     print("choose one:")
     print("(1) Convert to Base-10")
     print("(2) Convert From Base-10")
     print("(3) From Any Base to Any Base")
     print("(4) Exit")
     choice = input("choose between (1/2/3): ")
     if choice == "1":
          ke_desimal(False)
     elif choice == "2":
          dari_desimal(None)
     elif choice == "3":
          dari_desimal(ke_desimal(True))
     elif choice == "4":
          break
     else:
          print("Input Tidak Valid")
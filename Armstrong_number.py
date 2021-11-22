list = []
sayi = input("Bir sayı giriniz: ")
uzunluk = len(sayi)
if sayi.isdigit() :
     for i in sayi :
 	    list.append(int(i) ** uzunluk)
     if sum(list) == int(sayi) :
            print(f'{sayi} is an Armstrong number')
     else :
            print(f'{sayi} is not an Armstrong number')
else :
     print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

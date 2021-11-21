num = input("Sayı gir: ")
bos =[]
for i in range(2, int(num)) :
  b = int(num) % i
  bos.append(b)
if 0 in bos :
  print(num + " sayısı asal bir sayı değildir.")
elif int(num) <= 1:
  print(num + " sayısı asal bir sayı değildir.")
else :
  print(num + " sayısı asal bir sayıdır.")

counter_pos = 0
counter_neg = 0
counter_zer = 0

for i in range(5):
    number = int(input("Ingresa un número: "))
    if number > 0:
        counter_pos += 1
    elif number == 0:
        counter_zer += 1
    else:
        counter_neg += 1

print("Positivos: ", counter_pos)
print("Negativos: ", counter_neg)
print("Ceros: ", counter_zer)

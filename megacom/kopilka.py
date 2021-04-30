wantedSum = int(input("Сколько вы хотите накопить? : "))
sum = 0
while wantedSum > sum:
    vznos = int(input("Взнос : "))
    sum+=vznos
    if sum > wantedSum:
        print(f"Поздравляю! Вы накопили {sum} сомов!")
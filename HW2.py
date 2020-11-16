klubA = input("Klub A : ")
klubB = input("Klub B : ")
pemenang = []

n = True
i = 1
while n :
    print(f"Pertandingan {i} : ", end=" ")
    skor = input().split()
    
    if int(skor[0]) < 0 or int(skor[1]) < 0 :
        n = False
    else :
        if int(skor[0]) > int(skor[1]):
            pemenang.append(klubA)
        elif int(skor[0]) < int(skor[1]):
            pemenang.append(klubB)
        else :
            pemenang.append("Draw")

    i += 1

for i,n in enumerate(pemenang):
    print(f"Hasil {i+1} : {n}")

print("Pertandingan Selesai")

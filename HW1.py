arrBerat = []
bMin = 0.0
bMax = 0.0

def hitungMinMax(arrBerat):
    global bMin, bMax
    bMin = min(arrBerat)
    bMax = max(arrBerat)
    
def rerata(arrBerat):
    total = sum(arrBerat)
    return round(total/len(arrBerat),2)

print('Masukkan Banyak Data Berat Balita: ', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita ke-{i+1} :', end=' ')
    berat = float(input())
    arrBerat.append(berat)

hitungMinMax(arrBerat)
print("berat min :", bMin)
print("berat max :", bMax)
print("rerata berat :", rerata(arrBerat))

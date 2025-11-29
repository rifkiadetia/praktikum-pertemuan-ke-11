print("NAMA  : RIFKI ADE TIA")
print("NIM   : 312510334")
print("KELAS : TI.25.C5")
print()
import math

# Fungsi lambda
a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))   

# ==== Contoh Penggunaan ====

print("=== Penggunaan Fungsi a(x) ===")
print("a(5) =", a(5))             

print("\n=== Penggunaan Fungsi b(x, y) ===")
print("b(3, 4) =", b(3, 4))        

print("\n=== Penggunaan Fungsi c(*args) ===")
print("c(2, 4, 6) =", c(2, 4, 6))  

print("\n=== Penggunaan Fungsi d(s) ===")
print("d('halo') =", d('halo'))    
print("d('aaaaabbbccc') =", d('aaaaabbbccc'))  
# 📐 **Numerical Integration Calculator (Python)**

Proyek ini merupakan implementasi **integrasi numerik** dalam bahasa **Python**, menggunakan tiga metode populer:

1. **Rectangular Rule (Riemann Sum)**
2. **Trapezoidal Rule**
3. **Simpson’s Rule**

Aplikasi ini menghitung pendekatan nilai integral dari fungsi tertentu pada interval ([a, b]) dengan jumlah pembagian (n) titik.

---

## 🧠 **Deskripsi Program**

Fungsi utama:

```python
my_num_calc(f, a, b, n, option)
```

📌 **Parameter:**

| Parameter | Tipe     | Deskripsi                                           |
| --------- | -------- | --------------------------------------------------- |
| `f`       | function | Fungsi yang akan diintegralkan                      |
| `a`       | float    | Batas bawah integral                                |
| `b`       | float    | Batas atas integral                                 |
| `n`       | int      | Jumlah titik pembagi (harus ganjil untuk Simpson)   |
| `option`  | str      | Metode integrasi: `"rect"`, `"trap"`, atau `"simp"` |

📌 **Output:**
Mengembalikan nilai pendekatan integral fungsi `f` pada interval ([a, b]).

---

## ⚙️ **Algoritma yang Digunakan**

### 1️⃣ **Rectangular Rule (Riemann Sum)**

[
I = \sum_{i=1}^{n-1} f(x_i) \cdot h
]

### 2️⃣ **Trapezoidal Rule**

[
I = \frac{h}{2} \left[f(x_0) + 2 \sum_{i=1}^{n-2} f(x_i) + f(x_{n-1})\right]
]

### 3️⃣ **Simpson’s Rule**

[
I = \frac{h}{3} \left[f(x_0) + 4\sum_{i=1,3,5}^{n-2} f(x_i) + 2\sum_{i=2,4,6}^{n-3} f(x_i) + f(x_{n-1})\right]
]

📌 *Catatan:* Untuk metode Simpson, jumlah segmen ((n-1)) **harus genap**.

---

## 🧩 **Struktur Program**

| Fungsi          | Deskripsi                                                          |
| --------------- | ------------------------------------------------------------------ |
| `my_num_calc()` | Fungsi utama untuk menghitung integral numerik dengan tiga metode. |
| `f1`            | Contoh fungsi ( f(x) = x^2 ).                                      |
| `f2`            | Contoh fungsi ( f(x) = e^{x^2} ).                                  |
| `np.linspace()` | Digunakan untuk membagi interval menjadi titik-titik sama jarak.   |
| `h`             | Lebar tiap interval, dihitung sebagai ( h = \frac{b - a}{n - 1} ). |

---

## 🧪 **Contoh Penggunaan**

```python
import numpy as np

# Fungsi pertama: f(x) = x^2
f1 = lambda x: x**2
print(my_num_calc(f1, 0, 1, 3, "rect"))  # Metode Rectangular
print(my_num_calc(f1, 0, 1, 3, "trap"))  # Metode Trapezoid
print(my_num_calc(f1, 0, 1, 3, "simp"))  # Metode Simpson

# Fungsi kedua: f(x) = e^(x^2)
f2 = lambda x: np.exp(x**2)
print(my_num_calc(f2, -1, 1, 101, "simp"))     # n kecil
print(my_num_calc(f2, -1, 1, 10001, "simp"))   # n sedang
print(my_num_calc(f2, -1, 1, 100001, "simp"))  # n besar
```

---

## 📊 **Contoh Output**

```
0.3333333333333333
0.3333333333333333
0.3333333333333333
3.524490456868992
3.524490456868989
3.5244904568689884
```

---

## 🎯 **Tujuan Proyek**

* Memahami konsep **integrasi numerik** melalui pemrograman.
* Menunjukkan perbedaan ketelitian antara metode **Rectangular**, **Trapezoid**, dan **Simpson**.
* Membiasakan penggunaan **NumPy** dalam perhitungan ilmiah.

---

Apakah kamu mau saya ubah ini jadi file `README.md` yang bisa langsung kamu upload ke GitHub (biar format markdown-nya sempurna)?

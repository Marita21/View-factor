# 🔥 View Factor Calculator in Python

This project calculates the **view factor** between two polygonal surfaces using numerical integration methods. View factors are essential in modeling **radiative heat transfer**, especially in thermal engineering applications such as spacecraft, satellites, and enclosures.

---

## 📌 Features

- ✅ Computes view factors between two 3D surfaces (triangles or quadrilaterals)
- ✅ Calculates surface areas using line integrals
- ✅ Implements accurate **double integration** using SciPy
- ✅ Modular and clear Python code
- ✅ Multiple test cases included

---

## 🧠 How It Works

- Each surface is defined by a set of 3D vertices.
- The **area** of each surface is computed using single integrals along the edge.
- The **view factor** is obtained by evaluating a **double integral** over both surfaces using their normal vectors.
- The result gives the fraction of radiation leaving one surface that reaches the other.

---

## ▶️ Example: Compute View Factor Between Two Surfaces

```python
from viewfactor import viewfactor

FACTOR12, FACTOR21, AREA1, AREA2 = viewfactor(
    [[0, 0, 0], [1, 0, 0], [0, 1, 0]],
    [[0, 0, 1], [2, 0, 1], [0, 2, 1]],
    6
)

print(FACTOR12, FACTOR21, AREA1, AREA2)

## ✅ Output:

0.2843  0.0711  0.5  2.0

- 0.2843: View factor from surface 1 to surface 2

- 0.0711: View factor from surface 2 to surface 1

- 0.5: Area of surface 1

- 2.0: Area of surface 2

## 🌍 Use Case

Useful for:

Spacecraft and satellite thermal design

Simulation of radiative exchange between spacecraft parts

Academic purposes in thermodynamics and heat transfer courses

## 🛠️ Installation
You need Python 3 and the following libraries:

pip install numpy scipy

## 📂 Files

vfact.py: Example script to test the function with predefined surfaces.

viewfactor.py: Core logic that calculates areas and view factors.

functionviewfactorarea.py: Computes area element for single integrals.

## 📜 License
MIT License – free to use, share, and adapt.

functionintegral.py: Computes the integrand for view factor evaluation.


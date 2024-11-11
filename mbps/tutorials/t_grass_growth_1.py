# -*- coding: utf-8 -*-
"""
FTE34806 - Modelling of Biobased Production Systems
MSc Biosystems Engineering, WUR
Tutorial: Grass growth model analysis.
1. Light intensity over leaves.
"""
import numpy as np
import matplotlib.pyplot as plt

### 1. Light intensity over leaves
def f_Il(k, m, l, I0=100):
    return I0 * (k / (1 - m)) * np.exp(-k * l)

# Define an array with sensible values of leaf area index (l)
l = np.linspace(1, 5, 100)

# Light Intensity vs. Leaf Area Index with varying k
Il_k1 = f_Il(0.5, 0.1, l)
Il_k2 = f_Il(1, 0.1, l)
Il_k3 = f_Il(1.5, 0.1, l)

# Light Intensity vs. Leaf Area Index with varying m
Il_m1 = f_Il(1, 0.1, l)
Il_m2 = f_Il(1, 0.2, l)
Il_m3 = f_Il(1, 0.3, l)

# Light Intensity vs. Leaf Area Index with varying I0
Il_I01 = f_Il(1, 0.1, l, 50)
Il_I02 = f_Il(1, 0.1, l, 100)
Il_I03 = f_Il(1, 0.1, l, 150)

plt.style.use('ggplot')

fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# 1) Il vs. l, with three test values for k
axs[0].plot(l, Il_k1, label='k = 0.5', linestyle='-', color='blue')
axs[0].plot(l, Il_k2, label='k = 1', linestyle='--', color='green')
axs[0].plot(l, Il_k3, label='k = 1.5', linestyle='-.', color='red')
axs[0].set_xlabel('Leaf Area Index')
axs[0].set_ylabel('Light Intensity over Leaves')
axs[0].set_title('Light Intensity over Leaves vs. Leaf Area Index (varying k)')
axs[0].legend()
axs[0].grid(True)

# 2) Il vs. l, with three test values for m
axs[1].plot(l, Il_m1, label='m = 0.1', linestyle='-', color='blue')
axs[1].plot(l, Il_m2, label='m = 0.2', linestyle='--', color='green')
axs[1].plot(l, Il_m3, label='m = 0.3', linestyle='-.', color='red')
axs[1].set_xlabel('Leaf Area Index')
axs[1].set_ylabel('Light Intensity over Leaves')
axs[1].set_title('Light Intensity over Leaves vs. Leaf Area Index (varying m)')
axs[1].legend()
axs[1].grid(True)

# 3) Il vs. l, with three test values for I0
axs[2].plot(l, Il_I01, label='I0 = 50', linestyle='-', color='blue')
axs[2].plot(l, Il_I02, label='I0 = 100', linestyle='--', color='green')
axs[2].plot(l, Il_I03, label='I0 = 150', linestyle='-.', color='red')
axs[2].set_xlabel('Leaf Area Index')
axs[2].set_ylabel('Light Intensity over Leaves')
axs[2].set_title('Light Intensity over Leaves vs. Leaf Area Index (varying I0)')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig('data/grass_growth_analysis.png')
plt.show()

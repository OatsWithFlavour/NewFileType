import matplotlib.pyplot as plt
import numpy as np
import math as m
from armor import Armor


armor = Armor(100)
"""
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()"""


steel = {
    "with_shield": 96,
    "no_shield": 72,
    "shield": 24
}

print(armor.armor_value(steel["shield"], steel["no_shield"]))


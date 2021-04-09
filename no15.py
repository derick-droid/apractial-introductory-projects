# Write a program that prints out the sine and cosine of the angles ranging from 0 to 345 ◦ in
# 15 ◦ increments.
import math
for i in range(0, 346, 15):
    # converting the i value into degrees first
    deg = math.radians(i)
    # converting degrees to sine
    sine = math.sin(deg)
    # converting degrees to cosine
    cosine = math.cos(deg)

    print(i,"---",  "sine = ", round(sine, 4), "cosine = ", round(cosine, 4))
    

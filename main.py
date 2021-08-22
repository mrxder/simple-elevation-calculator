import math

print("Start")
print("start length:")
km_a = float(input())
print("start height:")
hm_a = float(input())

print("")

print("Target")
print("target length:")
km_b = float(input())
print("target height:")
hm_b = float(input())


distance = abs(km_a - km_b)
height = abs(hm_a - hm_b)

run = math.sqrt((math.pow(distance,2)) - (math.pow(height,2)))


percentage = (height / run) * 100

print("")
print("Elevation")
print(str(percentage) + "%")


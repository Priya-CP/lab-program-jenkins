
import sys

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

intrest = (principal * rate * time) / 100

print("simple intrest:", intrest)

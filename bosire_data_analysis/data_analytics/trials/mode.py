import scipy.stats as stats
import numpy as np

arr =[1,233,4,53,4,22,3,23,2,4]

ModeResult = stats.mode(arr)
mode = ModeResult.mode
count = ModeResult.count

print(f"Count = {count}")
print(f"Mode = {mode}")
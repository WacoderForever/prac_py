
def binary_sq(n,precision=0.00000001):
    if(n<0):
        print("Cannot find square root of a negative number")
    
    high = n
    low = 0

    while (high - low) > precision:
        mid = (low + high)/2
        mid_squared = mid * mid
        if(mid_squared==n):
            return mid
        if(mid_squared < n):
            low = mid
        else:
            high = mid
    
    return (low + high)/2

print(f"25: {binary_sq(25)}\n")
print(f"4: {binary_sq(4)}\n")
print(f"17: {binary_sq(17)}\n")
print(f"20: {binary_sq(20)}\n")
print(f"100: {binary_sq(100)}\n")
print(f"250: {binary_sq(250)}\n")
print(f"54: {binary_sq(54)}\n")
print(f"2: {binary_sq(2)}\n")
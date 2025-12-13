import matplotlib.pyplot as plt

xs = list(range(0, 11))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Method 1: Direct computation (proper alignment)
ys_squared = [i*i for i in xs]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
ys_twice = [2*i for i in xs]    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

plt.figure(figsize=(10, 6))
plt.plot(xs, ys_squared, 'b-o', label='y = x²', linewidth=2, markersize=8)
plt.plot(xs, ys_twice, 'r--s', label='y = 2x', linewidth=2, markersize=8)

plt.xlabel('x values (0-10)')
plt.ylabel('Function Values')
plt.title('Comparison: x² vs 2x')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(xs)
plt.show()
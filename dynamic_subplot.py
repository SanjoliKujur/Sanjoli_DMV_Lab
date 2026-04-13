import matplotlib.pyplot as plt

n = int(input("Enter number of subplots: "))

for i in range(1, n + 1):
    plt.subplot(1, n, i)
    
    x = []
    y = []
    m = int(input(f"Enter number of points for Plot {i}: "))
    
    for j in range(m):
        x_val = int(input("Enter x value: "))
        y_val = int(input("Enter y value: "))
        x.append(x_val)
        y.append(y_val)
    
    plt.plot(x, y)
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.title(f"PLOT {i}")

plt.tight_layout()
plt.show()
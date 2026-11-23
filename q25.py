import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [45000, 52000, 48000, 61000, 58000, 65000, 62000, 70000, 68000, 75000, 72000, 80000]

max_idx = sales.index(max(sales))
min_idx = sales.index(min(sales))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(months, sales, marker="o", color="b", linestyle="-")
plt.title("Monthly Sales Revenue (Line Chart)")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)

plt.subplot(1, 2, 2)
colors = ["skyblue" if i not in (max_idx, min_idx) else ("green" if i == max_idx else "red") for i in range(len(sales))]
plt.bar(months, sales, color=colors)
plt.title("Monthly Sales Revenue (Bar Chart)")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

plt.tight_layout()
plt.show()

print(f"Highest Sales: {months[max_idx]} with ₹{sales[max_idx]}")
print(f"Lowest Sales: {months[min_idx]} with ₹{sales[min_idx]}")
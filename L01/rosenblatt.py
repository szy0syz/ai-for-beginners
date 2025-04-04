import dataset
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)
print(xs)
print(ys)

#config
plt.title("Size-Toxicity Function", fontsize = 12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

plt.scatter(xs,ys)

w = 0.5

for i in range(100):
  for i in range(100):
    x = xs[i]
    y = ys[i]
    y_pred = w * x
    e = y - y_pred
    alpha = 0.05
    w = w + e * x * alpha

y_pred = w * xs

print(y_pred)

plt.plot(xs, y_pred)

plt.show()
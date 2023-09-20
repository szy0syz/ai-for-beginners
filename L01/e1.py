import dataset
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(5)
print(xs)
print(ys)

#config
plt.title("Size-Toxicity Function", fontsize = 12)
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

plt.scatter(xs,ys)
plt.show()
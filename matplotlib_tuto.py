import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# epochs = [1,2,3,4,5]
# loss = [0.9, 0.7, 0.5, 0.4, 0.3]

# plt.plot(epochs, loss)
# plt.xlabel("Epochs")
# plt.ylabel("Loss")
# plt.title("Training Loss Curve")
# plt.show()

# train_loss = [0.9,0.7,0.5,0.4,0.3]
# val_loss   = [1.0,0.8,0.6,0.6,0.7]

# plt.plot(train_loss, label="Train Loss")
# plt.plot(val_loss, label="Validation Loss")
# plt.legend()
# plt.show()

# df = pd.read_csv('students.csv')
# plt.scatter(df["Age"], df["Marks"])
# plt.xlabel("Age")
# plt.ylabel("Marks")
# plt.show()
# plt.figure(figsize=(4,5))
# plt.grid()
# plt.hist(df["Age"],bins=40)

# # plt.xlabel("Age")
# # plt.ylabel("Frequency")
# plt.show()

x = np.array([1,2,3,4,5])
y = np.array([5,8,5,9,10])

plt.subplot(2,1,1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([11, 20, 30, 40])

plt.subplot(2,1,1)

plt.plot(x,y)
plt.show()
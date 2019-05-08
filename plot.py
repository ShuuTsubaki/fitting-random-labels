import numpy as np
import pylab as plt

f = open("cifar10_parti.txt","r")
train_loss = []
test_loss = []
train_accuracy =[]
test_accuracy = []
# print(f.readline().strip().translate({ord(i): None for i in ','}).split(" "))
for line in f.readlines():
    line = line.strip().translate({ord(i): None for i in ','}).split(" ")
    test_loss.append(float(line[8]))
    train_loss.append(float(line[10]))
    train_accuracy.append(line[3])
    test_accuracy.append(line[5])
print(test_loss)
print(train_loss)
print(len(test_loss))
print(len(train_loss))
# plt.subplot(121)
# train_line = plt.plot(range(80), train_accuracy, label="Training")
# test_line = plt.plot(range(80), test_accuracy, label="Testing")
# plt.axis([0, 80, 0, 100])
# plt.title('Dataset')
# plt.xlabel('Iteration')
# plt.ylabel('Accuracy')
# plt.legend()

plt.subplot(122)
train_line = plt.plot(range(0, 81), train_loss, label="Training")
test_line = plt.plot(range(0, 81), test_loss, label="Testing")
plt.axis([0, 80, 0.0, 4.0])
plt.title('Dataset')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.legend()
plt.show()


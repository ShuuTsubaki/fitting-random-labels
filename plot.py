import numpy as np
import pylab as plt
cifar10_opt = ["cifar10_0.txt", 'cifar10_05.txt', 'cifar10_1.txt']
cifar100_opt = ["cifar100_0.txt", 'cifar100_05.txt', 'cifar100_1.txt']
train_loss = [[], [], []]
test_loss = [[], [], []]
train_accuracy = [[],[],[]]
test_accuracy = [[],[],[]]

for i in range(3):
    f = open(cifar100_opt[i],"r") # cifar10_opt can be replace
    for line in f.readlines():
        line_array = list(filter(None, line.strip().translate({ord(i): None for i in ','}).split(" ")))
        print(line_array)
        train_accuracy[i].append(float(line_array[2]))
        test_accuracy[i].append(float(line_array[4]))
        train_loss[i].append(float(line_array[6]))
        test_loss[i].append(float(line_array[8]))
    f.close()
plt.figure(1)
test_line1 = plt.plot(range(300), train_loss[0], label="true label")
test_line2 = plt.plot(range(300), train_loss[1], label="partially corrupted labels")
test_line3 = plt.plot(range(300), train_loss[2], label="random labels")
plt.axis([0, 300, 0, 4.0]) # can be replace by plt.axis([0, 300, 0, 1.5])
plt.title('Learning Curves of {} Dataset'.format("Wide Resnet on CIFAR100")) # can be replace by CIFAR10
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.legend()
plt.show()
# plt.subplot(122)
plt.figure(2)
test_line1 = plt.plot(range(300), test_loss[0], label="true label")
test_line2 = plt.plot(range(300), test_loss[1], label="partially corrupted labels")
test_line3 = plt.plot(range(300), test_loss[2], label="random labels")
plt.axis([0, 300, 0, 4.0])  # can be replace by plt.axis([0, 300, 0, 1.5])
plt.title('Generalization Error Growth of {} Dataset'.format("Wide Resnet on CIFAR100"))
plt.xlabel('Epoch')
plt.ylabel('Testing Error')
plt.legend()
plt.show()




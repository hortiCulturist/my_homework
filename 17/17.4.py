#################################################################################################
#Задача 1

import random
summ = 0
original_prices = [random.randint(-50, 50)]

new_prices = original_prices[:]

for i in range(len(new_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

summ = sum(original_prices) - sum(new_prices)
print(f"Мы потеряли: {abs(summ)}")

#################################################################################################
#Задача 2

nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

nums1 = nums[:]
nums2 = nums[:]
nums3 = nums[:]
nums4 = nums[:]
nums5 = nums[:]
nums6 = nums[:]

print(nums1[:5])
print(nums2[:8])
print(nums3[::2])
print(nums4[1:10:2])
print(nums5[::-1])
print(nums6[::-2])

#################################################################################################
#Задача 3

import random

N = [random.randint(1, 20) for _ in range(20)]
print('Старый список:', N)

A = random.randint(1, 20)
print('Ваше А:', A)

B = random.randint(1, 20)
print('Ваше B:', B)
if A < B:
    print('Новый срезанный в диапазоне от A до B список:', N[:A] + N[B + 1:])


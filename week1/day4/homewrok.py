# Zadání:
# 1) druhy_nejvetsi([4, 9, 2, 9, 7]) vrátí 7 (ne 9 — druhá největší různá hodnota)
# 2) bez_duplicit([1,2,1,3,2]) vrátí [1,2,3] a zachová pořadí
# 3) rozdel([1,2,3,4,5], 2) vrátí [[1,2],[3,4],[5]]

numbers = [4, 9, 2, 9, 7]
new_numbers = []
for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)

new_numbers.sort()
print(new_numbers[-2])  # Vrací druhou nejvyšší různou hodnotu.

nums = [1,2,1,3,2]
new_nums = []
for num in nums:
    if num not in new_nums:
        new_nums.append(num)

print(new_nums)

lst = [1,2,3,4,5]
for i in range(0, len(lst), 2):
    print(lst[i:i+2])

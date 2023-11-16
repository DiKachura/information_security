class GaloisField:
    def __init__(self, poly):
        self.poly = poly

    def add(self, a, b):
        return a ^ b

    def multiply(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            a <<= 1
            if a & 8:
                a ^= self.poly
            b >>= 1
        return result

    def power(self, a, n):
        result = 1
        while n > 0:
            if n & 1:
                result = self.multiply(result, a)
            a = self.multiply(a, a)
            n >>= 1
        return result

    def inverse(self, a):
        if a == 0:
            raise ZeroDivisionError("Cannot compute inverse of 0")
        return self.power(a, 6)

# Заданные элементы поля Галуа
alpha = 2  # α

# Заданные полиномы
poly = 11  # α^3 + α + 1

gf = GaloisField(poly)

# Задача 1: Найдите произведение элементов a и b
a = gf.add(gf.power(alpha, 2), gf.add(alpha, 1))
b = gf.add(gf.power(alpha, 2), alpha)
product = gf.multiply(a, b)
print("1. Произведение элементов a и b:", product)

# Задача 2: Вычислите результат возведения элемента α в степень 5
result_power = gf.power(alpha, 5)
print("2. Результат возведения элемента α в степень 5:", result_power)

# Задача 3: Найдите обратный элемент к элементу α^2 + 1
element_inverse = gf.inverse(gf.add(gf.power(alpha, 2), 1))
print("3. Обратный элемент к элементу α^2 + 1:", element_inverse)

# Задача 4: Проведите операцию сложения элементов α^2 + α и α^2 + 1
sum_result = gf.add(gf.add(gf.power(alpha, 2), alpha), gf.add(gf.power(alpha, 2), 1))
print("4. Результат сложения элементов α^2 + α и α^2 + 1:", sum_result)

# Задача 5: Вычислите результат умножения элементов α^3 + α^2 и α^2 + 1
multiply_result = gf.multiply(gf.add(gf.power(alpha, 3), gf.power(alpha, 2)), gf.add(gf.power(alpha, 2), 1))
print("5. Результат умножения элементов α^3 + α^2 и α^2 + 1:", multiply_result)

# Задача 6: Найдите обратный элемент к элементу α^2 + α + 1
element_inverse = gf.inverse(gf.add(gf.add(gf.power(alpha, 2), alpha), 1))
print("6. Обратный элемент к элементу α^2 + α + 1:", element_inverse)

# Задача 7: Проведите операцию вычитания элементов α^3 + α и α^2 + 1
subtraction_result = gf.add(gf.add(gf.power(alpha, 3), alpha), gf.add(gf.power(alpha, 2), 1))
print("7. Результат вычитания элементов α^3 + α и α^2 + 1:", subtraction_result)

# Задача 8: Вычислите результат возведения элемента α в степень 7
result_power = gf.power(alpha, 7)
print("8. Результат возведения элемента α в степень 7:", result_power)

# Задача 9: Найдите произведение элементов α^3 + α и α^2 + 1
a = gf.add(gf.power(alpha, 3), alpha)
b = gf.add(gf.power(alpha, 2), 1)
product = gf.multiply(a, b)
print("9. Произведение элементов α^3 + α и α^2 + 1:", product)

# Задача 10: Найдите обратный элемент к элементу α^3 + α
element_inverse = gf.inverse(gf.add(gf.power(alpha, 3), alpha))
print("10. Обратный элемент к элементу α^3 + α:", element_inverse)
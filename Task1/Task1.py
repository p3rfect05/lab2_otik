import collections
import math
from dataclasses import field


# Функция для расчета информации в символе
def calculate_information(probability):
    if probability == 0:
        return 0
    return -math.log2(probability)

# Открываем файл для анализа (замените "file.txt" на имя вашего файла)
file_path = "file.txt"
with open(file_path, 'rb') as file:
    file_content = file.read()

# Рассчитываем длину файла в байтах
file_length = len(file_content)

# Считаем частоту вхождения каждого байта
byte_frequencies = collections.Counter(file_content)

# Рассчитываем вероятность и информацию для каждого байта
byte_probabilities = {byte: freq / file_length for byte, freq in byte_frequencies.items()}
byte_information = {byte: calculate_information(prob) for byte, prob in byte_probabilities.items()}

# Сортируем таблицу характеристик символов по алфавиту и по убыванию частоты
sorted_byte_probabilities = sorted(byte_probabilities.items(), key=lambda x: x[0])
sorted_byte_probabilities_by_freq = sorted(byte_probabilities.items(), key=lambda x: x[1], reverse=True)

# Рассчитываем суммарное количество информации в файле
total_information = sum(freq * byte_information[byte] for byte, freq in byte_frequencies.items())

# Выводим результаты
#print(f"Длина файла в байтах: {file_length}")
#print("Таблица характеристик символов по алфавиту:")
#for byte, prob in sorted_byte_probabilities:
   # print(f"Символ: {byte}, Вероятность: {prob:.6f}, Информация: {byte_information[byte]:.6f}")
#print("\nТаблица характеристик символов по убыванию частоты:")
#for byte, prob in sorted_byte_probabilities_by_freq:
  #  print(f"Символ: {byte}, Вероятность: {prob:.6f}, Информация: {byte_information[byte]:.6f}")
#print(f"\nСуммарное количество информации в файле: {total_information * 8:.6f} бит")
#print(f"Суммарное количество информации в файле: {total_information:.6f} байт")


# пункт а

file_length_bits = len(file_content) * 8
print("Длина файла Q в битах =", file_length_bits)

Ibp_bits = total_information
print(f"Iбп(Q) [бит] = {Ibp_bits:.2f}")
print("{Iбп(Q) [бит]} = ", f"{Ibp_bits - int(Ibp_bits):.2e}")

# пункт б

file_length_octets = len(file_content)
print("Длина файла Q в октетах =", file_length_octets)

Ibp_octets = total_information / 8
print(f"Iбп(Q) [октетов] = {Ibp_octets:.2f}")

E = math.ceil(Ibp_octets)
print("E = ceil(Iбп(Q) [октетов]) =", E)

G64 = E + 256 * 8

print("G64 =", G64)

G8 = E + 256 * 1

print("G8 =", G8)


print("Таблица характеристик символов по алфавиту:")
for byte, prob in sorted_byte_probabilities:
    print(f"Символ: {byte}, Ненормированная частота: {byte_frequencies[byte]}, Оценка вероятности: {byte_probabilities[byte]: .6f}, Информация: {byte_information[byte]:.6f} ")

print("\nТаблица характеристик символов по убыванию частоты:")

for byte, prob in sorted_byte_probabilities_by_freq:
    print(f"Символ: {byte}, Ненормированная частота: {byte_frequencies[byte]}, Оценка вероятности: {byte_probabilities[byte]: .6f}, Информация: {byte_information[byte]:.6f}")


print(total_information)
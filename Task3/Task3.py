import collections
import os
from email.policy import default

import chardet


def calculate_octet_frequencies(file_path):
    octet_frequencies = collections.Counter()

    with open(file_path, 'rb') as file:
        content = file.read()
        octet_frequencies.update(content)

    return octet_frequencies


def print_top_octets(octet_frequencies_no_ascii, n, printable=True):
    if printable:
        print(f"Топ {n} октетов:")
    else:
        print(f"Топ {n} не печатных октетов:")
    for octet, freq in octet_frequencies_no_ascii.most_common(n):
        print(f"Октет: 0x{octet:02X}, Частота: {freq}")

# Папка с файлами plaintext
plaintext_folder = 'files/plaintext/'

# Перебираем файлы в папке
for filename in os.listdir(plaintext_folder):
    file_path = os.path.join(plaintext_folder, filename)

    octet_frequencies = calculate_octet_frequencies(file_path)
    print(f"\nАнализ файла: {filename}")
    print_top_octets(octet_frequencies, 4)

    octet_frequencies_no_ascii = calculate_octet_frequencies(file_path)
    for i in range(32, 127):
        octet_frequencies_no_ascii.pop(i, None)

    for i in range(128, 256):
        octet_frequencies_no_ascii.pop(i, None)

    print_top_octets(octet_frequencies_no_ascii, 4, False)


print("files/7.txt")
# Путь к файлу 𝑍 (замените на соответствующий путь)
file_z_path = 'files/7.txt'
if os.path.exists(file_z_path):
    # Определяем кодировку файла Z
    with open(file_z_path, 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        encoding = result['encoding']
        octet_frequencies = collections.Counter()
        octet_frequencies.update(data)


        for octet, freq in octet_frequencies.items():
            print(f"Октет: 0x{octet:02X}, Частота: {freq}")
        try:
            decoded_text = data.decode(encoding)
            print("Файл Z является русскоязычным текстом в кодировке", encoding)
        except UnicodeDecodeError:
            print("Файл Z не является русскоязычным текстом в стандартных кодировках")

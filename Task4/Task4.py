import collections
import math
import re



def count_exact(full_string: str, substr: str) -> int:
    return len(re.findall(rf'{substr}', full_string))

def count_inexact(full_string: str, symbol: str) -> int:
    if len(full_string) == 0 or len(symbol) == 0:
        return 0

    return len(re.findall(rf'{symbol}.', full_string)) + int(full_string[-1] == symbol)



def get_cond_prob(ak: str, aj: str) -> float:
    return count_exact(ak, aj) / count_inexact(ak, aj)

def calculate_information(probability):
    if probability == 0:
        return 0
    return -math.log2(probability)

def get_total_information(file_path: str) -> [int, int] :
    with open(file_path, 'rb') as file:
        file_content = file.read()


    # Считаем частоту вхождения каждого байта
    byte_frequencies = collections.Counter(file_content)

    # Рассчитываем вероятность и информацию для каждого байта
    byte_information = {byte: calculate_information(1/256) for byte, _ in byte_frequencies.items()}

    # Рассчитываем суммарное количество информации в файле
    total_information = sum(freq * byte_information[byte] for byte, freq in byte_frequencies.items())

    return total_information * 8, total_information

print(get_total_information('file.txt')[1])
import timeit
from tabulate import tabulate

from KMP_search import KMP_search
from BM_search import BM_search
from RK_search import RK_search

def measure_time(func, text, pattern):
    if not text or not pattern:
        return float('inf')
    return timeit.timeit(lambda: func(pattern, text), number=10)

def run_test():
    try:
        with open('data/article01.txt', 'r', encoding='utf-8') as f1, \
             open('data/article02.txt', 'r', encoding='utf-8') as f2:
            text1 = f1.read()
            text2 = f2.read()

        # Substrings to search
        real_pattern = "перевірити коректність пароля"
        fake_pattern = "вигадана фраза"

        # Results for article 1
        time_KMP1_real = measure_time(KMP_search, text1, real_pattern)
        time_BM1_real = measure_time(BM_search, text1, real_pattern)
        time_RK1_real = measure_time(RK_search, text1, real_pattern)

        time_KMP1_fake = measure_time(KMP_search, text1, fake_pattern)
        time_BM1_fake = measure_time(BM_search, text1, fake_pattern)
        time_RK1_fake = measure_time(RK_search, text1, fake_pattern)

        # Results for article 2
        time_KMP2_real = measure_time(KMP_search, text2, real_pattern)
        time_BM2_real = measure_time(BM_search, text2, real_pattern)
        time_RK2_real = measure_time(RK_search, text2, real_pattern)

        time_KMP2_fake = measure_time(KMP_search, text2, fake_pattern)
        time_BM2_fake = measure_time(BM_search, text2, fake_pattern)
        time_RK2_fake = measure_time(RK_search, text2, fake_pattern)

        headers = ["Алгоритм", "Стаття 1 (реальний)", "Стаття 1 (вигаданий)", "Стаття 2 (реальний)", "Стаття 2 (вигаданий)"]
        table = [
            ["KMP", time_KMP1_real, time_KMP1_fake, time_KMP2_real, time_KMP2_fake],
            ["BM", time_BM1_real, time_BM1_fake, time_BM2_real, time_BM2_fake],
            ["RK", time_RK1_real, time_RK1_fake, time_RK2_real, time_RK2_fake],
        ]

        print(tabulate(table, headers=headers, floatfmt=".6f"))

    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run_test()
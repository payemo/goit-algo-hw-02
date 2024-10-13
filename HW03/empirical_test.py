import timeit
import random
import copy
import csv
from tabulate import tabulate

from insertion_sort import insertion_sort
from merge_sort import merge_sort

def Timsort(arr):
    return sorted(arr)

def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def generate_sorted_list(size):
    return list(range(size))

def generate_partially_sorted_list(size):
    sorted_list = list(range(size))
    for i  in range(0, size, 10):
        if i + 1 < size:
            sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
    return sorted_list

def measure_time(sort_func, arr):
    arr_copy = copy.deepcopy(arr)
    start_time = timeit.default_timer()
    sort_func(arr_copy)
    end_time = timeit.default_timer()
    return end_time - start_time

def save_results(filename, headers, results):
    with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(results)
    print(f"\nResults saved to {filename}")

def run_tests():
    # Time measuring
    sizes = [1000, 5000, 10000, 100000]
    sort_funcs = [insertion_sort, merge_sort, Timsort]
    arr_types = {
        "Random": generate_random_list,
        "Sorted": generate_sorted_list,
        "Partially sorted": generate_partially_sorted_list
    }

    for arr_type, arr_gen_alg in arr_types.items():
        print(f"\n\n===== {arr_type} Data =====")
        results = []
        headers = ["Size", "Insertion Sort", "Merge Sort", "Timsort"]

        for size in sizes:
            row = [size]
            arr = arr_gen_alg(size)

            for sort_func in sort_funcs:
                if sort_func == insertion_sort and size > 10000:
                    row.append('N/A')
                    continue
                time = measure_time(sort_func, arr)
                row.append(f"{time:.6f}")
            results.append(row)

        # Display table
        print(tabulate(results, headers=headers, tablefmt="github"))

        # Save results to .CSV
        filename = f"{arr_type}_results.csv".replace(" ", "_")
        save_results(filename, headers, results)

if __name__ == '__main__':
    run_tests()
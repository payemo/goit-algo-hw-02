import heapq

def merge_k_lists(lists):
    merged_list = []
    minheap = []

    for i, list in enumerate(lists):
        if list:
            heapq.heappush(minheap, (list[0], i, 0))

    while minheap:
        val, list_idx, el_idx = heapq.heappop(minheap)
        merged_list.append(val)

        if el_idx + 1 < len(lists[list_idx]):
            next_tup = (lists[list_idx][el_idx + 1], list_idx, el_idx + 1)
            heapq.heappush(minheap, next_tup)
    
    return merged_list

if __name__ == '__main__':
    l = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]
    merged = merge_k_lists(l)
    print("Злитий відсортований список:", merged)
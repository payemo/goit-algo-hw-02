def dbinary_search(darr: list[float], s: float):
    iters = 0
    upper_bound = None
    low, high = 0, len(darr) - 1

    while(low <= high):
        mid = low + (high - low) // 2

        if darr[mid] == s:
            if mid + 1 < len(darr):
                return (iters, darr[mid + 1])
            else:
                return (iters, darr[mid])
        
        if darr[mid] > s:
            upper_bound = darr[mid]
            high = mid - 1
        else:
            low = mid + 1

        iters += 1
    
    return (iters, upper_bound)


darr = [0.52124, 5.123124, 8.2512, 10.12521, 11.20124, 11.98372, 14.52153]
print(dbinary_search(darr, 0.52124))
print(dbinary_search(darr, 0.52512))
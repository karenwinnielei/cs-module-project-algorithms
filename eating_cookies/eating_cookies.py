'''
Input: an integer
Returns: an integer
'''
from functools import lru_cache

def eating_cookies(n, cache = None):
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if cache is None:
            cache = [0 for i in range(n + 1)]
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]


# @lru_cache(maxsize=1000)
# def eating_cookies_lru(n):
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     else:
#         return eating_cookies_lru(n - 1) + eating_cookies_lru(n - 2) + eating_cookies_lru(n - 3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 500

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    # print(f"There are {eating_cookies_lru(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

def two_sum(arr, k):


    num_dict = {}

    for i, num in enumerate(arr):
        complement = k - num

        if complement in num_dict:
            idx1, idx2 = num_dict[complement], i
            return f"{min(idx1, idx2)}, {max(idx1, idx2)}"

        num_dict[num] = i

    return None



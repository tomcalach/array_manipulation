def array_manipulation(n, queries):
    """
    the function takes a size n of an array, and the list of list queries. each nested list in queries contain 3 ints:
    a- index of a member in the array, b(>a)- index of a member in the array (both of the indexes are 1 based),
    and k- int value that supposed to be added
    to all the list member between a and b (including). the function gives back the max value of all the members in the
    list after all the queries. the good first function is doing so in O(queries), while the others are doing so in
    O(n*queries).
    :param n: int
    :param queries: list of lists of 3 ints
    :return: int
    """
    # we are making a zeroed list in the length of n+1; then we are adding the value 'k' to all the 'a' indexes, and
    # subtracting the value 'k' from each b+1 point
    array = [0] * (n+1)
    for query in queries:
        point_a = query[0]-1
        point_b = query[1]
        k_increase = query[2]
        array[point_a] += k_increase
        array[point_b] -= k_increase

    # we are summing all the members of list we received from the first step one by one, after each summation we are
    # checking if the current sum is the max value we had so far, and remember it if is the max. that gives us the max
    # value of the array (the minus k appearances are canceling the plus k ones in the member that are outside of the
    # addition range).
    max_amount = accumulate_amount = 0
    for amount in array:
        accumulate_amount += amount
        if accumulate_amount > max_amount:
            max_amount = accumulate_amount

    return max_amount



# def array_manipulation(n, queries):
#     array = [0] * n
#     for query in queries:
#         print(array)
#         for i in range(query[0]-1, query[1]):
#             array[i] += query[2]
#     return max(array)


# def array_manipulation(n, queries):
#     maxi = 0
#     for ind in range(n):
#         ind_score = 0
#         for query in queries:
#             if query[0]-1 <= ind <= query[1]-1:
#                 ind_score += query[2]
#         if ind_score > maxi:
#             maxi = ind_score
#     return maxi


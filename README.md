# array_manipulation
    the function takes a size n of an array, and the list of list queries. each nested list in queries contain 3 ints:
    a- index of a member in the array, b(>=a)- index of a member in the array (both of the indexes are 1 based),
    and k- int value that supposed to be added
    to all the list member between a and b (including). the function gives back the max value of all the members in the
    list after all the queries. the good first function is doing so in O(queries), while the others are doing so in
    O(n*queries).

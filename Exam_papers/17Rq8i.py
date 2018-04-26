def partition(A, p, r):
    q = j = p
    while j < r:
        if A[j] <= A[r]:
            A[q], A[j] = A[j], A[q]
            q += 1
        j += 1
    A[q], A[r] = A[r], A[q]
    return q

A = [12, 88, 54, 50, 66, 41, 24, 46, 10, 21]
partition(A, 0, len(A) - 1)
print(A)

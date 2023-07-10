def create_cube_list(max_value):
    A = []
    for i in range(1, 200000):
        A.append(i**3)
        if A[i-1] > max_value:
            A.pop()
            break
    return A

B = create_cube_list(C)
print(B)

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i-1]
            for j in range(1, i):
                element = prev_row[j-1] + prev_row[j]
                row.append(element)
            row.append(1)
        triangle.append(row)

    return triangle

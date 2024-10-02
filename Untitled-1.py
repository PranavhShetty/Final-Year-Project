def String2igzag(strArr):
    word, rows = strArr[0], int(strArr[1])
    if rows == 1:
        return word
    
    matrix = [[' ' for _ in range(len(word))] for _ in range(rows)]
    row, col = 0, 0
    down = True

    for char in word:
        matrix[row][col] = char
        if row == rows - 1:
            down = False
        elif row == 0:
            down = True

        if down:
            row += 1
        else:
            row -= 1
            col += 1

    result = ''
    for i in range(rows):
        for j in range(len(word)):
            if matrix[i][j] != ' ':
                result += matrix[i][j]
    
    return result

# Example usages
result1 = String2igzag(["cat", "5"])
print(result1)  # Output: "cat"

result2 = String2igzag(["kaamvjjf1", "4"])
print(result2)  # Output: "kjajfavim"

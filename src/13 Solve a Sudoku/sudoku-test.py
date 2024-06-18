N = 9
# Checks to see if a 9x9 multi-dimensional array is passed in
def check_sudoku(array):
  if(len(array) != 9):
    return False
  
  for i in range(9):
    if(len(array[i]) != 9):
      return False
    
  return True

# Attempts to solve the array value
def solve_sudoku(array):
  if(not check_sudoku(array)):
    return "Sudoku array must be a 9x9 2 dimensional array"
  
  if solve_grid(array, 0, 0):
    return array
  else:
    return "Could not solve sudoku"

def isValid(array, row, col, num):
  for x in range(N):
    if array[row][x] == num:
      return False
  for x in range(N):
    if array[x][col] == num:
      return False
  startRow = row - row % 3
  startCol = col - col % 3
  for i in range(3):
    for j in range(3):
      if array[i + startRow][j + startCol] == num:
        return False
  return True

def solve_grid(array, row, col):
  if row == N - 1 and col == N:
    return True
  
  if col == N:
    row += 1
    col = 0
  
  if array[row][col] > 0:
    return solve_grid(array, row, col+1)
  for num in range(1, N+1, 1):
    if isValid(array, row, col, num):
      array[row][col] = num
      if solve_grid(array, row, col+1):
        return True
    array[row][col] = 0
  return False

def print_sudoku(array):
  for i in range(N):
    if i == 3 or i == 6:
      print("-----------------")
    for j in range(N):
      chr = array[i][j]
      chEnd = " "
      if(chr == 0):
        chr = '*'
      if( j == 2 or j == 5):
        chEnd = "|"
      print(chr, end=chEnd)
    print()

if __name__ == '__main__':
  puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
  result = solve_sudoku(puzzle)
  if type(result) == list:
    print_sudoku(result)
  else:
    print(result)
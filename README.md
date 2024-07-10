<h1 align="center">Sudoku Validator</h1>

Sudoku is a puzzle based on logic and combinatorial number placement. The goal in classic Sudoku is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids (also known as “boxes") contain all the digits from 1 to 9. The puzzle begins with a partially filled grid, and a well-designed puzzle will have only one possible solution.

<img align="center" src="https://github.com/KawasakiLucas/sudoku-checker-solver/blob/master/Sudoku_Puzzle.png">

<h2 align="center">Rules</h2>

A sudoku is valid if and only if:

- A row contains all numbers from `1` to `9`.
- A column contains all numbers from `1` to `9`.
- Each of the nine 3x3 little squares contains numbers from `1` to `9`.

<br />

<h2 align="center">Example</h2>

A Sudoku grid will be represented by a Python list of lists:

```python
grid = [
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],

    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],

    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4]
]
```

<h2 align="center">Idea</h2>

To make the program concise and easy to understand:

- Create a function to validate the elements in the row.
- Create a function to validate the elements in the column.
- Create a function to validate the elements in the boxes.

In the end, create a function to validate all the functions above.

#

🔗 [Check out my other projects here ->](https://github.com/KawasakiLucas/portfolio)

#

Thank you for your time.

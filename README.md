
# Sparse Matrix Operations

## Introduction

This project implements a `SparseMatrix` class in Python that efficiently handles sparse matrices and supports matrix operations such as addition, subtraction, and multiplication. Sparse matrices are matrices where most of the elements are zero, and this implementation focuses on optimizing memory usage by only storing non-zero elements.

## Features

- **File-based Matrix Input**: Load matrices from text files where matrix dimensions and non-zero elements are specified.
- **Sparse Matrix Representation**: Matrices are stored as dictionaries to save memory by only keeping track of non-zero elements.
- **Matrix Operations**: Supports addition, subtraction, and multiplication of sparse matrices.
- **File Output**: Results of matrix operations can be written to an output file.

## File Format

The input matrix file should have the following format:

- The first two lines specify the number of rows and columns in the matrix:
  ```
  rows=<number_of_rows>
  cols=<number_of_cols>
  ```
- Non-zero matrix elements are provided in the form:
  ```
  (row, col, value)
  ```
  where:
  - `row` is the row index (starting from 0).
  - `col` is the column index (starting from 0).
  - `value` is the integer value at that matrix position.


## Usage

### 1. Loading Matrices

You can load a sparse matrix from a file by specifying the file path when initializing a `SparseMatrix` object:

```python
matrix1 = SparseMatrix(file_path="matrix1.txt")
```

### 2. Performing Matrix Operations

The following operations are supported:

- **Addition**: Add two matrices if they have the same dimensions.
  ```python
  result = matrix1 + matrix2
  ```

- **Subtraction**: Subtract one matrix from another if they have the same dimensions.
  ```python
  result = matrix1 - matrix2
  ```

- **Multiplication**: Multiply two matrices if the number of columns in the first matrix matches the number of rows in the second matrix.
  ```python
  result = matrix1 * matrix2
  ```

### 3. Writing Results to a File

The result of an operation can be written to a file in the same format as the input:

```python
result.write_matrix_to_file("output_matrix.txt")
```

### 4. Command Line Interaction

The program also supports command-line interaction. Upon execution, the user can input the file paths for the matrices and choose the operation to perform. The result will be saved to an output file.

### Example Execution:

```python
Enter the path of the first matrix file: matrix1.txt
Enter the path of the second matrix file: matrix2.txt
Which operation would you like to perform?
1. Add
2. Subtract
3. Multiply
Enter your choice: 1
Enter the path for the output file: result_matrix.txt
```

## Error Handling

- **File Not Found**: If the input file is not found, a `FileNotFoundError` is raised.
- **Invalid Format**: If the input file format is incorrect (e.g., missing parentheses, non-integer values), a `ValueError` is raised.
- **Dimension Mismatch**: If the matrices are incompatible for the chosen operation (e.g., addition with mismatched dimensions or multiplication with incompatible row/column counts), a `ValueError` is raised.

## Requirements

- Python 3.x

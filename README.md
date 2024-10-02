# README

## Sparse Matrix Operations Script

### Overview
This Python script performs operations on sparse matrices, which are matrices with mostly zero elements. The operations supported include addition, subtraction, and multiplication of two sparse matrices. The script reads matrices from input files, processes them into a sparse matrix format, performs the chosen operation, and outputs the result to an output file.

### Features
- **Addition**: Add two sparse matrices.
- **Subtraction**: Subtract one sparse matrix from another.
- **Multiplication**: Multiply two sparse matrices.
- **Transpose**: Automatically transposes the second matrix for multiplication if needed.

### File Input Format
The input file should contain:
1. Dimensions of the matrix in the format:
   ```
   rows=<number_of_rows>
   cols=<number_of_columns>
   ```
2. Matrix data in the format:
   ```
   (row, column, value)
   ```
   - Rows, columns, and values should be integers.
   - Only non-zero values should be listed.

### How to Use the Script

1. **Input Files**: Prepare two input files with sparse matrix data. Each file should be formatted as described above.
2. **Run the Script**: Execute the script from the command line.
   
   ```bash
   python script.py
   ```

3. **Follow Prompts**: 
   - The script will ask you to enter the path of the first matrix file.
   - It will then ask for the second matrix file (it allows you to enter the same file if desired).
   - You will be asked to choose an operation: addition, subtraction, or multiplication.
   - Finally, provide the path to the output file where results will be saved.


### Functions Overview

- **`UtilFunctions.ltrim(s)`**: Removes leading spaces or tabs from the string.
- **`UtilFunctions.rtrim(s)`**: Removes trailing spaces, tabs, and newlines from the string.
- **`UtilFunctions.trim(s)`**: Removes both leading and trailing spaces, tabs, and newlines from the string.
- **`UtilFunctions.custom_append(lst, item)`**: Appends an item to a list.
- **`UtilFunctions.str_to_int(s)`**: Converts a string to an integer, handling edge cases like negative numbers or invalid inputs.
- **`UtilFunctions.mergeSort(array, begin, end)`**: Performs merge sort on a list.
- **`SparseMatrix.insert(r, c, val)`**: Inserts a value into the sparse matrix at a specific position.
- **`SparseMatrix.add(other)`**: Adds two sparse matrices.
- **`SparseMatrix.subtract(other)`**: Subtracts one sparse matrix from another.
- **`SparseMatrix.multiply(other)`**: Multiplies two sparse matrices.
- **`SparseMatrix.transpose()`**: Transposes a matrix (swapping rows with columns).
- **`process_input(input_path)`**: Processes the input file to create a sparse matrix.
- **`output_results(output_path, results, r, c)`**: Writes the resulting matrix to an output file.

### Dependencies
- Python 3.x

### Error Handling
- The script checks for invalid matrix dimensions or positions when inserting values.
- It raises exceptions when input files are incorrectly formatted or when matrix operations are not possible due to incompatible dimensions.

### Limitations
- Input files must be formatted correctly, or the script will throw errors.
- Only non-zero elements are stored, so the matrices must be sparse for efficient storage.

### License
MIT License

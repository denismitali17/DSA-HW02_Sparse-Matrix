class SparseMatrix:
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = {}

        if file_path:
            self.read_matrix_from_file(file_path)

    def read_matrix_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                # Reading rows and cols
                self.num_rows = int(file.readline().split('=')[1])
                self.num_cols = int(file.readline().split('=')[1])

                # Reading matrix entries
                for line in file:
                    line = line.strip()
                    if line:  # Skip empty lines
                        if not line.startswith('(') or not line.endswith(')'):
                            raise ValueError("Input file has wrong format (Invalid parentheses)")

                        # Extract row, col, value and check for floating points
                        try:
                            row, col, value = map(int, line[1:-1].split(','))
                        except ValueError:
                            raise ValueError("Input file has wrong format (Invalid values or floating point numbers)")

                        self.set_element(row, col, value)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} not found.")
        except Exception as e:
            raise e

    def get_element(self, row, col):
        return self.matrix.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.matrix[(row, col)] = value
        elif (row, col) in self.matrix:
            del self.matrix[(row, col)]

    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for addition")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (r, c), v in self.matrix.items():
            result.set_element(r, c, v + other.get_element(r, c))
        for (r, c), v in other.matrix.items():
            if (r, c) not in self.matrix:
                result.set_element(r, c, v)
        return result

    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match for subtraction")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (r, c), v in self.matrix.items():
            result.set_element(r, c, v - other.get_element(r, c))
        for (r, c), v in other.matrix.items():
            if (r, c) not in self.matrix:
                result.set_element(r, c, -v)
        return result

    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not allow multiplication")

        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (r1, c1), v1 in self.matrix.items():
            for r2 in range(other.num_cols):
                v2 = other.get_element(c1, r2)
                if v2 != 0:
                    result.set_element(r1, r2, result.get_element(r1, r2) + v1 * v2)
        return result

    def write_matrix_to_file(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"rows={self.num_rows}\n")
            file.write(f"cols={self.num_cols}\n")
            for (r, c), v in self.matrix.items():
                file.write(f"({r}, {c}, {v})\n")

# Test to make sure everything works
if __name__ == "__main__":
    try:
        # Load first matrix
        input_file1 = input("Enter the path of the first matrix file: ")
        matrix1 = SparseMatrix(file_path=input_file1)

        # Load second matrix
        input_file2 = input("Enter the path of the second matrix file: ")
        if input_file1 == input_file2:
            matrix2 = matrix1
        else:
            matrix2 = SparseMatrix(file_path=input_file2)

        # Choose operation
        print("Which operation would you like to perform?")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        choice = input("Enter your choice: ")

        # Perform the operation
        output_file = input("Enter the path for the output file: ")
        if choice == '1':
            result = matrix1 + matrix2
            result.write_matrix_to_file(output_file)
        elif choice == '2':
            result = matrix1 - matrix2
            result.write_matrix_to_file(output_file)
        elif choice == '3':
            result = matrix1 * matrix2
            result.write_matrix_to_file(output_file)
        else:
            print("Invalid operation choice")

    except Exception as e:
        print(f"Error: {e}") 

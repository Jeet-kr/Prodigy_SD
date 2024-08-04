import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver App by JK")
        self.window.geometry("460x500")
        self.window.configure(bg="#E5E5E5")
        self.window.resizable(False, False)

        # Create a frame to hold the content
        self.frame = tk.Frame(self.window, bg="#E5E5E5")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create grid of cells
        self.cells = {(i, j): tk.Entry(self.frame, width=2, font=("Arial", 24), justify="center", bg="#F0F0F0") for i in range(9) for j in range(9)}
        for (i, j), cell in self.cells.items():
            cell.grid(row=i, column=j)

        # Create solve button
        solve_button = tk.Button(self.frame, text="Solve", command=self.solve_sudoku, bg="#32CD32", fg="#FFFFFF")
        solve_button.grid(row=10, column=0, columnspan=4, pady=(20, 0))

        # Create clear button
        clear_button = tk.Button(self.frame, text="Clear", command=self.clear_sudoku, bg="#FF0000", fg="#FFFFFF")
        clear_button.grid(row=10, column=5, columnspan=4, pady=(20, 0))

    def solve_sudoku(self):
        # Get values from cells
        values = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.cells[(i, j)].get()
                if value == "":
                    row.append(0)
                elif value.isdigit() and 1 <= int(value) <= 9:
                    row.append(int(value))
                else:
                    messagebox.showerror("Error", "Invalid input")
                    return
            values.append(row)

        # Solve Sudoku
        if self.is_valid_sudoku(values):
            solution = self.solve(values)
            if solution:
                # Fill in solution
                for i in range(9):
                    for j in range(9):
                        self.cells[(i, j)].delete(0, tk.END)
                        self.cells[(i, j)].insert(0, str(solution[i][j]))
            else:
                messagebox.showerror("Error", "No solution exists")
        else:
            messagebox.showerror("Error", "Invalid Sudoku")

    def is_valid_sudoku(self, values):
        # Check rows and columns
        for i in range(9):
            row = [values[i][j] for j in range(9)]
            col = [values[j][i] for j in range(9)]
            if not self.is_valid_row(row) or not self.is_valid_row(col):
                return False

        # Check boxes
        for i in range(3):
            for j in range(3):
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append(values[i*3+x][j*3+y])
                if not self.is_valid_row(box):
                    return False

        return True

    def is_valid_row(self, row):
        seen = set()
        for value in row:
            if value != 0 and value in seen:
                return False
            seen.add(value)
        return True

    def solve(self, values):
        # Find empty cell
        for i in range(9):
            for j in range(9):
                if values[i][j] == 0:
                    # Try values 1-9
                    for value in range(1, 10):
                        values[i][j] = value
                        if self.is_valid_sudoku(values):
                            solution = self.solve(values)
                            if solution:
                                return solution
                    # If no value works, return None
                    values[i][j] = 0
                    return None
        # If all cells filled, return solution
        return values

    def clear_sudoku(self):
        # Clear all cells
        for i in range(9):
            for j in range(9):
                self.cells[(i, j)].delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = SudokuSolver()
    app.run()
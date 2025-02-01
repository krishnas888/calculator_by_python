### **Brief Description of the Code**
This Python script creates a simple **GUI-based calculator** using **Tkinter**.

### **Key Components**
1. **Main Class (`Application`)**
   - Inherits from `Frame`, which acts as a container for organizing widgets.
   - Initializes with an entry field (`Entry`) to display input/output.
   - Calls `creat_widgets()` to generate buttons for numbers (0-9) and operations (+, -, *, /).

2. **Button Creation (`creat_widgets`)**
   - Uses `Button` widgets to create number buttons (0-9).
   - Adds operator buttons (`+`, `-`, `*`, `/`).
   - Includes `=` (equals) to evaluate expressions and `AC` (clear) to reset.

3. **Functionalities**
   - `buttonClick(number)`: Appends the clicked number/operator to the input field.
   - `CalculateTask()`: Evaluates the entered expression using `eval()`.
   - `displayText(value)`: Updates the input field with the result.
   - `ClearDisplay()`: Clears the input field.

4. **Main Application Setup**
   - `Tk()` initializes the main window.
   - `Application(calculator)` creates an instance of the calculator.
   - `mainloop()` keeps the GUI running.

### **Final Output**
A functional calculator where users can input numbers, perform basic arithmetic, and clear the screen when needed. 🚀


![Screenshot 2025-02-01 120457](https://github.com/user-attachments/assets/89aabd23-bd1c-4bb9-ab9f-5a5aec82dfe0)

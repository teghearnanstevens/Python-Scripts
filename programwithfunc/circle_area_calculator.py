import tkinter as tk
import math

def main():
    # Create the root window
    root = tk.Tk()
    root.title("Circle Area Calculator")

    # Call the function to populate the GUI
    populate_main_window(root)

    # Start the GUI event loop
    root.mainloop()


def populate_main_window(root):
    """Create and grid the widgets in the main window."""
    
    # Create labels, entry boxes, and buttons
    lbl_radius = tk.Label(root, text="Radius:")
    ent_radius = tk.Entry(root)
    lbl_area = tk.Label(root, text="Area:")
    lbl_result = tk.Label(root, text="")
    lbl_status = tk.Label(root, text="", fg="red", anchor="w")  # Status bar
    
    btn_calculate = tk.Button(root, text="Calculate")
    btn_clear = tk.Button(root, text="Clear")

    # Position widgets in a grid
    lbl_radius.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    ent_radius.grid(row=0, column=1, padx=5, pady=5)
    lbl_area.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    lbl_result.grid(row=1, column=1, padx=5, pady=5)
    lbl_status.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    btn_calculate.grid(row=2, column=0, padx=5, pady=5)
    btn_clear.grid(row=2, column=1, padx=5, pady=5)

    # Nested functions for the buttons
    def calculate():
        """Calculate the area of a circle and display the result."""
        try:
            # Get the radius entered by the user
            radius = float(ent_radius.get())
            if radius < 0:
                raise ValueError("Radius must be non-negative.")
            
            # Compute the area of the circle
            area = math.pi * radius**2
            
            # Display the result
            lbl_result.config(text=f"{area:.2f}")
            lbl_status.config(text="")  # Clear the status bar
        except ValueError as e:
            # Display an error message in the status bar
            lbl_status.config(text=f"Error: {e}")
            lbl_result.config(text="")  # Clear the result

    def clear():
        """Clear all inputs and outputs."""
        ent_radius.delete(0, tk.END)
        lbl_result.config(text="")
        lbl_status.config(text="")

    # Bind the functions to the buttons
    btn_calculate.config(command=calculate)
    btn_clear.config(command=clear)


# Run the main function
if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox

def launch_gui(model):
    if model is None:
        print("Model is not available. Cannot launch GUI.")
        return
    # Create the GUI window
    window = tk.Tk()
    window.title("Real Estate Price Predictor")
    window.geometry("400x300")

    # Input fields for property details
    location_label = tk.Label(window, text="Location")
    location_label.pack()
    location_entry = tk.Entry(window)
    location_entry.pack()

    size_label = tk.Label(window, text="Property Size (sqft)")
    size_label.pack()
    size_entry = tk.Entry(window)
    size_entry.pack()

    rooms_label = tk.Label(window, text="Number of Rooms")
    rooms_label.pack()
    rooms_entry = tk.Entry(window)
    rooms_entry.pack()

    # Predict button action
    def predict_price():
        try:
            location = location_entry.get()
            size = float(size_entry.get())
            rooms = int(rooms_entry.get())
            # Feature vector
            features = [[size, rooms]]
            predicted_price = model.predict(features)
            messagebox.showinfo("Predicted Price", f"Estimated Price: ${predicted_price[0]:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for size and rooms.")

    predict_button = tk.Button(window, text="Predict Price", command=predict_price)
    predict_button.pack()

    # Run the GUI loop
    window.mainloop()

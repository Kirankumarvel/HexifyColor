import tkinter as tk
from tkinter import messagebox, ttk
from src.utils import get_hex_code

def show_hex_code():
    """Display the hex code for the entered color name."""
    color_name = entry.get()
    hex_code = get_hex_code(color_name)
    
    if hex_code:
        result_label.config(text=f"Hex Code for '{color_name}': {hex_code}", foreground=hex_code)
        color_preview.config(bg=hex_code)
    else:
        messagebox.showerror("Error", "Invalid color name. Try common names like 'red', 'skyblue', 'orange'.")
        result_label.config(text="")
        color_preview.config(bg=app_bg)

def main():
    """Initialize the GUI application."""
    global entry, result_label, color_preview, app_bg

    # Colors and styles
    app_bg = "#23272f"
    fg_color = "#f8f8f2"
    accent_color = "#7ed957"
    entry_bg = "#2d323c"
    entry_fg = "#f8f8f2"
    btn_bg = accent_color
    btn_fg = "#23272f"

    # Initialize main window
    app = tk.Tk()
    app.title("ColorHexplorer")
    app.geometry("350x220")
    app.resizable(False, False)
    app.configure(bg=app_bg)

    # Style
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", font=("Segoe UI", 11, "bold"), background=btn_bg, foreground=btn_fg)
    style.configure("TLabel", background=app_bg, foreground=fg_color, font=("Segoe UI", 11))
    
    # Title Label
    title = tk.Label(app, text="ColorHexplorer", font=("Segoe UI", 16, "bold"), bg=app_bg, fg=accent_color)
    title.pack(pady=(15, 5))

    # Input Label
    label = tk.Label(app, text="Enter a Color Name:", bg=app_bg, fg=fg_color, font=("Segoe UI", 11))
    label.pack(pady=(5, 2))

    # Input Entry
    entry = tk.Entry(app, width=25, font=("Segoe UI", 11), bg=entry_bg, fg=entry_fg, insertbackground=entry_fg, relief="flat", justify="center")
    entry.pack(pady=2)
    entry.focus()

    # Submit Button
    btn = ttk.Button(app, text="Get Hex Code", command=show_hex_code)
    btn.pack(pady=8)

    # Result Label
    result_label = tk.Label(app, text="", bg=app_bg, fg=accent_color, font=("Segoe UI", 11, "bold"))
    result_label.pack(pady=(8, 2))

    # Color Preview Box
    color_preview = tk.Label(app, width=10, height=2, bg=app_bg, bd=1, relief="solid")
    color_preview.pack(pady=(2, 0))

    # Start the application
    app.mainloop()

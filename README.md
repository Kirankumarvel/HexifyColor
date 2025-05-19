# HexifyColor – Discover Hex Codes for Common Colors

A simple Python tool to convert common color names to their hexadecimal codes using the webcolors library.


---

## 🌟 **Features:**
- Convert color names to hex codes with a simple user interface.
- Live color preview based on the hex code.
- Error handling for invalid color names with informative messages.
- Modern and visually pleasing design using Tkinter and custom styles.

---

## 🛠️ **Project Structure:**

ColorHexplorer/
│─── app.py # Main entry point
│─── requirements.txt # Library dependencies
│─── README.md # Project documentation
│─── ui/
│ └─── main.py # GUI logic
│─── src/
│ └─── utils.py # Utility functions (hex conversion)
│─── assets/
│ └─── logo.png # (Optional) App logo
│─── tests/
│ └─── test_utils.py # Unit tests for utility functions

yaml
Copy
Edit

---

## ✅ **Dependencies:**

- **webcolors:** Converts color names to hexadecimal codes.
- **tkinter:** Built-in Python library for creating graphical interfaces.  
- **ttk:** Provides themed widgets for a modern look.

---

## 🔧 **Installation and Setup:**

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/ColorHexplorer.git
cd ColorHexplorer
Install required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Note: tkinter is included in Python by default. Only webcolors needs to be installed.

🚀 Usage:
Run the application using:

bash
Copy
Edit
python app.py
Enter a valid color name (e.g., red, blue, skyblue).

Click Get Hex Code to see the hexadecimal code.

The preview box will change color to match the entered color name.

✅ Example:
Input:

css
Copy
Edit
Enter a color name: Silver
Output:

csharp
Copy
Edit
Hex Code for 'Silver' is: #c0c0c0
Live Preview: The preview box changes to the color #c0c0c0.

🛠️ Libraries and Modules Used:
Library	Description
webcolors	Converts color names to hexadecimal codes.
tkinter	Python’s standard GUI toolkit.
ttk	Themed widgets for a more modern UI.

✅ Future Enhancements:
Implement dark mode and light mode toggling.

Add a search bar for all available color names.

Include a copy-to-clipboard button for the hex code.

Add more styling options for the preview box.

📦 License:
This project is licensed under the MIT License.


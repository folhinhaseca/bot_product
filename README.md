# 🛒 Product Registration Automation Bot

This project uses **Python** with the **PyAutoGUI** library to automate the process of registering products on a web system.

## 📋 Description

The script performs the following steps:

1. Opens the Google Chrome browser.
2. Accesses the system login page.
3. Logs in using email and password.
4. Reads a `produtos.csv` spreadsheet containing product data.
5. Automatically fills in the form fields with the information from the spreadsheet.
6. Submits the registration for each product.

## 📂 Data Structure

The `produtos.csv` file must contain the following columns:

- `codigo`: Product code
- `marca`: Brand
- `tipo`: Type
- `categoria`: Category
- `preco_unitario`: Unit price
- `custo`: Cost
- `obs`: Notes (optional)

## 🧰 Technologies Used

- Python 3.x
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- Pandas

## ⚠️ Requirements

- The screen resolution must match the one used when configuring the automation.
- The browser must be installed and accessible via the Start menu.
- The website and clickable elements must be in the same position on the screen, or the click coordinates must be adjusted accordingly.

## 🚀 Running the Script

1. Install the dependencies:

```bash
pip install pyautogui pandas

# 🛒 Python Supermarket Billing System

A lightweight, interactive command-line application built in Python that simulates a supermarket checkout process. It allows users to add items to a digital cart, track both the original cost and the discounted price, edit their cart, and print a beautifully formatted receipt.

## ✨ Features
* **Dynamic Cart Management:** Users can add as many items to their cart as they want using an infinite loop that breaks upon a 'q' command.
* **Review & Edit System:** Before checking out, users can view their current cart and remove items by their index number.
* **Auto-Recalculation:** The system calculates the final totals only after the user has finished editing their cart, ensuring 100% accuracy.
* **Clean Tabular Receipts:** Utilizes the `pandas` library to organize items, original prices, and discounted prices into a highly readable, structured receipt.
* **Savings Tracker:** Automatically calculates and displays the total amount of money the user saved at the bottom of the receipt.

## 🚀 How to Run

### Prerequisites
You must have Python 3 installed on your machine, along with the `pandas` library. 
If you don't have pandas installed, you can install it via terminal:
```bash
pip install pandas

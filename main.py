import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
from datetime import datetime

# --- Payment Strategy Interface ---
class PaymentStrategy:
    def pay(self, amount):
        pass

# --- Concrete Strategies ---
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid ${amount:.2f} via Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid ${amount:.2f} via PayPal")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid ${amount:.2f} via Cryptocurrency")

class ApplePayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid ${amount:.2f} via Apple Pay")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid ${amount:.2f} via Bank Transfer")

# --- Context Class ---
class PaymentContext:
    def __init__(self):
        self.strategy = None
        self.method = None

    def set_strategy(self, strategy, method_name):
        self.strategy = strategy
        self.method = method_name

    def pay(self, amount):
        if self.strategy:
            self.strategy.pay(amount)
        else:
            raise Exception("No payment strategy set.")

# --- JSON Logger ---
def log_transaction(method, amount):
    log = {
        "method": method,
        "amount": amount,
        "timestamp": datetime.now().isoformat()
    }

    try:
        with open("payment_logs.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(log)

    with open("payment_logs.json", "w") as f:
        json.dump(data, f, indent=4)

# --- GUI ---
class PaymentApp:
    def __init__(self, master):
        self.master = master
        master.title("Payment Processing System")

        self.amount_label = ttk.Label(master, text="Enter amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry = ttk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.method_label = ttk.Label(master, text="Select payment method:")
        self.method_label.grid(row=1, column=0, padx=10, pady=10)

        self.methods = ["Credit Card", "PayPal", "Cryptocurrency", "Apple Pay", "Bank Transfer"]
        self.method_var = tk.StringVar()
        self.method_combo = ttk.Combobox(master, textvariable=self.method_var, values=self.methods, state="readonly")
        self.method_combo.grid(row=1, column=1, padx=10, pady=10)

        self.pay_button = ttk.Button(master, text="Pay", command=self.process_payment)
        self.pay_button.grid(row=2, column=0, columnspan=2, pady=20)

    def process_payment(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            return

        method = self.method_var.get()
        if not method:
            messagebox.showerror("Error", "Please select a payment method.")
            return

        strategy = None
        if method == "Credit Card":
            input_data = simpledialog.askstring("Credit Card", "Enter card number:")
            if not input_data:
                return
            strategy = CreditCardPayment()
        elif method == "PayPal":
            input_data = simpledialog.askstring("PayPal", "Enter PayPal email:")
            if not input_data:
                return
            strategy = PayPalPayment()
        elif method == "Cryptocurrency":
            input_data = simpledialog.askstring("Crypto", "Enter wallet address:")
            if not input_data:
                return
            strategy = CryptoPayment()
        elif method == "Apple Pay":
            input_data = simpledialog.askstring("Apple Pay", "Enter Apple Device ID:")
            if not input_data:
                return
            strategy = ApplePayPayment()
        elif method == "Bank Transfer":
            input_data = simpledialog.askstring("Bank Transfer", "Enter IBAN:")
            if not input_data:
                return
            strategy = BankTransferPayment()

        context = PaymentContext()
        context.set_strategy(strategy, method)
        context.pay(amount)

        log_transaction(method, amount)
        messagebox.showinfo("Success", f"✅ Payment of ${amount:.2f} via {method} completed and logged.")

# --- Launch GUI ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()

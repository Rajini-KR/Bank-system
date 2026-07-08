import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from bank import Bank


class BankGUI:
    def __init__(self, root):
        self.root = root
        self.bank = Bank()
        self.login()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    # ---------------- LOGIN ----------------
    def login(self):
        self.clear()
        self.root.title("Bank Login")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        frame = tk.Frame(self.root, bg="#f0f0f0")
        frame.pack(expand=True)

        tk.Label(frame, text="BANK LOGIN",
                 font=("Arial", 18, "bold"),
                 bg="#f0f0f0").pack(pady=10)

        tk.Label(frame, text="Username", bg="#f0f0f0").pack()
        u = tk.Entry(frame)
        u.pack(pady=5)

        tk.Label(frame, text="Password", bg="#f0f0f0").pack()
        p = tk.Entry(frame, show="*")
        p.pack(pady=5)

        def go():
            if u.get() == "admin" and p.get() == "admin123":
                self.menu()
            else:
                messagebox.showerror("Error", "Invalid Login")

        tk.Button(frame, text="Login", bg="green", fg="white",
                  width=15, command=go).pack(pady=15)

    # ---------------- MENU ----------------
    def menu(self):
        self.clear()
        self.root.title("Bank Dashboard")
        self.root.geometry("500x500")

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(frame, text="BANK DASHBOARD",
                 font=("Arial", 18, "bold")).pack(pady=10)

        buttons = [
            ("Create Account", self.create),
            ("Deposit", self.deposit),
            ("Withdraw", self.withdraw),
            ("Transfer", self.transfer),
            ("Balance", self.balance),
            ("View Accounts", self.view),
            ("Exit", self.root.destroy)
        ]

        for text, cmd in buttons:
            tk.Button(frame, text=text, width=25,
                      bg="lightblue", height=2,
                      command=cmd).pack(pady=5)

    # ---------------- FEATURES ----------------
    def create(self):
        n = simpledialog.askstring("Account", "Account No")
        name = simpledialog.askstring("Account", "Name")
        b = simpledialog.askfloat("Account", "Initial Balance")

        messagebox.showinfo(
            "Result",
            "Created" if self.bank.create_account(n, name, b) else "Exists"
        )

    def deposit(self):
        n = simpledialog.askstring("Deposit", "Account No")
        a = simpledialog.askfloat("Deposit", "Amount")

        messagebox.showinfo(
            "Result",
            "Success" if self.bank.deposit(n, a) else "Failed"
        )

    def withdraw(self):
        n = simpledialog.askstring("Withdraw", "Account No")
        a = simpledialog.askfloat("Withdraw", "Amount")

        messagebox.showinfo(
            "Result",
            "Success" if self.bank.withdraw(n, a) else "Failed"
        )

    def transfer(self):
        f = simpledialog.askstring("Transfer", "From Account")
        t = simpledialog.askstring("Transfer", "To Account")
        a = simpledialog.askfloat("Transfer", "Amount")

        messagebox.showinfo(
            "Result",
            "Success" if self.bank.transfer(f, t, a) else "Failed"
        )

    def balance(self):
        n = simpledialog.askstring("Balance", "Account No")
        bal = self.bank.balance(n)

        messagebox.showinfo("Balance", f"{bal}" if bal else "Not Found")

    def view(self):
        win = tk.Toplevel(self.root)
        win.title("Accounts")
        win.geometry("500x300")

        tv = ttk.Treeview(win, columns=("A", "N", "B"), show="headings")

        tv.heading("A", text="Account No")
        tv.heading("N", text="Name")
        tv.heading("B", text="Balance")

        tv.pack(fill="both", expand=True)

        for acc in self.bank.get_all_accounts():
            tv.insert("", "end", values=acc.get_details())
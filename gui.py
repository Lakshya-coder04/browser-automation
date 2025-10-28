import tkinter as tk
from tkinter import messagebox
from main import WebAutomation

class App:
    def __init__(self, root):
        #Setting window Title and frame 
        self.root = root
        self.root.title("Web Automation GUI")

        #setting up a login frame for Username and Password
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=15, pady=20)

        #Creating label and Input for Username 
        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, sticky='w')
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, sticky="ew")

        #Creating label and Input for Password
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky='w')
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky="ew")

        #FORM Submission Frame 
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=20, pady=10)

        #creating label and input for Full Name 
        tk.Label(self.form_frame, text="Full Name").grid(row=0, column=0, sticky='w')
        self.entry_fullname = tk.Entry(self.form_frame)
        self.entry_fullname.grid(row=0, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Email").grid(row=1, column=0, sticky='w')
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Current Address").grid(row=2, column=0, sticky='w')
        self.entry_current_Address = tk.Entry(self.form_frame)
        self.entry_current_Address.grid(row=2, column=1, sticky="ew")

        tk.Label(self.form_frame, text="Permanent Address").grid(row=3, column=0, sticky='w')
        self.entry_permanent_Address = tk.Entry(self.form_frame)
        self.entry_permanent_Address.grid(row=3, column=1, sticky="ew")

        # Create a frame for submit and close browser buttons
        self.button_frame = tk.Frame()
        self.button_frame.pack(padx=10, pady=10)

        tk.Button(self.button_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Close Browser", command=self.close_browser).grid(row=0, column=1, padx=5)


    def submit_data(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        full_name = self.entry_fullname.get()
        email = self.entry_email.get()
        current_address = self.entry_current_Address.get()
        permanent_address = self.entry_permanent_Address.get()

        self.web_automation = WebAutomation()
        self.web_automation.login(username, password)
        self.web_automation.fill_form(full_name, email, current_address, permanent_address)


    def close_browser(self):
        self.web_automation.close()
        messagebox.showinfo("Browser Close" ,"Submitted Successfully!")


root = tk.Tk()
app = App(root)
root.mainloop()

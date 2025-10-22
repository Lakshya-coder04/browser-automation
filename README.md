# 🧠 Project: Automated Web Interaction using Selenium

A Python-based automation tool that uses **Selenium WebDriver** to log in to a demo website, fill out a form, and download a file automatically.

This project demonstrates your skills in **browser automation**, **DOM manipulation**, and **secure credential handling** — ideal for showcasing on your developer portfolio.

---

## 🚀 Features

- 🔐 Secure login using environment variables  
- 🧭 Automated form filling on a demo website  
- 📥 Auto-downloads files to a local directory  
- ⚙️ Customizable Chrome browser options  
- 🧹 Clean and modular OOP structure  

---

## 🧩 Tech Stack

- **Language:** Python  
- **Automation Framework:** Selenium  
- **Environment Management:** python-dotenv  
- **Browser:** Google Chrome (via ChromeDriver)

---

## 📂 Project Structure

```
browser-automation/
│
├── chromedriver-win64/          # ChromeDriver executable
├── .env                         # Stores credentials (not pushed to GitHub)
├── main.py                      # Main automation script
└── README.md                    # Project documentation
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/Lakshya-coder04/browser-automation.git
cd browser-automation
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install Dependencies
```bash
pip install selenium python-dotenv
```

### 4️⃣ Set Up .env File
Create a `.env` file in the project root with the following:
```
USERNAME=your_username
PASSWORD=your_password
```

> ⚠️ **Never commit your .env file** — add it to `.gitignore` to keep credentials safe.

### 5️⃣ Download ChromeDriver
- Download the matching **ChromeDriver** version for your Chrome browser:  
  👉 https://chromedriver.chromium.org/downloads  
- Extract it to a folder (e.g. `chromedriver-win64/`)  
- Update the path in `main.py` if necessary:
  ```python
  service = Service('chromedriver-win64/chromedriver.exe')
  ```

---

## ▶️ Run the Automation
```bash
python main.py
```

The script will:
1. Open Chrome  
2. Navigate to [demoqa.com/login](https://demoqa.com/login)  
3. Log in with your credentials  
4. Fill a text box form  
5. Download a sample file  
6. Wait for user input before closing  

---

## 🧠 Learning Outcomes

- Automate repetitive browser tasks  
- Work with Selenium’s WebDriverWait and ExpectedConditions  
- Manage sensitive credentials with .env  
- Understand browser DOM interaction  
- Structure automation projects using classes and methods  

---

## 🛡️ Security Tips

- Always use .env for credentials  
- Add .env and __pycache__ to .gitignore  
- Use encrypted secrets if deploying on GitHub Actions  

---

## 💡 Future Improvements

- Add automated screenshots after each step  
- Integrate logging and error handling  
- Support for headless Chrome mode  
- Extend for real website workflows (login, scraping, form submissions)

---

## ✨ Author

**Lakshya Birla**  
🔗 [GitHub Profile](https://github.com/Lakshya-coder04)  

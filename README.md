# OrangeHRM Test Automation Suite

Automated UI testing framework for OrangeHRM using Selenium WebDriver and Python.

## 📋 Project Overview

This project implements a Page Object Model (POM) framework to automate testing of the OrangeHRM web application, covering login, PIM (Employee Management), and Admin functionalities.

## 🗂️ Project Structure

orangehrm-automation/
├── config/ # Configuration settings
├── data/ # Test data (JSON files)
├── pages/ # Page Object classes
├── reports/ # HTML reports and screenshots
├── tests/ # Test files
└── utils/ # Helper utilities


## ✅ Test Coverage

| Module | Tests |
|--------|-------|
| Login | Valid login, Invalid login |
| PIM | Add Employee, Search Employee, Delete Employee |
| Admin | Search by username, Verify user role, Verify user status |

## 🛠️ Tools & Technologies

- Python 3.x
- Selenium WebDriver
- pytest
- pytest-html
- pytest-ordering
- Page Object Model (POM)
- Data-driven testing (JSON)

## 🚀 How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest -v
```

### Run with HTML report
```bash
pytest -v --html=reports/report.html
```

### Run specific module
```bash
pytest tests/test_login.py -v
pytest tests/test_pim.py -v
pytest tests/test_admin.py -v
```

## 📊 Features

- **Page Object Model** — Separation of test logic and page interactions
- **Data-driven testing** — Test data stored in JSON files
- **HTML Reports** — Visual test reports generated automatically
- **Screenshots on failure** — Automatic screenshots when tests fail
- **Headless mode** — Configurable headless browser execution
- **Explicit Waits** — Reliable element interaction with WebDriverWait

## ⚠️ Notes

- Tests are run against the [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/) which is a **shared public environment**
- Test stability may vary due to data added by other users on the demo site
- For best results, run tests on a fresh OrangeHRM instance

## 👤 Author

MiaB77
# OrangeHRM Test Automation Suite

Automated UI testing framework for OrangeHRM using Selenium WebDriver and Python.

## 📋 Project Overview

This project implements a Page Object Model (POM) framework to automate testing of the OrangeHRM web application, covering Login, PIM (Employee Management), and Admin functionalities.

Built with industry best practices: data-driven testing, explicit waits, screenshot on failure, and configurable CI/CD-ready setup.

## 🗂️ Project Structure
orangehrm-automation/
├── config/ # Configuration settings (BASE_URL, HEADLESS mode)
├── data/ # JSON test data files
├── pages/ # Page Object classes (BasePage, LoginPage, PIMPage, AdminPage)
├── reports/ # HTML reports and screenshots
├── tests/ # Test files
└── utils/ # Helper utilities (data_loader)


## ✅ Test Coverage

| Module | Tests |
|--------|-------|
| Login | Valid login, Invalid login (3 scenarios) |
| PIM | Add Employee, Search Employee, Delete Employee |
| Admin | Search by username, Verify user role, Verify user status |

**Total: 13 parametrized test cases across 3 modules**

## 🛠️ Tools & Technologies

- **Python 3.x** — OOP, data-driven testing
- **Selenium WebDriver 4.x** — UI automation
- **pytest** — Test framework with parametrize
- **pytest-html** — Automated HTML reports
- **pytest-ordering** — Test execution order control
- **Page Object Model (POM)** — BasePage inheritance pattern
- **JSON** — External test data management

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

### Run in headless mode
Set `HEADLESS = True` in `config/settings.py`

## 📊 Key Features

- **Page Object Model** — Separation of test logic and page interactions
- **BasePage architecture** — Shared methods (click, enter_text, wait_for_element)
- **Data-driven testing** — JSON files with parametrized test scenarios
- **HTML Reports** — Auto-generated with pytest-html and --self-contained-html
- **Screenshot on failure** — Automatic capture saved to reports/screenshots/
- **Explicit Waits** — WebDriverWait with Expected Conditions throughout
- **Headless mode** — Configurable for CI/CD pipeline execution

## ⚠️ Notes

- Tests run against [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/) — a **shared public environment**
- Test stability may vary due to data added by other users on the demo site
- For best results, run tests on a fresh OrangeHRM instance

## 👤 Author

[MiaB77](https://github.com/MiaB77)

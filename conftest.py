import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import HEADLESS
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCREENSHOT_DIR = BASE_DIR / "reports" / "screenshots"


@pytest.fixture()
def driver():
    options = Options()

    if HEADLESS:
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        
        if driver:
            SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
            screenshot_path = SCREENSHOT_DIR / f"{item.name}.png"
            driver.save_screenshot(str(screenshot_path))
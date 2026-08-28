# UI tests against Selenoid 

🚀 Test automation project with **Python**, **Pytest**, **Selenium**, **Allure** and **Selenoid**.

---

### 🛠️ Setup

```bash
pip install -r requirements.txt
```
### 🧪 Running Tests
#### Local
```bash
pytest
```
#### Selenoid
```bash
pytest --selenoid
```
### ⚙️ Command Line Parameters
| Parameter | Default | Description |
|-----------|---------|-------------|
| `--selenoid` | `False` | Run tests in Selenoid (remote browser) |
| `--browser` | `chrome` | Browser: `chrome` or `firefox` |
| `--browser_version` | `151.0` | Browser version (for Selenoid) |
| `--headless` | `False` | Run in headless mode |
| `--window_width` | `1920` | Browser window width |
| `--window_height` | `1080` | Browser window height |
#### Examples
```bash
# Run with specific browser and version
pytest --selenoid --browser=chrome --browser_version=154.0

# Headless mode with custom window size
pytest --selenoid --headless --window_width=1366 --window_height=768

# Combine all parameters
pytest --selenoid --browser=chrome --browser_version=151.0 --headless --window_width=1920 --window_height=1080
```
### 📊 Allure Report
```bash
# Run tests with Allure results
pytest --alluredir=allure-results

# Generate and open Allure report
allure generate allure-results -o allure-report --clean
allure open allure-report
```
### 🔴 Watch tests in Selenoid
During test execution, open:
```bash
UI: https://selenoid.qa.guru/ui/
```
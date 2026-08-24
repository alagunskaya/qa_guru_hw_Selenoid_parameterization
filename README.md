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
# 🚀 Playwright RESTful Booker API Automation Framework

<div align="center">

### API Test Automation Framework using Playwright + Pytest

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square\&logo=python)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-API%20Testing-2EAD33?style=flat-square\&logo=playwright)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-Test%20Framework-0A9EDC?style=flat-square\&logo=pytest)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-FF6B6B?style=flat-square)](https://docs.qameta.io/allure/)
![API Tests](https://github.com/SahilSR81/playwright-restful-booker-api/actions/workflows/api_tests.yml/badge.svg)

</div>

---

# 📌 Overview

This project is a backend API automation framework built using **Playwright APIRequestContext**, **Pytest**, and **Python**.

The framework validates the RESTful Booker API through positive, negative, contract, and data-driven test scenarios while following reusable automation framework design principles and industry-standard testing practices.

### 🔗 API Under Test

https://restful-booker.herokuapp.com

---

# 🎯 Project Goals

* Learn API Automation using Playwright
* Implement CRUD API Testing
* Build a reusable automation framework architecture
* Implement Data-Driven Testing
* Perform Contract Testing using JSON Schema Validation
* Integrate Reporting and Logging
* Configure CI/CD using GitHub Actions

---

# ✨ Features

* ✅ Health Check API Testing
* ✅ Authentication API Testing
* ✅ Create Booking API Testing
* ✅ Update Booking API Testing
* ✅ Delete Booking API Testing
* ✅ Positive & Negative Test Coverage
* ✅ JSON Schema Validation
* ✅ Data-Driven Testing
* ✅ Pytest Fixtures
* ✅ Custom API Client
* ✅ Request & Response Logging
* ✅ Allure Reporting
* ✅ GitHub Actions CI/CD
* ✅ Parameterized Tests

---

# 🛠️ Tech Stack

| Tool                         | Purpose                  |
| ---------------------------- | ------------------------ |
| Python                       | Programming Language     |
| Playwright APIRequestContext | API Automation           |
| Pytest                       | Test Framework           |
| Allure                       | Reporting                |
| JSON Schema                  | Contract Validation      |
| GitHub Actions               | CI/CD                    |
| Logging                      | Debugging & Traceability |

---

# 📊 Test Coverage

| Module                 | Positive | Negative |
| ---------------------- | -------- | -------- |
| Health Check API       | ✅        | ✅        |
| Authentication API     | ✅        | ✅        |
| Create Booking API     | ✅        | ✅        |
| Update Booking API     | ✅        | ✅        |
| Delete Booking API     | ✅        | ✅        |
| JSON Schema Validation | ✅        | ✅        |
| Parameterized Testing  | ✅        | ✅        |

---

# 📁 Project Structure

```bash
playwright-restful-booker-api/
│
├── .github/
│   └── workflows/
│       └── api_tests.yml
│
├── data/
│   ├── auth_data.json
│   └── booking_data.json
│
├── schemas/
│   ├── auth_schema.json
│   ├── booking_schema.json
│   └── booking_list_schema.json
│
├── tests/
│   ├── test_health_check.py
│   ├── test_auth.py
│   ├── test_auth_parameterized.py
│   ├── test_create_booking.py
│   ├── test_create_booking_parameterized.py
│   ├── test_update_booking.py
│   ├── test_delete_booking.py
│   ├── test_invalid_booking_data.py
│   └── test_schema_validation.py
│
├── utils/
│   ├── api_client.py
│   ├── data_loader.py
│   ├── logger.py
│   └── schema_validator.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# 🏗️ Framework Architecture

```text
Test Cases
     │
     ▼
Pytest Fixtures
     │
     ▼
API Client
     │
     ▼
RESTful Booker API
     │
     ▼
Response Validation
     │
     ├── Assertions
     ├── Schema Validation
     ├── Logging
     └── Reporting
```

---

# ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/SahilSR81/playwright-restful-booker-api.git

cd playwright-restful-booker-api
```

### Create Virtual Environment

Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Tests

### Run Complete Suite

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_auth.py
```

### Run Verbose Execution

```bash
pytest -v
```

### Run Specific Test Case

```bash
pytest tests/test_auth.py::test_generate_token
```

---

# 📊 Allure Reports

### Generate Results

```bash
pytest
```

### Serve Report

```bash
allure serve reports/allure-results
```

### Generate Static Report

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

### Open Static Report

```bash
allure open reports/allure-report
```

---

# 📝 Logging

The framework supports:

* Request Logging
* Response Logging
* Status Code Logging
* Execution Summary Logging
* Pass/Fail Tracking

Example:

```text
POST REQUEST -> /auth

STATUS CODE -> 200

PASSED -> tests/test_auth.py::test_generate_token
```

---

# 🔄 CI/CD

GitHub Actions automatically:

* Installs dependencies
* Installs Playwright
* Executes the test suite
* Generates test results
* Validates framework stability on every code change

Workflow triggers on:

* Push
* Pull Request

---

# 📈 Latest Results

```text
Total Tests : 46

Passed      : 46

Failed      : 0

Pass Rate   : 100%
```

---

# 📚 Learning Outcomes

This project demonstrates:

* REST API Testing
* Authentication Testing
* CRUD Operations Testing
* Contract Testing
* JSON Schema Validation
* Data-Driven Testing
* Parameterized Testing
* Test Framework Design
* Reporting & Logging
* CI/CD Integration

---

# 📖 Learning Resources

The following resources helped me learn and build this framework:

### Playwright

* Playwright Python Documentation
  https://playwright.dev/python/

* Playwright API Testing Documentation
  https://playwright.dev/python/docs/api-testing

### Pytest

* Pytest Official Documentation
  https://docs.pytest.org/

### JSON Schema Validation

* JSON Schema Documentation
  https://json-schema.org/

* Python JSONSchema Library
  https://python-jsonschema.readthedocs.io/

### Allure Reporting

* Allure Framework Documentation
  https://docs.qameta.io/allure/

### GitHub Actions

* GitHub Actions Documentation
  https://docs.github.com/en/actions

### REST API Testing Practice

* RESTful Booker API
  https://restful-booker.herokuapp.com

* RESTful Booker GitHub Repository
  https://github.com/mwinteringham/restful-booker

### Python

* Python Official Documentation
  https://docs.python.org/3/

### Additional Learning

* Test Automation University (TAU)
  https://testautomationu.applitools.com/

* Ministry of Testing
  https://www.ministryoftesting.com/

* QA Community Discussions and Open-Source Projects on GitHub

---

# 🚀 Future Enhancements

* [ ] PATCH Booking API Coverage
* [ ] Environment Configuration Support
* [ ] Docker Integration
* [ ] Parallel Execution
* [ ] API Mocking
* [ ] Performance Testing

---


# 🤝 Contributing

Contributions, improvements, suggestions and feedback are welcome.

Fork the repository and create a pull request.

---

<div align="center">

## "Good tests verify functionality. Great tests provide confidence." 🚀

</div>

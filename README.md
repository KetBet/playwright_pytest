# playwright_pytest

Playwright + pytest testing framework. 
[Tested website](https://www.automationexercise.com)

[Test cases](https://www.automationexercise.com/test_cases)

## Requirements

- Python
- Allure Report

## Installation

1. Clone the repository to your local machine
  
2. Navigate into repo, install the required dependencies:
    ```
    python -m pip install --upgrade pip
    pip install pipenv
    pipenv install --system
    playwright install chromium
    pipenv install faker
    ```

## Run Playwrigth tests

- Run all set of tests:
  ```shell
  pytest
  ```

- Run one particular test:
  ```shell
  pytest -k <name of the test>
  ```

## Generate Allure report

- To open the report in your default web browser, run:
  ```shell
  allure serve reports
  ```

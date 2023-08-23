# api-testing
365scores QA Automation Engineer Technical Assignment

[Allure report](https://andrey-tretyakov.github.io/api-testing/)

**Setup**

```
git clone https://github.com/andrey-tretyakov/api-testing.git
cd api_testing

pip install virtualenv
virtualenv venv
venv\Scripts\activate or source venv/bin/activate

pip install -r requirements.txt
```

**Launch autotests**

```
python -m pytest --alluredir=./allure-results --retries 2

allure serve
```

# SQL Injection Demo 

This program demonstrates the basics of an SQL-injection. It shows how an injected input like `admin' OR '1'='1` can trick the program into gaining access.

## How To Run
Requirements:
- Python 3.8+
- Django

Steps:
1. Install Django:
	```bash
	pip install django
	```
2. Start the server:
	```bash
	python manage.py runserver
	```
3. Open your browser to: `http://127.0.0.1:8000/`
4. Try a normal login with:
	- Username: `admin`
	- Password: `s3cret`
5. Then try the injection example:
	- Username: `admin' OR '1'='1`
	- Password: `anything`
6. What to expect:
	- Normal login should report: "Regular login succeeded."
	- Injection should report: "Injection succeeded (bypassed login)."
7. Why it works in this demo:
	- The demo builds a fake query string and checks for `OR` in the input, which
	  makes the vulnerable check pass.

## Limitations 
- This tool is for educational use only and should not be used for securing or storing sensitive information
- This is not a real authentication check.
- This code does not secure real data and should not be used in production.

## Ethical Considerations
This project is for education only. It demonstrates a common vulnerability to help developers recognize and avoid this kind of issue. Do not use this code or the concepts here to access systems you do not own or have explicit permission to test.

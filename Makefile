deploy:
	sh deploy.sh
fmt:
	isort lambda_function.py && black lambda_function.py
source .env
pip install --platform manylinux2014_x86_64 --only-binary :all: -t package -r requirements.txt

cd package
zip -r ../function .

cd ..
zip function.zip .env lambda_function.py

aws s3 cp function.zip s3://${S3_BUCKET_NAME}/${LAMBDA_FUNCTION_NAME} --profile ${PROFILE}
aws lambda update-function-code --function-name ${LAMBDA_FUNCTION_NAME} --s3-bucket ${S3_BUCKET_NAME} --s3-key ${LAMBDA_FUNCTION_NAME} --profile ${PROFILE}

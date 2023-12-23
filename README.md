## Lambda Function Templete with Custom Library

### How To Use

1. Create Lambda Function by AWS Management Console / CLI.
2. Create `.env` file.

```
S3_BUCKET_NAME=
LAMBDA_FUNCTION_NAME=
PROFILE=
REGION=
COMMANDS_PATH=
```

3. Write required library to `requirements.txt`
4. Execute `sh deploy.sh`

FROM public.ecr.aws/lambda/python:3.11


COPY . .

RUN pip install --no-cache-dir -r requirements.txt


CMD ["main.lambda_handler"]

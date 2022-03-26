# Simple flask app to display env variable

## Dockerization

This is Dockerized simple Hello World Flask Application which responds with a message that is set up as an environment variable.

## CI/CD Pipeline

Developed a CI/CD pipeline(Github Actions) which would lint the python code and push the updated image to ECR.

## Deployment to ECS

workflow which would deploy the latest ECR image to ECS on Fargate, By updating AWS task-defination.json with the latest image.

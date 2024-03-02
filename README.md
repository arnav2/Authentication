# Authentication
Authentication app written in Python and Falcon (backend only). This will be put on a dockerfile and deployed on Kubernetes. It will also consist of a workflow to create both Python and Typescript SDK

# Developer Notes

## How to setup 

brew install openapi-generator

## To create a python client

Please replace your path for the yaml:

openapi-generator-cli generate -i path/to/authenticator.yaml -g python -o path/to/python-sdk

openapi-generator-cli generate -i path/to/authenticator.yaml -g typescript -o path/to/typescript-sdk

docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/petstore.yaml \
  -g go \
  -o /local/out/go
# Authentication
Authentication app written in Python and Falcon (backend only). This will be put on a dockerfile and deployed on Kubernetes. It will also consist of a workflow to create both Python and Typescript SDK. 

Python SDK will be used by the backend codebase.
Typescript SDK will be used by the frontend codebase. 

# Developer Notes

## How to setup 

brew install openapi-generator

## To create a python client

Please replace your path for the yaml:
<!-- TODO: SETUP A PYTHON_POST_PROCESS_FILE -->
openapi-generator generate -i path/to/authenticator.yaml -g python -o path/to/python-sdk
openapi-generator generate -i authenticator.yaml -g python -o python_sdk

openapi-generator generate -i path/to/authenticator.yaml -g typescript -o path/to/typescript-sdk

docker run --rm \
  -v ${PWD}:/local openapitools/openapi-generator-cli generate \
  -i /local/petstore.yaml \
  -g go \
  -o /local/out/go

  ### NOTE
  Adding the path of the folder to the PYTHONPATH for the .bashrc or .bash_profile or .zshrc would help

  export PYTHONPATH=/path/to/your/directory:$PYTHONPATH

  In this case we need to add the path to the authentication folder and the path to the SDK folder to the python path
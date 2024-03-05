# Authentication System

This authentication system is implemented in Python using the Falcon framework for the backend. It includes functionality for user authentication and will be containerized using Docker and deployed on Kubernetes. Additionally, the system provides workflows to generate both Python and Typescript SDKs.

## Developer Notes

### Setup Instructions

To build the Docker image for the authentication app:

```bash
docker build -t authentication-app .
```

To tag the Docker image for pushing to a Docker registry:

```bash
docker tag authentication-app:latest your-docker-registry/authentication-app:latest
```

To deploy the application on Kubernetes using a deployment YAML file for a specific stage (e.g., ALPHA):

For testing install minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-darwin-arm64
sudo install minikube-darwin-arm64 /usr/local/bin/minikube
```

```bash
kubectl apply -f deployment_ALPHA.yaml
```

To check the status of the deployed pods:

```bash
kubectl get pods
```

To expose the deployment as a LoadBalancer service:

```bash
kubectl expose deployment authentication-app --type=LoadBalancer --port=8000
```

### Developer Note

Adding the path of the folder to the PYTHONPATH environment variable can simplify module imports and execution. You can add the following line to your `.bashrc`, `.bash_profile`, or `.zshrc` file:

```bash
export PYTHONPATH=/path/to/your/directory:$PYTHONPATH
```

In this case, you need to add the path to the authentication folder and the path to the SDK folder to the PYTHONPATH. For example:

```bash
export PYTHONPATH=/path/to/authentication:/path/to/SDK:$PYTHONPATH
```

Replace `/path/to/your/directory`, `/path/to/authentication`, and `/path/to/SDK` with the actual paths to your directories.

---

This README provides clear instructions for building and deploying the authentication system using Docker and Kubernetes. Additionally, it includes helpful tips for setting up the development environment.
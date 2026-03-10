# Wisecow DevOps Deployment Project

## 📌 Project Overview

This project demonstrates the **containerization and deployment of the Wisecow application** using modern DevOps practices.
The application is packaged using Docker, deployed on a Kubernetes cluster, and integrated with a CI/CD pipeline using GitHub Actions.
Secure HTTPS communication is implemented using TLS.

The goal of this project is to simulate a **real-world DevOps workflow** from development to deployment.

---

# 🏗 Architecture

Developer pushes code to GitHub →
GitHub Actions builds Docker image →
Image pushed to DockerHub →
Kubernetes pulls the image →
Application deployed and exposed via Service and Ingress →
Users access the application via HTTPS.

---

# ⚙️ Tools & Technologies Used

| Tool           | Purpose                              |
| -------------- | ------------------------------------ |
| Docker         | Containerize the Wisecow application |
| DockerHub      | Store Docker images                  |
| Kubernetes     | Container orchestration platform     |
| Minikube       | Local Kubernetes cluster             |
| GitHub Actions | CI/CD automation                     |
| Nginx Ingress  | Traffic routing                      |
| TLS            | Secure HTTPS communication           |

---

# 📂 Project Structure

wisecow-devops-project

```
.
├── app.sh
├── Dockerfile
├── README.md
│
├── k8s
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
└── .github
    └── workflows
        └── deploy.yml
```

---

# 🐳 Dockerization

The application is containerized using Docker.

### Build Docker Image

```
docker build -t <dockerhub-username>/wisecow:latest .
```

### Run Container

```
docker run -p 4499:4499 <dockerhub-username>/wisecow:latest
```

Access application:

```
http://localhost:4499
```

---

# ☸ Kubernetes Deployment

The application is deployed to a Kubernetes cluster using Deployment and Service manifests.

### Apply Kubernetes Resources

```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check running pods:

```
kubectl get pods
```

Check services:

```
kubectl get svc
```

---

# 🔐 TLS Implementation

Secure communication is enabled using TLS with Kubernetes Ingress.

### Create TLS Secret

```
kubectl create secret tls wisecow-tls \
--cert=tls.crt \
--key=tls.key
```

### Apply Ingress

```
kubectl apply -f k8s/ingress.yaml
```

Now access the application securely via:

```
https://wisecow.local
```

---

# 🔄 CI/CD Pipeline (GitHub Actions)

A GitHub Actions workflow automates:

1. Docker image build
2. Push to DockerHub
3. Continuous deployment to Kubernetes

Workflow file:

```
.github/workflows/deploy.yml
```

Pipeline triggers automatically when code is pushed to the **main branch**.

---

# 🧪 Testing

Check pods:

```
kubectl get pods
```

Check service:

```
kubectl get svc
```

Access application:

```
minikube service wisecow-service
```

---

# ⚠️ Common Issues

### ImagePullBackOff

Check Docker image name and DockerHub access.

### Pod CrashLoopBackOff

Check pod logs:

```
kubectl logs <pod-name>
```

### Service Not Accessible

Verify NodePort or Ingress configuration.

---

# 📈 Key DevOps Concepts Demonstrated

* Containerization using Docker
* Kubernetes application deployment
* Service exposure
* CI/CD automation with GitHub Actions
* Secure TLS communication
* Infrastructure automation principles

---

# 🎯 End Goal

Successfully deploy the **Wisecow application** on Kubernetes with:

* Docker containerization
* Automated CI/CD pipeline
* Secure TLS communication

This project was developed as part of a **DevOps assignment to demonstrate containerization, orchestration, and automation skills**.

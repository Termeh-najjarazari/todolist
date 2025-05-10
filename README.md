# 📝 ToDo List Microservice with Kubernetes + Docker + GitHub Actions

A powerful Notion-style ToDo list application built with **Flask**, **SQLite**, and **TailwindCSS**, containerized with **Docker**, and deployed via **Kubernetes** on **Minikube**, with automated CI/CD using **GitHub Actions**.

---

## 🌟 Features

- ✅ Add, delete, and toggle tasks (done/undone)
- 🗂️ Category-based filtering
- 🎨 Elegant Notion-inspired UI using TailwindCSS
- 🗃️ Lightweight SQLite database (no external DB setup needed)
- 🐳 Dockerized for portability
- ☸️ Kubernetes deployment-ready
- 🔁 GitHub Actions for auto-build and Docker Hub push
- 🔍 Health check endpoint for probes

---

## 📁 Project Structure

```

todolist-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── .github/
│   └── workflows/
│       └── deploy.yml
├── templates/
│   └── index.html
└── static/
└── style.css

````

---

## 🚀 Quick Start (Local)

### 🔧 Prerequisites

- Python 3.9+
- Git
- Docker
- Minikube + kubectl (for Kubernetes)
- A [Docker Hub](https://hub.docker.com) account

### 🛠️ Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
````

App will run at: `http://localhost:5000`

---

## 🐳 Docker

### 🔨 Build Image

```bash
docker build -t 1termeh/todo-app .
```

### 🧪 Run Locally with Docker

```bash
docker run -p 5000:5000 1termeh/todo-app
```

---

## ☸️ Kubernetes (Minikube)

### ✅ Start Minikube

```bash
minikube start
```

### 📦 Deploy

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 🌐 Access Service

```bash
minikube service todo-service
```

---

## ⚙️ GitHub Actions (CI/CD)

This project is connected to GitHub Actions for automated Docker image builds and pushes to Docker Hub.

### 🛡️ Secret Setup in GitHub

Go to: `Settings → Secrets and variables → Actions`
Add the following secret:

| Name              | Description                  |
| ----------------- | ---------------------------- |
| `DOCKER_PASSWORD` | Your Docker Hub access token |

> Token can be generated at [Docker Hub → Account Settings → Security](https://hub.docker.com/settings/security)

### 🧾 Workflow File

Path: `.github/workflows/deploy.yml`

This workflow:

* Builds the Docker image
* Logs in to Docker Hub
* Pushes image `1termeh/todo-app:latest`

Trigger: Every push to `main` branch

---

## 🔁 Update & Push Script (optional)

To auto-push new changes and trigger CI/CD:

```bash
echo "# update $(date)" >> app.py
git add .
git commit -m "📦 Update"
git push origin main
```

---

## 🩺 Health Check

For liveness/readiness probes:

```http
GET /health
Response: 200 OK
```

---

## 📸 Screenshots

> *(Add your own UI screenshots here for better visualization)*

---

## 👤 Author

* GitHub: [Termeh-najjarazari](https://github.com/Termeh-najjarazari)

---

## 📃 License

MIT License

```

---


```

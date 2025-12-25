# FlaskDockNexus — Two-Tier Web Application 🚀

## 📌 Overview

FlaskDockNexus is a two-tier web application built with **Flask** and **MySQL**, designed to demonstrate core **DevOps fundamentals** such as containerization, service-to-service communication, and CI/CD automation using **Docker Compose** and **Jenkins**.

---

## 🏗️ Architecture

* **Web Tier:** Flask application running in a Docker container
* **Database Tier:** MySQL database running in a Docker container
* **Orchestration:** Docker Compose
* **CI/CD:** Jenkins Pipeline (automated build & deploy)

```
User → Flask Web App → MySQL Database
```

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** MySQL 8
* **Containers:** Docker, Docker Compose
* **CI/CD:** Jenkins
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
FlaskDockNexus/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── docker-compose.yml
├── Jenkinsfile
├── screenshots/
│   ├── app-running.png
│   ├── docker-running.png
│   └── jenkins-pipeline.png
└── README.md
|-Dockerfile
```

---

## 🔄 Application Workflow

1. Docker Compose starts the **Flask** and **MySQL** containers
2. Flask application reads database credentials via environment variables
3. Flask connects to the MySQL database container
4. Connection status is displayed on the UI
5. Jenkins pipeline automates build and deployment

---

## ⚙️ Run Locally

```bash
docker-compose up --build
```

Access the app:

```
http://localhost:5000
```

Expected output:

> **Database Connected Successfully ✓**

---

## 🤖 CI/CD with Jenkins

* Jenkins pulls the code from GitHub
* Builds Docker images
* Deploys containers using Docker Compose
* Enables automated deployment on every pipeline run

---

## 📸 Screenshots

<img width="1746" height="770" alt="app-running" src="https://github.com/user-attachments/assets/226383d6-5794-41d9-b338-52a93d880132" />



* Docker containers active
* <img width="1490" height="355" alt="docker-running" src="https://github.com/user-attachments/assets/a0c903c9-30f6-45e2-be24-91a05cb813d1" />

* Jenkins pipeline success

---

## 🚀 Outcome

* Successfully implemented a two-tier architecture
* Verified database connectivity between containers
* Automated deployment using Jenkins CI/CD pipeline
---
⭐ **Built by Rabiya Akram** 

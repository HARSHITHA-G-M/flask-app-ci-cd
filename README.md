# 🚀 Flask CI/CD Pipeline with Jenkins, Docker & Pytest

A complete CI/CD pipeline for a Flask web application using **Jenkins Freestyle Job**, **Docker**, **Pytest**, and **Docker Hub**.  
This project demonstrates automated testing, Docker image building, and pushing to Docker Hub with Jenkins.

---

## 📁 Project Structure

flask-app-ci-cd/
│
├── app/
│ ├── app.py # Main Flask app
│ └── init.py
│
├── test/
│ └── test_app.py # Pytest test cases
│
├── Dockerfile # Docker image build file
├── requirements.txt # Python dependencies
└── README.md


---

## 🛠️ Tools & Technologies

- **Python 3.12**
- **Flask 3.1**
- **Pytest** for unit testing
- **Jenkins** for CI/CD (Freestyle job)
- **Docker** for containerization
- **Docker Hub** for image registry
- **GitHub** for source version control

---

## 🔁 CI/CD Workflow

1. ✅ **Code pushed to GitHub**
2. 🔁 **Jenkins Freestyle Job** triggers:
   - Clone the repo
   - Create virtual environment & install requirements
   - Run tests with Pytest
3. 🐳 **Docker build & tag**
4. 🚀 **Docker push to Docker Hub**
5. ▶️ **Docker run** the container

---

## 🧪 Pytest Command

```bash
PYTHONPATH=. pytest test/

🐳 Docker Commands Used
# Build
docker build -t yourusername/flask-cicd-app .

# Login
docker login

# Push
docker push yourusername/flask-cicd-app

# Run
docker run -d -p 5000:5000 yourusername/flask-cicd-app


✅ Output
Jenkins builds and tests the Flask app.

If tests pass, it builds the Docker image and pushes it to Docker Hub.

Finally, the app is available to run via Docker.

🤝 Connect
Built by Harshitha

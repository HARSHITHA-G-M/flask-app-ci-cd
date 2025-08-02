# 🚀 Flask CI/CD Pipeline with Jenkins, Docker & Pytest

A complete CI/CD pipeline for a Flask web application using **Jenkins Freestyle Job**, **Docker**, **Pytest**, and **Docker Hub**.  
This project demonstrates automated testing, Docker image building, and pushing to Docker Hub with Jenkins.
![Buildpacks](https://img.shields.io/badge/Built%20With-Buildpacks-blue)

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


🚀 Cloud Native Buildpacks Integration
This project uses Cloud Native Buildpacks to build the Docker image for the Flask application without writing a Dockerfile.

✅ Why Buildpacks?
No Dockerfile needed
Auto-detects runtime and builds accordingly
Used by platforms like Heroku, Google Cloud Run, and Paketo
Automatically installs Python, Gunicorn, and dependencies

🔧 Buildpacks Used
Builder: gcr.io/buildpacks/builder:google-22
Runtime Detected: Python
Entrypoint: main.py or defined via Procfile / GOOGLE_ENTRYPOINT


🛠️ How to Build Using Buildpacks
cd app  # Make sure you're in the directory with main.py and requirements.txt
pack build flask-app --builder gcr.io/buildpacks/builder:google-22
Make sure pack CLI is installed: Install Pack CLI

🐳 Run the Built Image
docker run -p 5000:8080 flask-app
Then visit: http://localhost:5000

If tests pass, it builds the Docker image and pushes it to Docker Hub.
Finally, the app is available to run via Docker.

🤝 Connect
Built by Harshitha

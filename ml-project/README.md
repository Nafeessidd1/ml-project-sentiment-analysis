Sentiment Analysis ML Project 🎬

A complete end-to-end MLOps project that trains a sentiment analysis model and serves it through a web application. This application can classify movie reviews as positive or negative.

✨ Key Features
End-to-End ML Pipeline: Includes scripts for data processing, model training, and inference.

Deep Learning Model: Utilizes a PyTorch-based CNN for text classification.

API Backend: A robust backend built with FastAPI to serve the trained model.

Interactive Frontend: A user-friendly web interface created with Streamlit.

Containerized: Fully containerized with Docker for consistent deployment and scalability.

🛠️ Tech Stack
Language: Python 3.9

Backend: FastAPI, Uvicorn

Frontend: Streamlit

ML/DL: PyTorch, Pandas, Scikit-learn

Deployment: Docker, Colima

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
Git

Conda

Docker (or a lightweight alternative like Colima)

Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Create and activate the Conda environment:

Bash

./create_environment.sh
conda activate ml-project
Train the model:

Bash

python src/main.py --mode train
🖥️ Usage
To run the web application, you need to start the backend and frontend in two separate terminals.

Start the API Backend (in your first terminal):

Bash

uvicorn app.backend:app --host 127.0.0.1 --port 8000
Start the Streamlit Frontend (in a second terminal):

Bash

streamlit run app/Home.py
Open your browser and navigate to http://localhost:8501.

🐳 Docker Deployment
You can also run the entire application using Docker for a completely isolated environment.

Build the Docker image:

Bash

docker build -t sentiment-app .
Run the Docker container:

Bash

docker run -p 8000:8000 -p 8501:8501 sentiment-app
The application will be available at http://localhost:8501.
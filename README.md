🚀 Backend Developer Technical Assessment

📌 Overview

This project implements a simple data pipeline using Docker with three services:
	•	Flask API → Serves mock customer data from a JSON file
	•	FastAPI Service → Ingests data and stores it in PostgreSQL
	•	PostgreSQL → Stores customer records

🔄 Data Flow

Flask (Mock API) → FastAPI (Ingestion) → PostgreSQL → API Response

🛠️ Tech Stack
	•	Python 3.10
	•	Flask
	•	FastAPI
	•	SQLAlchemy
	•	PostgreSQL
	•	Docker & Docker Compose

📂 Project Structure

project-root/
├── docker-compose.yml
├── README.md
├── mock-server/
│   ├── app.py
│   ├── data/customers.json
│   ├── Dockerfile
│   └── requirements.txt
└── pipeline-service/
    ├── main.py
    ├── database.py
    ├── models/customer.py
    ├── services/ingestion.py
    ├── Dockerfile
    └── requirements.txt

🚀 Setup & Run

1. Start all services

docker-compose up --build

📡 Services

🔹 Flask Mock Server
	•	URL: http://localhost:5001
	•	Endpoints:
	•	GET /api/customers?page=1&limit=10
	•	GET /api/customers/{id}
	•	GET /api/health

🔹 FastAPI Pipeline Service
	•	URL: http://localhost:8000
	•	Endpoints:
	•	POST /api/ingest → Fetches data from Flask and stores in DB
	•	GET /api/customers?page=1&limit=10
	•	GET /api/customers/{id}

🧪 API Testing

1. Fetch customers from Flask

curl http://localhost:5001/api/customers?page=1&limit=5

2. Ingest data into PostgreSQL

curl -X POST http://localhost:8000/api/ingest

3. Fetch customers from database

curl http://localhost:8000/api/customers?page=1&limit=5


⚙️ Key Features
	•	JSON-based mock data (no hardcoding)
	•	Pagination support in Flask & FastAPI
	•	Automatic pagination handling during ingestion
	•	Upsert logic (insert/update)
	•	SQLAlchemy ORM for database operations
	•	Dockerized multi-service architecture
	•	Database connection retry handling

⚠️ Notes
	•	Flask runs on port 5001 (mapped from 5000 due to system port conflict)
	•	FastAPI communicates with Flask internally using Docker network (mock-server:5000)
	•	Database connection includes retry logic to handle startup delays

✅ Submission Checklist
	•	All services run using Docker Compose
	•	Flask API serves paginated data
	•	FastAPI ingests and stores data
	•	PostgreSQL integration working
	•	All endpoints functional

👨‍💻 Author
Priyanshu Shukla

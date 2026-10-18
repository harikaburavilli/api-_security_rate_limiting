# API Security and Rate Limiting

## Project Overview
This project demonstrates API security and rate limiting
using Python and FastAPI.

## Technologies Used
- Python
- FastAPI
- MySQL
- Uvicorn

## Features
- API key authentication
- Request rate limiting
- HTTP error handling
- API health-check endpoint
- MySQL connection module

## Project Files
- main.py: Main FastAPI application
- database.py: MySQL connection helper
- requirements.txt: Python dependencies
- README.md: Project documentation

## Installation

Install Python 3.10 or later.

Install the required packages:

    pip install -r requirements.txt

## Run the Application

    uvicorn main:app --reload

Open the API documentation in your browser:

    http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
| GET | / | Welcome message |
| GET | /health | Health check |
| GET | /secure | API-key authentication and rate limiting |

## Demo API Key

For local testing only:

    internship-demo-key

Do not use this demonstration key in production.

## Database Configuration

Set these environment variables before configuring
the MySQL database connection:

- DB_HOST
- DB_USER
- DB_PASSWORD
- DB_NAME

## Future Improvements
- Store API keys securely in a database
- Persist rate-limit data
- Add security monitoring and audit logs
- Add automated tests# api-_security_rate_limiting
python FastAPI project for API security and rate limiting

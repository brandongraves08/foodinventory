# MetaPantry AR

A food inventory management system that leverages Meta Quest's Passthrough feature and AI-driven services.

## Project Overview

MetaPantry AR is a two-part system:
1. Meta Quest AR Scanner (Frontend)
2. Food Inventory Backend (API + Database)

This repository contains the backend implementation for the food inventory system.

## Features

- RESTful API for food item management
- Barcode scanning and lookup
- Image analysis using OpenAI Vision API
- Food item tracking with expiration dates

## Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker
- **External APIs**: Open Food Facts API, OpenAI API

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker (optional)

### Installation

1. Clone the repository
```bash
git clone https://github.com/brandongraves08/foodinventory.git
cd foodinventory
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the application
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

MIT
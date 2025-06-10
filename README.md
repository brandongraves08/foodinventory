# MetaPantry AR

A food inventory management system that leverages both web technologies and Meta Quest's Passthrough feature with AI-driven services.

## Project Overview

MetaPantry AR is a multi-platform system:
1. Web Frontend (Browser-based interface)
2. Meta Quest AR Scanner (Augmented Reality interface)
3. Food Inventory Backend (API + Database)

This repository contains the complete implementation including the backend API and web frontend.

## Features

- User authentication and multi-user support
- Web interface for inventory management
- Meta Quest AR integration for immersive scanning
- RESTful API for food item management
- Barcode scanning and lookup
- Image analysis using OpenAI Vision API
- Food item tracking with expiration dates

## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Authentication**: OAuth2 with JWT
- **Containerization**: Docker
- **External APIs**: Open Food Facts API, OpenAI API

### Web Frontend
- **Framework**: React with TypeScript
- **UI Library**: Material-UI
- **State Management**: React Context API
- **API Client**: Axios
- **Routing**: React Router

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL
- Docker (optional)

### Backend Installation

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

4. Run database migrations
```bash
alembic upgrade head
```

5. Run the backend application
```bash
uvicorn app.main:app --reload
```

### Frontend Installation

1. Navigate to the frontend directory
```bash
cd frontend
```

2. Install dependencies
```bash
npm install
# or
yarn install
```

3. Start the development server
```bash
npm start
# or
yarn start
```

## Docker Deployment

You can also run the entire application using Docker:

```bash
docker-compose up -d
```

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Web Interface

The web interface will be available at:
- http://localhost:3000 (development)
- http://localhost:8000 (when deployed with Docker)

## License

MIT
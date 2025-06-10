# MetaPantry AR - System Architecture

## Overview

MetaPantry AR is a comprehensive food inventory management system that allows users to track their food items, expiration dates, and inventory levels. The system provides multiple interfaces for data input and management:

1. **Web Frontend** - Primary interface for desktop and mobile web users
2. **Meta Quest AR Scanner** - Augmented reality interface for scanning and managing inventory
3. **REST API** - Backend services that power all client applications

## System Components

### 1. Backend Services

The backend is built with FastAPI and provides the following services:

- **Authentication Service**: User registration, login, and token management
- **Food Item Service**: CRUD operations for food inventory items
- **Barcode Service**: Integration with Open Food Facts API for product lookup
- **Image Analysis Service**: AI-powered food recognition using OpenAI Vision API
- **Database**: PostgreSQL for persistent storage

### 2. Web Frontend

The web frontend is a responsive React application that provides:

- User authentication (login/register)
- Dashboard with expiration alerts and inventory overview
- Food item management (add, edit, delete)
- Barcode scanning via device camera
- Image upload and analysis
- Filtering and searching inventory

### 3. Meta Quest AR Scanner

The Meta Quest AR component provides an immersive way to interact with the inventory:

- Scan products in AR using the Meta Quest camera
- Voice commands for hands-free operation
- Visual overlays showing expiration dates and inventory information
- Gesture-based interaction for adding and managing items

## Data Flow

1. **Data Input**:
   - Web Frontend: Manual entry, barcode scanning via webcam, image upload
   - Meta Quest AR: Direct scanning in augmented reality environment

2. **Processing**:
   - All data is processed through the central API
   - Authentication and authorization checks
   - Data validation and normalization

3. **Storage**:
   - PostgreSQL database for structured data
   - File storage for images

4. **Retrieval**:
   - Real-time data access from both web and AR interfaces
   - Filtered views based on user preferences

## Technical Stack

### Backend
- FastAPI (Python)
- PostgreSQL
- SQLAlchemy ORM
- Alembic for migrations
- JWT authentication
- OpenAI Vision API
- Docker for containerization

### Web Frontend
- React with TypeScript
- Material-UI components
- Axios for API communication
- React Router for navigation
- PWA capabilities for mobile use

### Meta Quest AR
- Unity 3D
- Meta Quest SDK
- AR Foundation
- REST API integration

## Deployment Architecture

The system is deployed using a containerized approach:

- Docker containers for backend services
- PostgreSQL in a separate container or managed service
- Web frontend served via static hosting or CDN
- Meta Quest AR application distributed through Meta App Store

## Security Considerations

- JWT-based authentication
- HTTPS for all communications
- Data encryption at rest
- Role-based access control
- API rate limiting

## Future Enhancements

- Mobile native applications
- Integration with smart refrigerators
- Shopping list generation
- Recipe recommendations based on inventory
- Additional AR platforms support
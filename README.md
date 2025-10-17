# Eco-Loop

**A sustainable waste management platform connecting producers, consumers, and recyclers to promote circular economy practices.**

## Overview

Eco-Loop is a mobile application that facilitates waste recycling by connecting three key user groups:

- **Producers**: Businesses and individuals who generate recyclable waste
- **Consumers**: Individuals who want to responsibly dispose of their waste
- **Recyclers**: Companies that collect and process recyclable materials


## Features

### Core Features

- **Multi-Role Authentication**: Separate user experiences for Producers, Recyclers, and Consumers
- **AI-Powered Search**: Natural language waste description and intelligent matching
- **Marketplace**: Browse and connect with recyclers based on location, waste type, and pricing
- **Transaction Management**: Track waste collection from initiation to completion
- **Environmental Impact Tracking**: Monitor personal contributions (carbon reduction, waste recycled/reused, materials recovered)
- **Rewards System**: Earn points from transactions and redeem for eco-friendly products
- **Rating \& Reviews**: Rate and review recyclers based on service quality
- **Location-Based Matching**: Find nearby recyclers with distance and delivery estimates


### User-Specific Features

**For Producers \& Consumers:**

- Create waste listings with type, quantity, location, and pricing
- View waste by categories (PET, HDPE, PP, PS, Aluminum, Glass, Paper)
- Link directly with preferred buyers
- Track waste impact statistics

**For Recyclers:**

- Browse available waste listings with filtering options
- Manage collection schedules
- View materials recovered and carbon offset metrics
- Build reputation through reviews and ratings


### Premium Features

- Enhanced analytics and detailed environmental impact reports
- Priority listing visibility
- Ad-free experience


## Technology Stack

### Frontend

- **Framework**: Flutter
- **State Management**: Provider/Riverpod
- **HTTP Client**: Dio
- **Platforms**: iOS, Android


### Backend

- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: JWT
- **ORM**: SQLAlchemy


## Project Structure

```
eco-loop/
├── eco-loop-frontend/    # Flutter mobile app
└── eco-loop-backend/     # Python FastAPI server
```


## Getting Started

### Prerequisites

- Flutter SDK (latest stable)
- Python 3.9+
- PostgreSQL 13+


### Backend Setup

1. Navigate to backend directory:
```bash
cd eco-loop-backend
```

2. Install Poetry (if not installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

5. Run migrations and start server:
```bash
poetry shell
alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Add new packages:**

```bash
poetry add package-name              # Production
poetry add --group dev package-name  # Development only
```

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd eco-loop-frontend
```

2. Install dependencies:
```bash
flutter pub get
```

3. Update API endpoint in `lib/config/api_config.dart`:
```dart
static const String BASE_URL = "http://YOUR_LOCAL_IP:8000";
```

4. Run the app:
```bash
flutter run
```


## API Documentation

Once the backend is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Development Roadmap

### Month 1: Foundation

- Authentication system
- User profile management
- Basic marketplace functionality
- Transaction system


### Month 2: Advanced Features

- Payment gateway integration
- AI-powered recommendations
- Messaging system
- Rewards and points system


### Month 3: Polish \& Deployment

- Testing and bug fixes
- Performance optimization
- Security hardening
- Production deployment


## Environmental Impact

Eco-Loop helps users track their environmental contributions:

- **Carbon Reduction**: Measured CO2 offset from recycling activities
- **Waste Diverted**: Total weight of waste kept out of landfills
- **Materials Recovered**: Breakdown by material type (PET, Glass, Aluminum, etc.)


## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Acknowledgments

Built to promote sustainable waste management and support circular economy practices in local communities.

***

**Version**: 1.0.0 (Prototype)
**Last Updated**: October 2025


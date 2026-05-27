\# Ping Pong AI Point Counter



Real-time AI-powered ping pong game point counter using Azure ML and Computer Vision.



\## Project Overview



This project uses Microsoft Azure AI services to:

\- Detect ping pong ball position and trajectory

\- Identify player paddles and table surface

\- Automatically count points based on ITTF official rules

\- Track player scores by jersey color identification

\- Provide real-time score updates via web dashboard



\## Features



\- ✓ Real-time video analysis (30 FPS)

\- ✓ Ball, paddle, and table detection (YOLO v8)

\- ✓ Player identification by sportswear color

\- ✓ Automatic point scoring (ITTF rules)

\- ✓ Live score dashboard

\- ✓ Azure cloud deployment

\- ✓ WebSocket real-time updates



\## Tech Stack



\- \*\*Backend\*\*: FastAPI (Python)

\- \*\*ML Model\*\*: YOLO v8 / Azure Custom Vision

\- \*\*Video Processing\*\*: OpenCV

\- \*\*Cloud\*\*: Microsoft Azure

\- \*\*Real-time\*\*: Azure SignalR

\- \*\*Database\*\*: Azure Cosmos DB

\- \*\*Storage\*\*: Azure Blob Storage

\- \*\*Frontend\*\*: React.js / React Native

\- \*\*Containerization\*\*: Docker



\## Project Structure

pingpong-ai-counter/

├── src/ # Main application code

├── models/ # ML models

├── training/ # Training scripts

├── config/ # Configuration files

├── tests/ # Unit tests

├── notebooks/ # Jupyter notebooks

├── docs/ # Documentation

├── data/ # Data files (gitignored)

└── venv/ # Python virtual environment



\## Getting Started



\### Prerequisites

\- Python 3.10+

\- Azure Account

\- Docker (optional)



\### Installation



1\. Clone the repository:

```bash

git clone https://github.com/gierszewskibartosz-png/pingpong-ai-counter

cd pingpong-ai-counter





Create and activate virtual environment:

python -m venv venv

.\\venv\\Scripts\\activate.bat  # Windows

source venv/bin/activate     # Linux/Mac

Install dependencies:

pip install -r requirements.txt

Configure environment variables:

copy .env.example .env

\# Edit .env with your Azure credentials

Run the application:

python -m src.main

Usage

Training the Model

python -m training.train\_model --data-path ./data/training\_videos

Running Real-time Analysis

python -m src.main

Access dashboard at: http://localhost:8000



Architecture

Camera Feed (Laptop/iPhone)

&#x20;   ↓

Frame Extraction (OpenCV)

&#x20;   ↓

Object Detection (YOLO v8)

&#x20;   ↓

Ball Tracking \& Player ID

&#x20;   ↓

Rules Engine (ITTF)

&#x20;   ↓

Scoring Logic

&#x20;   ↓

Azure Cosmos DB

&#x20;   ↓

Real-time Dashboard (React)

Development Phases



Phase 1: Solution Design \& Architecture



Phase 2: Environment Setup



Phase 3: Training Data Preparation



Phase 4: Model Training \& Testing



Phase 5: Backend API Development



Phase 6: Frontend Dashboard



Phase 7: Azure Deployment



Phase 8: Testing \& Optimization

API Endpoints

GET /health - Health check

POST /api/video/stream - Video stream input

GET /api/score - Current game score

WebSocket /ws/scoreupdate - Real-time score updates

GET /api/game/stats - Game statistics

Configuration

See .env.example for configuration options.



Contributing

Contributions are welcome! Please follow these steps:



Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Create a Pull Request

License

This project is licensed under the MIT License - see LICENSE file for details.



Authors

Your Name / Organization

Support

For issues and questions, please open an issue on GitHub.



Acknowledgments

ITTF (International Table Tennis Federation) for official rules

Microsoft Azure for cloud services

OpenCV and YOLO communities

Project Status: 🚀 In Development



Last Updated: 2026-05-25


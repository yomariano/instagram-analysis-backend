# Instagram Analysis Backend API

FastAPI backend for Instagram audience demographics analysis using AI.

## Features

- **Instagram Scraping**: Automated data extraction with Apify
- **AI Demographics**: Gender and age classification using Google Gemini Flash
- **Async Processing**: Redis queue with RQ for job management
- **RESTful API**: FastAPI with automatic OpenAPI documentation
- **PostgreSQL**: Structured data storage

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Redis 7+
- Apify account
- Google Cloud account (Gemini API)

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Set environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Environment Variables

```env
DATABASE_URL=postgresql://user:pass@localhost/instagram_analysis
REDIS_URL=redis://localhost:6379
APIFY_TOKEN=your_apify_token
GEMINI_API_KEY=your_gemini_key
SECRET_KEY=your_jwt_secret
ALLOWED_ORIGINS=https://your-frontend-domain.com
```

### Running

```bash
# Start the API server
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

- `POST /api/v1/accounts` - Add Instagram account for analysis
- `GET /api/v1/accounts/{username}/analysis` - Get analysis results
- `GET /api/v1/accounts/{username}/demographics` - Get demographic breakdown
- `GET /health` - Health check endpoint

## Architecture

```
API Request → Apify Scraper → AI Analysis (Gemini) → PostgreSQL → Response
```

## Deployment

### Docker

```bash
docker build -t instagram-backend .
docker run -p 8000:8000 instagram-backend
```

### Coolify

1. Connect this repository to Coolify
2. Set all required environment variables
3. Configure health check on `/health`
4. Deploy with automatic builds

## Testing

```bash
pytest tests/
```

## License

MIT License
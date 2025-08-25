from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

app = FastAPI(
    title="Instagram Audience Analysis API",
    description="API for analyzing Instagram account demographics",
    version="1.0.0"
)

# CORS configuration
allowed_origins = os.getenv("CORS_ALLOWED_ORIGINS", "https://instagram-app.teabag.online,http://localhost:3000")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins.split(","),
    allow_credentials=False,  # Set to False for wildcard origins
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Add inline routes to avoid import issues
import uuid

@app.get("/api/v1/test")
async def test_endpoint():
    """Simple test endpoint"""
    return {"message": "API is working!", "status": "ok"}

@app.post("/api/v1/accounts")
async def add_instagram_account(account: dict):
    """Add an Instagram account for analysis"""
    try:
        username = account.get("username")
        if not username:
            raise HTTPException(status_code=400, detail="Username is required")
        
        # Generate job ID (simplified for now)
        job_id = str(uuid.uuid4())
        print(f"Analysis request for @{username}, job_id: {job_id}")
        
        return {"message": f"Analysis started for @{username}", "job_id": job_id}
    except Exception as e:
        print(f"Error in add_instagram_account: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/api/v1/accounts/{username}/demographics")
async def get_demographics(username: str):
    """Get demographic breakdown for account followers"""
    # Return mock demographic data
    return {
        "gender_split": {"male": 45, "female": 55},
        "age_distribution": {"18-24": 30, "25-34": 40, "35+": 30},
        "account_types": {"private": 60, "public": 40}
    }

# Custom exception handler to ensure CORS headers on errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    response = JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )
    
    # Add CORS headers to error responses
    origins = allowed_origins.split(",")
    origin = request.headers.get("origin")
    if origin and origin in origins:
        response.headers["Access-Control-Allow-Origin"] = origin
    elif "*" in origins:
        response.headers["Access-Control-Allow-Origin"] = "*"
    
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    
    return response

@app.get("/")
async def root():
    return {"message": "Instagram Audience Analysis API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
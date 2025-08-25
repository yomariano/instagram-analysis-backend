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

# Import routes after FastAPI app is created to avoid circular imports
try:
    from app.api.routes import router
    app.include_router(router, prefix="/api/v1")
except Exception as e:
    print(f"Error importing routes: {e}")
    # Add inline routes as fallback
    @app.get("/api/v1/test")
    async def test_endpoint():
        return {"message": "API is working!", "status": "ok"}

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
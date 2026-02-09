from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.task_router import router as task_router

# Create FastAPI app instance
app = FastAPI(
    title="Todo API",
    description="Backend API for the multi-user Todo application",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(task_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
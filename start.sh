#!/bin/bash

# Start script for running both frontend and backend together
# This script is designed for production deployment on Render

echo "🚀 Starting Portfolio Application..."

# Get the port from environment variable (Render provides this)
PORT=${PORT:-5000}

# Start backend with Gunicorn in the background
echo "📡 Starting backend API on port $PORT..."
gunicorn --chdir backend --bind 0.0.0.0:$PORT --workers 2 --timeout 30 wsgi:app &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 5

# Start frontend server (Nuxt 3 with Nitro)
echo "🌐 Starting frontend server..."

# Debug: Show current directory and contents
echo "Current directory: $(pwd)"
echo "Directory contents: $(ls -la)"

# Check if frontend directory exists
if [ ! -d "frontend" ]; then
    echo "❌ Frontend directory not found. Current location: $(pwd)"
    echo "Available directories: $(ls -d */)"
    kill $BACKEND_PID
    exit 1
fi

cd frontend

# Check if .output directory exists (Nuxt 3 build output)
if [ ! -d ".output" ]; then
    echo "❌ Frontend .output directory not found. Make sure to run build script first."
    echo "Frontend directory contents: $(ls -la)"
    kill $BACKEND_PID
    exit 1
fi

# Start the Nuxt Nitro server
PORT=3000 node .output/server/index.mjs &
FRONTEND_PID=$!

echo "✅ Application started!"
echo "📡 Backend API running on port $PORT"
echo "🌐 Frontend running on port 3000"
echo "🔄 Backend PID: $BACKEND_PID"
echo "🔄 Frontend PID: $FRONTEND_PID"

# Function to handle shutdown
cleanup() {
    echo "🛑 Shutting down..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Trap SIGTERM and SIGINT
trap cleanup SIGTERM SIGINT

# Wait for both processes
wait $BACKEND_PID
wait $FRONTEND_PID
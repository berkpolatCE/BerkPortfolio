#!/bin/bash

# Start script for running both frontend and backend together
# This script is designed for production deployment on Render

echo "🚀 Starting Portfolio Application..."

# Get the port from environment variable (Render provides this)
PORT=${PORT:-5000}

# Start backend on internal port 5000
echo "📡 Starting backend API on internal port 5000..."
gunicorn --chdir backend --bind 0.0.0.0:5000 --workers 2 --timeout 30 wsgi:app &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 5

# Start frontend server on the main PORT (Nuxt 3 with Nitro)
echo "🌐 Starting frontend server on port $PORT..."

# Check if frontend directory exists
if [ ! -d "frontend" ]; then
    echo "❌ Frontend directory not found."
    kill $BACKEND_PID
    exit 1
fi

# Check if .output directory exists (Nuxt 3 build output)
if [ ! -d "frontend/.output" ]; then
    echo "❌ Frontend .output directory not found. Make sure to run build script first."
    kill $BACKEND_PID
    exit 1
fi

# Start the Nuxt Nitro server on the main PORT
PORT=$PORT node frontend/.output/server/index.mjs &
FRONTEND_PID=$!

echo "✅ Application started!"
echo "📡 Backend API running on internal port 5000"
echo "🌐 Frontend running on main port $PORT"
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
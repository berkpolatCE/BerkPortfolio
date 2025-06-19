#!/bin/bash

# Start script for running both frontend and backend together
# This script is designed for production deployment on Render

echo "🚀 Starting Portfolio Application..."

# Get the port from environment variable (Render provides this)
PORT=${PORT:-5000}

# Start backend with Gunicorn in the background
echo "📡 Starting backend API on port $PORT..."
cd backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 --timeout 30 wsgi:app &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 5

# Start frontend build serving (for production)
echo "🌐 Starting frontend server..."
cd ../frontend

# Check if dist directory exists (should be built already)
if [ ! -d "dist" ]; then
    echo "❌ Frontend dist directory not found. Make sure to run build script first."
    kill $BACKEND_PID
    exit 1
fi

# Serve the built frontend using a simple HTTP server
# We'll use a Node.js static server that can handle SPA routing
npx serve dist -s -l 3000 &
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
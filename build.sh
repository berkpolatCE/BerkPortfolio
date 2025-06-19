#!/bin/bash

# Build script for preparing both frontend and backend for production
# This script is designed for Render deployment

echo "🔨 Building Portfolio Application for Production..."

# Build Backend
echo "📦 Installing backend dependencies..."
cd backend
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Backend dependency installation failed"
    exit 1
fi

echo "✅ Backend dependencies installed"

# Build Frontend  
echo "📦 Installing frontend dependencies..."
cd ../frontend
npm install

if [ $? -ne 0 ]; then
    echo "❌ Frontend dependency installation failed"
    exit 1
fi

echo "🔨 Building frontend for production..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Frontend build failed"
    exit 1
fi

echo "✅ Frontend built successfully"

# Install serve globally for serving the frontend
echo "📦 Installing serve for static file serving..."
npm install -g serve

if [ $? -ne 0 ]; then
    echo "❌ Failed to install serve"
    exit 1
fi

echo "✅ Build completed successfully!"
echo "📁 Frontend built to: frontend/.output/public/"
echo "🚀 Ready for deployment with ./start.sh"
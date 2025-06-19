# Portfolio Website

A modern, responsive portfolio website built with Nuxt 3 frontend and Flask backend, featuring smooth animations and a clean, minimalist design.

## 🚀 Features

- **Modern Tech Stack**: Nuxt 3 frontend with Flask REST API backend
- **Responsive Design**: Optimized for all device sizes
- **Smooth Animations**: GSAP-powered interactions and transitions
- **Auto-hiding Navigation**: Intelligent sidebar that appears on hover
- **Dark Theme**: Elegant dark color scheme with accent highlights
- **Particle Background**: Dynamic animated background
- **RESTful API**: Clean API endpoints for portfolio data
- **Production Ready**: Configured for deployment with Gunicorn

## 🛠️ Tech Stack

### Frontend
- **Nuxt 3** - Vue.js framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first styling
- **GSAP** - Animations and interactions
- **Vue Use** - Composition utilities

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Gunicorn** - WSGI HTTP server (production)
- **Python-dotenv** - Environment variable management

## 📁 Project Structure

```
BerkPortfolio/
├── frontend/                 # Nuxt 3 frontend application
│   ├── components/          # Vue components
│   ├── composables/         # Composable functions
│   ├── layouts/            # Layout components
│   ├── pages/              # Route pages
│   ├── public/             # Static assets
│   └── assets/             # Processed assets
├── backend/                 # Flask API backend
│   ├── routes/             # API route handlers
│   ├── data/               # Static data
│   ├── utils/              # Utility functions
│   └── app.py              # Flask application
└── README.md
```

## 🏃‍♂️ Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd BerkPortfolio
   ```

2. **Set up the backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up the frontend**
   ```bash
   cd frontend
   npm install
   ```

### Environment Configuration

1. **Backend Environment** (create `backend/.env`):
   ```env
   FLASK_HOST=127.0.0.1
   FLASK_PORT=5000
   FLASK_ENV=development
   FLASK_DEBUG=False
   SECRET_KEY=your-secret-key-here
   CORS_ORIGINS=http://localhost:3000
   ```

2. **Frontend Environment** (create `frontend/.env`):
   ```env
   NUXT_PUBLIC_API_BASE=http://localhost:5000/api/v1
   ```

### Development

1. **Start the backend server**
   ```bash
   cd backend
   python run.py
   ```

2. **Start the frontend development server**
   ```bash
   cd frontend
   npm run dev
   ```

Visit `http://localhost:3000` to view the application.

## 🚀 Production Deployment

### Using Gunicorn (Recommended)

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Create WSGI entry point** (`backend/wsgi.py`):
   ```python
   from app import app
   
   if __name__ == "__main__":
       app.run()
   ```

3. **Start with Gunicorn**
   ```bash
   cd backend
   gunicorn --config gunicorn.conf.py wsgi:app
   ```

### Environment Variables for Production

Set these environment variables in your production environment:

- `FLASK_ENV=production`
- `FLASK_DEBUG=False`
- `SECRET_KEY=<secure-random-key>`
- `CORS_ORIGINS=https://your-domain.com`
- `NUXT_PUBLIC_API_BASE=https://your-api-domain.com/api/v1`

## 📡 API Endpoints

- `GET /api/health` - Health check
- `GET /api/v1/home` - Home page data
- `GET /api/v1/projects` - All projects
- `GET /api/v1/projects/{id}` - Specific project
- `GET /api/v1/skills` - All skills
- `GET /api/v1/skills/{category}` - Skills by category
- `GET /api/v1/contact` - Contact information
- `GET /api/v1/photo` - Photo gallery

## 🎨 Customization

### Portfolio Data

Edit `backend/data/portfolio_data.py` to customize:
- Personal information
- Projects
- Skills
- Contact details

### Styling

The project uses Tailwind CSS with a custom theme. Main colors can be adjusted in `frontend/assets/css/main.css`.

### Logo

Replace `frontend/public/images/SOCRadar-Logo-white.png-1.webp` with your own logo.

## 🔧 Development Commands

### Frontend
```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run linter
```

### Backend
```bash
python run.py        # Start development server
python app.py        # Alternative start method
```

## 🐛 Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure `CORS_ORIGINS` is set correctly in backend environment
2. **API Connection**: Verify `NUXT_PUBLIC_API_BASE` matches your backend URL
3. **Port Conflicts**: Change ports in environment variables if needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using Nuxt 3 and Flask**
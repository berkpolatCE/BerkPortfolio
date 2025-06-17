# TODO - Portfolio Website Development

## Current Status
- [x] Flask backend API created with versioned endpoints
- [x] Hardcoded portfolio data structure
- [x] CORS enabled for frontend communication
- [ ] Nuxt.js frontend development
- [ ] Production deployment

## Backend Tasks
- [ ] Update `portfolio_data.py` with your actual information:
  - [ ] Personal details (name, title, about section)
  - [ ] Real project data with descriptions and links
  - [ ] Actual skills and proficiency levels
  - [ ] Contact information and social media links
  - [ ] Upload CV file to `backend/static/files/cv.pdf`
- [ ] Add profile and project images to `backend/static/images/`
- [ ] Test all API endpoints thoroughly
- [ ] Add environment variables for sensitive data

## Frontend Development (Nuxt.js)

### 1. Setup Nuxt.js Project
```bash
cd frontend
npx nuxi@latest init .
# Choose your preferred options during setup

# Install additional dependencies
npm install @nuxtjs/tailwindcss @nuxt/image axios @pinia/nuxt
```

### 2. Configure Nuxt for API Communication
Create `nuxt.config.ts`:
```typescript
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', '@nuxt/image', '@pinia/nuxt'],
  runtimeConfig: {
    public: {
      apiBase: process.env.API_BASE_URL || 'http://localhost:5000/api/v1'
    }
  },
  ssr: true, // Enable SSR for better SEO
})
```

### 3. Create API Composables
Create `composables/useApi.ts`:
```typescript
export const useApi = () => {
  const config = useRuntimeConfig()
  
  const fetchData = async (endpoint: string) => {
    const { data } = await $fetch(`${config.public.apiBase}${endpoint}`)
    return data
  }
  
  return {
    getHome: () => fetchData('/home'),
    getProjects: (featured?: boolean) => 
      fetchData(`/projects${featured ? '?featured=true' : ''}`),
    getProject: (id: number) => fetchData(`/projects/${id}`),
    getSkills: () => fetchData('/skills'),
    getPhoto: () => fetchData('/photo'),
    getContact: () => fetchData('/contact'),
    getCv: () => fetchData('/cv'),
  }
}
```

### 4. Page Structure
```
frontend/
├── pages/
│   ├── index.vue          # Home page
│   ├── projects/
│   │   ├── index.vue      # Projects listing
│   │   └── [id].vue       # Individual project
│   ├── skills.vue         # Skills page
│   └── contact.vue        # Contact page
├── components/
│   ├── NavBar.vue
│   ├── HeroSection.vue
│   ├── ProjectCard.vue
│   ├── SkillBar.vue
│   └── Footer.vue
└── layouts/
    └── default.vue
```

### 5. Example Page Implementation
```vue
<!-- pages/index.vue -->
<template>
  <div>
    <HeroSection :data="homeData" />
    <ProjectsSection :projects="featuredProjects" />
    <SkillsPreview :skills="skillsData" />
  </div>
</template>

<script setup>
const api = useApi()
const { data: homeData } = await useAsyncData('home', () => api.getHome())
const { data: featuredProjects } = await useAsyncData(
  'featured-projects', 
  () => api.getProjects(true)
)
const { data: skillsData } = await useAsyncData('skills', () => api.getSkills())
</script>
```

## Production Preparation

### 1. Environment Configuration
Create `.env` files:
```bash
# Backend (.env)
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
CORS_ORIGINS=https://yourdomain.com

# Frontend (.env)
API_BASE_URL=https://api.yourdomain.com/api/v1
```

### 2. Backend Production Setup
- [ ] Disable debug mode in production
- [ ] Use production WSGI server (Gunicorn)
- [ ] Set specific CORS origins (not all)
- [ ] Add rate limiting
- [ ] Implement logging
- [ ] Add SSL/HTTPS support

Update `backend/config.py`:
```python
import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
```

### 3. Frontend Production Build
```bash
cd frontend
npm run build
npm run preview  # Test production build locally
```

### 4. Security Checklist
- [ ] Remove all debug statements
- [ ] Secure sensitive endpoints
- [ ] Validate all inputs
- [ ] Set secure headers
- [ ] Enable HTTPS only
- [ ] Remove default secret keys
- [ ] Sanitize error messages

## Deployment Options

### Option 1: Traditional VPS (DigitalOcean, Linode, etc.)
```bash
# Backend deployment
- Install Python, nginx, supervisor
- Clone repository
- Setup virtual environment
- Configure Gunicorn with supervisor
- Setup nginx reverse proxy
- Configure SSL with Let's Encrypt

# Frontend deployment
- Build Nuxt app
- Serve with PM2 or nginx
- Configure nginx for SSR
```

### Option 2: Platform-as-a-Service

#### Backend (Render, Railway, Fly.io)
1. Create `Procfile`:
   ```
   web: gunicorn backend.app:app
   ```
2. Add `runtime.txt`:
   ```
   python-3.11.0
   ```
3. Deploy via Git

#### Frontend (Vercel, Netlify)
1. Connect GitHub repository
2. Set build command: `npm run build`
3. Set environment variables
4. Deploy

### Option 3: Containerized (Docker)

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
  
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - API_BASE_URL=http://backend:5000/api/v1
```

## Pre-deployment Checklist

### Backend
- [ ] Update all placeholder data in `portfolio_data.py`
- [ ] Add actual CV file
- [ ] Add project screenshots/images
- [ ] Test all endpoints with production data
- [ ] Remove or secure debug endpoints
- [ ] Configure production logging
- [ ] Set up error monitoring (Sentry)

### Frontend
- [ ] Implement responsive design
- [ ] Add meta tags for SEO
- [ ] Optimize images
- [ ] Add loading states
- [ ] Implement error boundaries
- [ ] Add analytics (Google Analytics, etc.)
- [ ] Test on multiple devices/browsers

### General
- [ ] Create production branch
- [ ] Set up CI/CD pipeline
- [ ] Configure domain and SSL
- [ ] Set up monitoring and alerts
- [ ] Create backup strategy
- [ ] Document deployment process

## Development Commands Reference

```bash
# Backend
cd backend
source venv/bin/activate
python run.py

# Frontend (after setup)
cd frontend
npm run dev

# Run both with tmux or multiple terminals
```

## API Endpoints Reference
- Health: `GET /api/health`
- Home: `GET /api/v1/home`
- Projects: `GET /api/v1/projects`
- Skills: `GET /api/v1/skills`
- Photo: `GET /api/v1/photo`
- Contact: `GET /api/v1/contact`
- CV: `GET /api/v1/cv`

## Notes
- Keep backend and frontend in same repository for easier deployment
- Use environment variables for all configuration
- Implement proper error handling on both ends
- Consider adding authentication if needed for admin features
- Monitor API usage and implement rate limiting if necessary
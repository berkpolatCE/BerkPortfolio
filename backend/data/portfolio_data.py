# Consolidated portfolio data - single source of truth

PORTFOLIO_DATA = {
    "home": {
        "name": "Your Name",
        "title": "Full Stack Developer",
        "about": "Passionate developer with expertise in creating modern web applications. "
                 "I enjoy solving complex problems and building scalable solutions.",
        "image_url": "/static/images/profile.jpg",
        "location": "Your City, Country",
        "languages": ["English", "Other Language"],
        "interests": ["Web Development", "Machine Learning", "Open Source"]
    },
    "photo": {
        "profile_photo": "/static/images/profile.jpg",
        "gallery": [
            {
                "id": 1,
                "url": "/static/images/photo1.jpg",
                "caption": "Project showcase",
                "date": "2024-01"
            },
            {
                "id": 2,
                "url": "/static/images/photo2.jpg",
                "caption": "Team collaboration",
                "date": "2024-02"
            }
        ]
    },
    "projects": [
        {
            "id": 1,
            "title": "E-commerce Platform",
            "description": "A full-stack e-commerce solution built with React and Node.js",
            "technologies": ["React", "Node.js", "MongoDB", "Stripe API"],
            "github_url": "https://github.com/yourusername/project1",
            "live_url": "https://project1.example.com",
            "image": "/static/images/project1.jpg",
            "featured": True
        },
        {
            "id": 2,
            "title": "Task Management App",
            "description": "A collaborative task management tool with real-time updates",
            "technologies": ["Vue.js", "Express", "PostgreSQL", "Socket.io"],
            "github_url": "https://github.com/yourusername/project2",
            "live_url": None,
            "image": "/static/images/project2.jpg",
            "featured": True
        },
        {
            "id": 3,
            "title": "Weather Dashboard",
            "description": "Real-time weather monitoring dashboard with data visualization",
            "technologies": ["Python", "Flask", "Chart.js", "OpenWeather API"],
            "github_url": "https://github.com/yourusername/project3",
            "live_url": "https://project3.example.com",
            "image": "/static/images/project3.jpg",
            "featured": False
        }
    ],
    "skills": {
        "technical": {
            "languages": [
                {"name": "Python", "level": "90%"},
                {"name": "JavaScript", "level": "85%"},
                {"name": "TypeScript", "level": "80%"},
                {"name": "Java", "level": "75%"}
            ],
            "frontend": [
                {"name": "React", "level": "85%"},
                {"name": "Vue.js", "level": "80%"},
                {"name": "HTML/CSS", "level": "90%"},
                {"name": "Tailwind CSS", "level": "85%"}
            ],
            "backend": [
                {"name": "Node.js", "level": "85%"},
                {"name": "Flask", "level": "90%"},
                {"name": "Django", "level": "80%"},
                {"name": "Express", "level": "85%"}
            ],
            "databases": [
                {"name": "PostgreSQL", "level": "85%"},
                {"name": "MongoDB", "level": "80%"},
                {"name": "Redis", "level": "75%"},
                {"name": "MySQL", "level": "80%"}
            ],
            "tools": [
                {"name": "Git", "level": "90%"},
                {"name": "Docker", "level": "80%"},
                {"name": "AWS", "level": "75%"},
                {"name": "CI/CD", "level": "80%"}
            ]
        },
        "soft": [
            "Problem Solving",
            "Team Collaboration",
            "Communication",
            "Project Management",
            "Agile Methodologies"
        ]
    },
    "cv": {
        "filename": "YourName_CV.pdf",
        "url": "/static/files/cv.pdf",
        "last_updated": "2024-03-01"
    },
    "contact": {
        "email": "your.email@example.com",
        "phone": "+1 234 567 8900",
        "linkedin": "https://linkedin.com/in/yourusername",
        "github": "https://github.com/yourusername",
        "twitter": "https://twitter.com/yourusername",
        "instagram": "https://instagram.com/yourusername",
        "availability": "Open to opportunities"
    }
}
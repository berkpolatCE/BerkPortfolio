# Consolidated portfolio data - single source of truth

PORTFOLIO_DATA = {
    "home": {
        "name": "Berk Polat",
        "title": "Computer Engineering Student",
        "about": "A dedicated and passionate Computer Engineering student currently in the third year at Istanbul Okan University. "
                 "Possesses advanced proficiency in C++ and Python, with intermediate skills in Java and Lua. "
                 "Specializes in cybersecurity, actively engaging in practical learning and challenges on Hack The Box to enhance hands-on experience. "
                 "Demonstrates advanced knowledge of both Linux and Windows operating systems. "
                 "Eager to apply technical expertise and problem-solving skills in cybersecurity and software development roles.",
        "image_url": "/images/profile.jpg",
        "location": "Kartal, Istanbul, Turkey",
        "languages": ["Turkish (Native)", "English (C1, 8.0 IELTS)"],
        "interests": ["Web Application Security", "Network Enumeration", "Penetration Testing", "Vulnerability Assessment", "Cybersecurity Research"],
    },
    "photo": {
        "profile_photo": "/images/profile.jpg",
        "gallery": [
            {
                "id": 1,
                "url": "/images/photo1.jpg",
                "caption": "Project showcase",
                "date": "2024-01"
            },
            {
                "id": 2,
                "url": "/images/photo2.jpg",
                "caption": "Team collaboration",
                "date": "2024-02"
            }
        ]
    },
    "projects": [
        {
            "id": 1,
            "title": "BZTyping",
            "description": "BZTyping is a powerful, customizable speech-to-text application that converts your spoken words into typed text in real-time.",
            "technologies": ["OpenAI Whisper", "PyQT5"],
            "github_url": "https://github.com/berkpolatCE/BZTyping",
            "live_url": None,
            "image": "/images/project1.jpg",
            "featured": True
        },
        {
            "id": 2,
            "title": "Task Management App",
            "description": "A collaborative task management tool with real-time updates",
            "technologies": ["Vue.js", "Express", "PostgreSQL", "Socket.io"],
            "github_url": "https://github.com/yourusername/project2",
            "live_url": None,
            "image": "/images/project2.jpg",
            "featured": True
        },
        {
            "id": 3,
            "title": "Weather Dashboard",
            "description": "Real-time weather monitoring dashboard with data visualization",
            "technologies": ["Python", "Flask", "Chart.js", "OpenWeather API"],
            "github_url": "https://github.com/yourusername/project3",
            "live_url": "https://project3.example.com",
            "image": "/images/project3.jpg",
            "featured": False
        }
    ],
    "skills": {
        "technical": {
            "languages": [
                {"name": "C++", "level": "90%"},
                {"name": "Python", "level": "90%"},
                {"name": "Java", "level": "70%"},
                {"name": "Lua", "level": "70%"}
            ],
            "frontend": [
                {"name": "Nuxt.js", "level": "80%"},
                {"name": "Vue.js", "level": "80%"},
                {"name": "Tailwind CSS", "level": "85%"},
                {"name": "GSAP", "level": "75%"}
            ],
            "backend": [
                {"name": "Python", "level": "90%"},
                {"name": "Flask", "level": "85%"}
            ],
            "cybersecurity": [
                {"name": "Web Application Penetration Testing", "level": "85%"},
                {"name": "Network Penetration Testing", "level": "80%"},
                {"name": "Reverse Engineering", "level": "70%"},
                {"name": "Threat Intelligence", "level": "75%"},
                {"name": "DFIR (Digital Forensics & Incident Response)", "level": "70%"}
            ],
            "tools": [
                {"name": "Git", "level": "85%"},
                {"name": "Linux", "level": "90%"},
                {"name": "Windows", "level": "90%"},
                {"name": "Nmap", "level": "80%"},
                {"name": "Metasploit", "level": "75%"},
                {"name": "SQLMap", "level": "75%"},
                {"name": "Burp Suite", "level": "70%"}
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
        "url": "/files/cv.pdf",
        "last_updated": "2024-03-01"
    },
    "contact": {
        "email": "berkpolat@gmail.com",
        "linkedin": "https://linkedin.com/in/berkpolat",
        "github": "https://github.com/berkpolatCE",
        "availability": "Interning at SOCRadar"
    }
}
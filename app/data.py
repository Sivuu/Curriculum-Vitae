"""
📝 WEBSITE DATA FILE - ALL CONTENT STORED HERE
You only need to modify dictionaries in this file to change entire website content
No need to edit any html files
"""

# ==============================
# ✅ PERSONAL INFORMATION
# ==============================
personal_info = {
    "name": "Industrial Automation Engineer",
    "title": "Engineer & Developer",
    "slogan": "Specialist in Robotic AMR, Industrial Sensors, Industrial Communication and PLC Automation",
    "description": "Design, develop and deploy modern automation solutions for Smart Factory 4.0. Focus on building flexible, efficient and intelligent automation systems.",
    "experience_years": "10+",
    "projects_done": "20+",
    "technologies": "8+",
    "skills": [
        {
            "icon": "fa-android",
            "color": "accent",
            "name": "Robotic AMR Systems/ ARM Robot Systems FANUC, Yaskawa.",
            "description": "Design, operation and programming of autonomous mobile robots in factory environments."
        },
        {
            "icon": "fa-rss",
            "color": "tech",
            "name": "Industrial Sensors",
            "description": "Integration and data processing from various industrial sensor types."
        },
        {
            "icon": "fa-exchange",
            "color": "green-500",
            "name": "Industrial Communication",
            "description": "Profinet, Modbus, OPC UA, EtherNet/IP and other communication protocols."
        },
        {
            "icon": "fa-microchip",
            "color": "orange-500",
            "name": "PLC & HMI",
            "description": "PLC Programming/Setting JTEKT, Mitsubishi, Omron and HMI."
        }
    ]
}

# ==============================
# ✅ EDUCATION & CERTIFICATIONS
# ==============================
education_timeline = [
    {
        "year": "2009",
        "color": "accent",
        "side": "left",
        "title": "Microsoft Certified Systems Administrator (MCSA)",
        "organization": "MCSA Certification - Microsoft",
        "description": "Specialized in Windows Server environments and network administration."
    },
    {
        "year": "2011",
        "color": "tech",
        "side": "right",
        "title": "Cisco Certified Network Associate (CCNA)",
        "organization": "CISCO Systems",
        "description": "Specialized in network fundamentals, IP connectivity, and security protocols."
    },
    {
        "year": "2016",
        "color": "accent",
        "side": "left",
        "title": "Barchelor of Information Technology",
        "organization": "Binh Duong University",
        "description": "Comprehensive education in IT fundamentals, programming, database management and network administration."
    },
    {
        "year": "2022",
        "color": "green-500",
        "side": "right",
        "title": "Electric shock prevention (V22 感09254)",
        "organization": "Toyota Motor Corporation",
        "description": "Training on electric shock prevention and safety protocols in industrial environments."
    },
    {
        "year": "2022",
        "color": "green-500",
        "side": "left",
        "title": "Low-voltage electrical work (LE22049)",
        "organization": "Toyota Motor Corporation",
        "description": "Certification for performing low-voltage electrical work safely and effectively in industrial settings."
    },
    {
        "year": "2024",
        "color": "green-500",
        "side": "right",
        "title": "Working at heights (V24 高12537)",
        "organization": "Toyota Motor Corporation",
        "description": "Certification for safely performing work at heights, including fall prevention and rescue procedures in industrial environments."
    }

]

# ==============================
# ✅ CAREER & COMPANIES
# ==============================
career_timeline = [
    {
        "year": "2012 - 2016",
        "color": "accent",
        "side": "left",
        "position": "IT Helpdesk",
        "company": "YUENFOONGYU BINH DUONG Co., Ltd.",
        "tasks": [
            "✅ IT system maintenance and support for 80+ employees",
            "✅ AutoCAD and designing software support for engineering team",
            "✅ Network setup and troubleshooting for office and factory",
            "✅ System administration of Windows Server and Linux servers"
        ]
    },
    {
        "year": "2016 - 2019",
        "color": "tech",
        "side": "right",
        "position": "IT Helpdesk",
        "company": "VINASOY BINH DUONG Co., Ltd.",
        "tasks": [
            "✅ IT system maintenance and support for 115+ employees",
            "✅ PLC setting and support for factory automation systems",
            "✅ SAP HANA system support for finance and logistics departments",
            "✅ Networking setup and troubleshooting for office and factory",
            "✅ Developing a time attendance system using face ID.",
        ]
    },
    {
        "year": "2019 - 2022",
        "color": "tech",
        "side": "left",
        "position": "Database and Software Engineer",
        "company": "Expert Software Japan Co., Ltd.",
        "tasks": [
            "✅ Developed C# and Python systems for PLC/SCADA data management and sensor reporting",
            "✅ Engineered internal web systems and managed corporate IT infrastructure.",
            "✅ Provided technical troubleshooting and maintenance for deployed products at client offices.",
            "✅ Designed and administered databases for insurance information and policy records."
        ]
    },
    {
        "year": "2022 - Present",
        "color": "tech",
        "side": "right",
        "position": "Automation Engineer",
        "company": "LUMI JAPAN Co., Ltd.",
        "tasks": [
            "✅ ADAS Validation System Development: Designed a QR-based testing framework for Toyota vehicle performance validation.",
            "✅ Forklift & AGV Management System: Developed software to manage coordinates, navigation settings, and real-time activity logging.",
            "✅ IoT & Network Architecture: Engineered real-time synchronization between PLC, PC servers, and WiFi networks.",
            "✅ Industrial Automation Programming: Created control scripts and vision processing modules using Python, C#, and Rust."
        ]
    }
]

# ==============================
# ✅ FEATURED PROJECTS
# ==============================
projects = [
    {
        "name": "AMR Logistics System",
        "description": "Deployment of  AMR robots for automated goods transportation in 10,000m2 factory area",
        "tags": ["Aichi Kikai AGV", "Ethernet/IP", "Ladder Logic", "PLC Toyopuc"]
    },
    {
        "name": "Pallet Recognition System",
        "description": "Yolov8 and EasyOCR based pallet recognition system for automated inventory management and logistics optimization",
        "tags": ["iPro Camera", "Yolov8", "Opencv", "Python", "EasyOCR"]
    },
    {
        "name": "Car Alignment Validation System",
        "description": "QR code based car alignment validation system for ADAS performance testing and validation in automotive industry",
        "tags": ["Raspberry Pi", "Python", "FastAPI", "OpenCV", "ADAS"]
    },
    {
        "name": "Automated Forklift Management System",
        "description": "Real-time forklift management system with coordinate tracking, navigation settings and activity logging for optimized warehouse operations",
        "tags": ["Ubuntu", "Python", "FastAPI", "OpenCV", "LiDAR", "Laser Sensor", "SocketIO"]
    }
]

# ==============================
# ✅ NEWS & TECHNOLOGY
# ==============================
news = [
    {
        "date": "April 10, 2026",
        "icon": "fa-android",
        "gradient_from": "accent",
        "gradient_to": "tech",
        "title": "AMR Trends in Smart Factory 2026",
        "excerpt": "Analysis of autonomous mobile robot development and important role in next generation automation production systems..."
    },
    {
        "date": "April 05, 2026",
        "icon": "fa-exchange",
        "gradient_from": "green-500",
        "gradient_to": "accent",
        "title": "OPC UA - Future Protocol for Industry 4.0",
        "excerpt": "Learn about OPC UA open communication standard and why it becomes the foundation for all modern automation systems..."
    },
    {
        "date": "March 28, 2026",
        "icon": "fa-microchip",
        "gradient_from": "orange-500",
        "gradient_to": "tech",
        "title": "Next Generation PLC with AI Integration",
        "excerpt": "Introduction of latest Programmable Logic Controllers with integrated artificial intelligence processing capabilities on edge..."
    },
    {
        "date": "March 15, 2026",
        "icon": "fa-rss",
        "gradient_from": "purple-500",
        "gradient_to": "accent",
        "title": "Next Generation IIoT Smart Sensors",
        "excerpt": "Industrial sensors today not only measure but also integrate data processing and wireless communication..."
    },
    {
        "date": "March 02, 2026",
        "icon": "fa-line-chart",
        "gradient_from": "tech",
        "gradient_to": "accent",
        "title": "Digital Twin in Manufacturing",
        "excerpt": "Digital twin technology helps simulate and optimize production processes before actual deployment..."
    },
    {
        "date": "February 20, 2026",
        "icon": "fa-lock",
        "gradient_from": "red-500",
        "gradient_to": "accent",
        "title": "Cybersecurity in OT Systems",
        "excerpt": "Cybersecurity challenges for industrial systems and solutions to protect critical infrastructure..."
    }
]

# ==============================
# ✅ CONTACT INFORMATION
# ==============================
contact_info = {
    "email": "biofan4u@hotmail.com",
    "phone": "+81 70 4157 8957",
    "address": "Aichi Prefecture, Japan",
    "linkedin": "linkedin.com/in/automation-engineer"
}
# Attendance Management System

An intelligent attendance management system built using Python and Streamlit. The application helps teachers manage classes, register students, and record attendance using face and voice recognition.

##  Live Demo

[Open Attendance Management System](https://attendance-main-ai.streamlit.app/)

##  Project Overview

The Attendance Management System is designed to simplify the traditional attendance process through automation. It provides a platform for teachers and students to manage attendance records efficiently.

##  Features

- **Teacher Registration & Login** – Secure teacher account access.
- **Student Registration & Login** – Student account management.
- **Face Recognition** – Supports face-based attendance.
- **Voice Recognition** – Supports voice-based identification.
- **Attendance Management** – Record and review attendance.
- **QR Code Sharing** – Share class joining links using QR codes.
- **Database Integration** – Store and retrieve records using Supabase.
- **Interactive Dashboard** – User-friendly Streamlit interface.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Supabase | Database and backend |
| OpenCV | Image processing |
| NumPy | Numerical operations |
| Pandas | Data handling |
| Bcrypt | Password hashing |
| Segno | QR code generation |

##  Project Structure

```text
attendance-website/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── components/
    ├── database/
    ├── pipelines/
    └── ui/
```

##  Installation & Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd attendance-website
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your Supabase credentials using Streamlit secrets.

5. Run the application:

```bash
streamlit run app.py
```

##  Security

- Password hashing using Bcrypt.
- Supabase credentials stored in Streamlit secrets.
- Sensitive configuration files excluded from GitHub.

##  Deployment

Deployed using **Streamlit Community Cloud**.

##  Developer

**Sai Charan Reddy**

GitHub: [YOUR_GITHUB_PROFILE_URL](https://github.com/saicharanreddy987)

---

*An automated approach to making attendance management simpler and more efficient.*

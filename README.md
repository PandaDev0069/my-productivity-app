# Productivity App - Backend API

## 🌐 Frontend Repository
Frontend: [https://github.com/PandaDev0069/productivity-app-frontend](https://github.com/PandaDev0069/productivity-app-frontend)

## 📖 Overview
A comprehensive productivity management system backend built with Flask. This RESTful API serves a React frontend and helps users manage tasks, track expenses, set goals, and boost productivity through various productivity features.

## ✨ Key Features
- 🔐 **User Authentication** - JWT-based secure authentication
- ✅ **Task Management** - Create, update, delete tasks with priorities and recurrence
- 📝 **Note Taking** - Markdown-supported notes with CRUD operations
- 💰 **Expense Tracking** - Category-based expense management
- 🎯 **Goal Setting** - Personal productivity goals
- 📊 **User Progress** - XP system with level progression
- � **Secure API** - CORS enabled, JWT protected endpoints
- 📱 **Mobile Ready** - Responsive API design

## 🛠 Tech Stack
- **Framework**: Flask 3.1.0
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-JWT-Extended
- **Migrations**: Flask-Migrate with Alembic
- **Security**: SSL/TLS enabled, CORS configured
- **Email**: Flask-Mail support
- **Deployment**: Gunicorn + Uvicorn ready

## 📋 API Endpoints

### Authentication
- `POST /api/register` - User registration
- `POST /api/login` - User login
- `GET /api/profile` - Get user profile (JWT required)

### Tasks
- `GET /api/tasks` - Get all user tasks
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task

### Notes
- `GET /api/notes` - Get all user notes
- `POST /api/notes` - Create new note
- `PUT /api/notes/<id>` - Update note
- `DELETE /api/notes/<id>` - Delete note

### Expenses
- `GET /api/expenses` - Get all user expenses
- `POST /api/expenses` - Create new expense
- `PUT /api/expenses/<id>` - Update expense
- `DELETE /api/expenses/<id>` - Delete expense

## 🗄 Database Models

### User
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `password` - Hashed password
- `xp` - User experience points (default: 0)

### Task
- `id` - Primary key
- `title` - Task title
- `description` - Task description
- `due_date` - Due date (required)
- `deadline` - Optional deadline
- `completed` - Boolean completion status
- `priority` - Priority level (low, medium, high)
- `recurrence` - Recurrence pattern (none, daily, weekly, monthly)
- `user_id` - Foreign key to User

### Note
- `id` - Primary key
- `title` - Note title
- `content` - Markdown content
- `created_at` - Creation timestamp
- `user_id` - Foreign key to User

### Expense
- `id` - Primary key
- `amount` - Expense amount (float)
- `category` - Expense category
- `date` - Expense date
- `user_id` - Foreign key to User

## 📁 Project Structure
```
my-productivity-app/           #  Backend Flask Application
├── app/                      # � Application Package
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration settings
│   ├── extensions.py        # Flask extensions initialization
│   ├── models.py            # � Database models (User, Task, Note, Expense)
│   └── routes.py            # 🌐 API endpoints and routes
├── instance/                # 📊 Instance-specific files
│   └── database.db          # SQLite database file
├── migrations/              # 📈 Database migration files
│   ├── versions/            # Migration version files
│   ├── alembic.ini         # Alembic configuration
│   └── env.py              # Migration environment
├── main.py                  # � Application entry point
├── requirements.txt         # 📦 Python dependencies
├── setup_database.py        # � Database initialization script
├── cert.pem                # 🔒 SSL certificate
└── key.pem                 # 🔑 SSL private key
```

## � Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd my-productivity-app
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python setup_database.py
   ```

5. **Run the application**
   ```bash
   # Development mode
   python main.py
   
   # Or using Flask CLI
   flask run
   
   # Production mode with SSL
   python main.py --ssl
   ```

The API will be available at:
- HTTP: `http://localhost:5000`
- HTTPS: `https://localhost:5000` (with SSL certificates)

## � Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
# Database
DATABASE_URL=sqlite:///instance/database.db

# JWT Secret Key
JWT_SECRET_KEY=your-super-secret-jwt-key-here

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Mail Configuration (optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## 🧪 Development

### Database Migrations
```bash
# Initialize migration repository (first time only)
flask db init

# Create a new migration
flask db migrate -m "Description of changes"

# Apply migrations to database
flask db upgrade

# Downgrade to previous migration
flask db downgrade
```

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-flask

# Run tests
pytest

# Run with coverage
pytest --cov=app
```

## � API Usage Examples

### Authentication
```bash
# Register a new user
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "email": "john@example.com", "password": "securepassword"}'

# Login
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email": "john@example.com", "password": "securepassword"}'
```

### Tasks
```bash
# Create a task (requires JWT token)
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"title": "Complete project", "description": "Finish the productivity app", "due_date": "2024-12-31 23:59:59", "priority": "high"}'

# Get all tasks
curl -X GET http://localhost:5000/api/tasks \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 🚢 Deployment

### Using Gunicorn
```bash
# Install Gunicorn (already in requirements.txt)
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app

# With SSL
gunicorn -w 4 -b 0.0.0.0:5000 --certfile=cert.pem --keyfile=key.pem main:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🛟 Support

For support, email your-email@example.com or create an issue in the repository.
# SecureAuth Pro - Modern Login System

A production-ready, secure login system with modern UI design and comprehensive security features.

## Features

### 🔐 Security Features
- **Password Hashing**: Uses Werkzeug's secure password hashing
- **CSRF Protection**: Built-in CSRF token validation
- **Session Management**: Secure session handling with configurable timeouts
- **Input Validation**: Comprehensive form validation with WTForms
- **SQL Injection Protection**: Parameterized database queries
- **Brute Force Protection**: Rate limiting capabilities

### 🎨 Modern Design
- **Responsive UI**: Mobile-first design with Bootstrap 5
- **Cool Visual Effects**: Interactive hover effects and animations
- **Modern Typography**: Inter font family for clean aesthetics
- **Gradient Backgrounds**: Beautiful gradient overlays
- **Glass Morphism**: Backdrop blur effects for modern appeal
- **Interactive Elements**: Smooth transitions and loading states

### 🚀 Production Ready
- **Error Handling**: Comprehensive error pages (404, 500)
- **Form Validation**: Real-time client and server-side validation
- **User Experience**: Loading states, feedback messages, and tooltips
- **Database Integration**: SQLite database with proper schema
- **Modular Code**: Clean, maintainable Flask application structure

## Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   - Open your browser and go to `http://localhost:5000`
   - Default admin credentials: `admin` / `admin123`

## Project Structure

```
Lesson5/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── users.db              # SQLite database (auto-created)
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── dashboard.html    # User dashboard
│   ├── 404.html          # Error page
│   └── 500.html          # Error page
└── static/
    └── css/
        └── style.css     # Custom styles
```

## Usage

### Login
- Navigate to the login page
- Enter your username and password
- Optional "Remember Me" for extended sessions
- Forgot password functionality available

### Registration
- Create a new account with username, email, and password
- Real-time password strength validation
- Terms of service acceptance required
- Automatic duplicate checking

### Dashboard
- Secure user area after login
- Account status information
- Profile management options
- Security settings access

## Security Configuration

The application includes several security measures:

- **Session Security**: Random secret keys and configurable timeouts
- **Password Policy**: Minimum 6 characters with strength validation
- **Database Security**: Parameterized queries prevent SQL injection
- **CSRF Protection**: All forms protected against cross-site request forgery
- **Input Sanitization**: Server-side validation for all user inputs

## Dependencies

- **Flask**: Web framework
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation
- **Werkzeug**: Password hashing utilities
- **Bootstrap 5**: CSS framework
- **Font Awesome**: Icon library

## License

This project is intended for educational and development purposes.
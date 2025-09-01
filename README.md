# Sigma Freelancer Client Dashboard

![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-blue.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A modern, responsive client dashboard built with Django, Bootstrap 5, and Chart.js, designed to streamline project management for freelance clients. Features a professional landing page, secure login, and an animated dashboard with real-time project tracking via pie charts and progress bars. Deployed on PythonAnywhere for reliable access.

🔗 **[Live Demo](https://sigmafreelncer.pythonanywhere.com/)**

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project is a full-stack web application developed to enhance client communication for freelancers. It provides a centralized portal for clients to track project progress, view task statuses, and receive updates in real-time. The platform features a modern UI with animated elements, making it both functional and visually appealing. Built as a portfolio piece for Upwork, it showcases expertise in Django, Bootstrap, and JavaScript.

## Features
- **Professional Landing Page**: A responsive, Bootstrap-based homepage with a call-to-action for client login.
- **Secure Login System**: Django authentication with a modern, animated login interface.
- **Interactive Dashboard**: Displays project details, task statuses, and updates with animated pie charts (Chart.js) and progress bars.
- **Real-Time Tracking**: Clients can monitor project and task progress with visual indicators.
- **Responsive Design**: Optimized for desktop and mobile devices using Bootstrap 5.
- **Animations**: Fade-in, slide-in, and progress bar animations for a polished user experience.
- **Task Modals**: Detailed task views with descriptions, due dates, and updates.

## Tech Stack
| Category          | Technologies                     |
|-------------------|----------------------------------|
| **Backend**       | Django 5.2, Python 3.13          |
| **Frontend**      | Bootstrap 5.3, Chart.js, Font Awesome 6 |
| **Deployment**    | PythonAnywhere, Git              |
| **Database**      | SQLite                           |
| **Styling**       | Custom CSS with animations        |

## Installation
To run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd freelance_clientdashboard
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python client_dashboard/manage.py makemigrations
   python client_dashboard/manage.py migrate
   ```

5. **Collect Static Files**:
   ```bash
   python client_dashboard/manage.py collectstatic
   ```

6. **Run the Development Server**:
   ```bash
   python client_dashboard/manage.py runserver
   ```

7. **Access Locally**:
   Open `http://127.0.0.1:8000/` in your browser.

## Usage
- **Landing Page**: Visit the root URL (`/`) for a professional welcome page with a login CTA.
- **Login**: Access `/login/` with credentials (e.g., `testclient`/`test123` for demo).
- **Dashboard**: View `/dashboard/` to track projects, tasks, and updates with animated pie charts and progress bars.
- **Admin Panel**: Manage projects and tasks at `/admin/` (requires superuser login).

## Screenshots
### Landing Page
![Landing Page](client_dashboard/home.png)
*Modern, responsive landing page with Bootstrap 5 and CTA.*

### Login Page
![Login Page](screenshots/login_page.png)
*Secure, animated login interface with error handling.*

### Dashboard
![Dashboard](screenshots/dashboard.png)
*Interactive dashboard with pie charts, progress bars, and task modals.*

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Built by sigmafreelancer. Contact [sigmafreelancers@gmail.com](mailto:sigmafreelancers@gmail.com) for freelance opportunities!*

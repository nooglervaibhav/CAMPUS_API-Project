

# Campus Event Reminder App

A web application designed to help college students stay updated about upcoming campus events by providing reminders, event details, and filtering options.

---

## Overview

The Campus Event Reminder App enables students to:
- View a list of upcoming campus events.
- Filter events by type (e.g., Tech, Talk, Cultural, Seminar).
- Set personal email reminders for events.
- View detailed event information (description, organizer, location).
- Optionally add events to their phone calendar.

---

## Features

- **View Events:** See a list of upcoming events with date and time.
- **Filter by Type:** Easily filter events by categories such as Tech, Talk, Cultural, and Seminar.
- **Set Reminders:** Add and manage personalized event reminders via email.
- **Event Details:** Access full event details including description, organizer, and location.
- **Add to Calendar:** Optionally add events directly to your phone calendar.

---



---

## Tech Stack

- **Frontend:** HTML, Tailwind CSS
- **Backend:** Django (Python)
- **Database:** SQLite (can be upgraded to Postgres/MongoDB)
- **Notifications:** Browser-based or in-app alerts

---

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Node.js and npm (for Tailwind CSS, optional)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nooglervaibhav/BlogAPPExpress.git
   cd BlogAPPExpress
   ```

2. **Backend Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

3. **Frontend Setup**
   - Tailwind is integrated via CDN or can be built using npm.
   - If building locally:
     ```bash
     npm install
     npx tailwindcss -i ./static/src/input.css -o ./static/css/tailwind.css --watch
     ```

4. **Access the App**
   - Open your browser at [http://localhost:8000](http://localhost:8000)

---

## Usage

- Browse the home screen to view all upcoming events.
- Use the filter dropdown/buttons to view events by category.
- Click an event for details and to set a reminder.
- Manage your reminders from the settings page.

---

## Project Structure

```
/BlogAPPExpress
  ├── backend/ (Django project)
  ├── static/
      ├── src/
      ├── css/
  ├── templates/
  ├── requirements.txt
  ├── README.md
  └── ...
```

---

## Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE)

---

## Deliverables

- Working deployed app (Vercel, PythonAnywhere, etc.)
- Code on GitHub
- Demo video (2-3 minutes)
- Final report (PDF with screenshots and features)

---

## Contact

For questions or feedback, please contact [nooglervaibhav](https://github.com/nooglervaibhav).

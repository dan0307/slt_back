# Django Rest + React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh
# Capstone - Steps for Running Project

### Requirements

`Python, Node, git`

### Clone the repository:

- Create a empty folder and `cd` into that folder.
- Type the following command to clone project in same directory.

```bash
git clone https://github.com/zhansvltan/capstone.git -b backend
```

## Backend

### 1. Go to the root folder and perform the following commands:

`cd backend/`

### 2. Create and activate the virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

> If their is any error activating virtual env, please google search it for your system or try `venv\bin\activate` or `source venv/bin/activate`

### 3. Install required packages

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python manage.py migrate
python manage.py runserver
```

## Frontend

- Head back to the root folder
- Enter in `cd frontend/`

### 1. Installing packages

```bash
npm install
```

### 2. Run the application

```bash
npm run dev
```

> Make sure both frontend and backend are running.

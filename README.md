# Django Rest

### Requirements

`Python, git`

### Clone the repository:

- Create a empty folder and `cd` into that folder.
- Type the following command to clone project in same directory.

```bash
git clone https://github.com/bekaffee/slt_back.git
```

## Backend

### 1. Create and activate the virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

> If their is any error activating virtual env, please google search it for your system or try `venv\bin\activate` or `source venv/bin/activate`

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Run the server

```bash
python manage.py migrate
python manage.py runserver
```

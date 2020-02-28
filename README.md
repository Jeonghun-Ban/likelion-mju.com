mjuseoul.likelion.org
===

📖 Introduction
---

This project is a site for applying Likelion at MJU Seoul

🏁 Getting started
---

first of all, prepare a virtual environment with the django and several packages

### 1. create virtual environment
```bash
$ python -m venv venv
```

The name of virtual environment is defined by "venv"

### 2. activate virtual environment
```bash
$ source venv/scripts/activate # for windows
$ source venv/bin/activate # for mac or linux
```

### 3. install pip packages
```bash
$ pip install -r requirements.txt
```

The required packages are defined in the requirements.txt file.

```bash
$ pip freeze > requirements.txt
```

If additional packages are installed, the following commands should be executed.

🧐 What's inside?
---
    .
    ├── config
    ├── page
    ├── .gitignore
    ├── manage.py
    ├── README.md
    └── requirements.txt

1. `/config`: setup files in project
2. `/page`: app directory
3. `.gitignore`: define what should be ignored in git
4. `manage.py`: django command-line util
5. `requirement.txt`: list of pip-packages to install

📝 License
---
This project uses the [MIT License](LICENSE)
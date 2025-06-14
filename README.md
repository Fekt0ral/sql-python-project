# MySQL Product Reporter

A lightweight Python script that connects to a MySQL database, retrieves basic product and order statistics, and prints nicely formatted reports to the console using pandas.

## Requirements

Install dependencies listed in requirements.txt (Python 3.8 or newer):

```bash
pip install -r requirements.txt
```

Key libraries:

* mysql‑connector‑python – MySQL driver

* python‑dotenv – reads environment variables from .env

* pandas – tabular formatting

## Environment Variables

The script expects a local .env file (ignored by Git) with the following keys:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD='your_password'
DB_NAME=shop

Tip: The script never prints credentials; they stay in memory only.

## Usage

```bash
python shop.py
```

## Project Structure

├── .gitignore
├── requirements.txt
├── project.py       # main script (this repo)
├── shop.sql       # creating tables script
└── README.md

## License

This project is licensed under the MIT License. Feel free to use and modify it as you like.

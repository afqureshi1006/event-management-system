# Event Management System — 3-Tier Demo

A small lab demo with:
- **Presentation tier:** HTML/CSS page in `templates/index.html`
- **Application tier:** Python Flask API/web application in `app.py`
- **Database tier:** MySQL table `events`

## 1. Install prerequisites (Ubuntu)

```bash
sudo apt update
sudo apt install mysql-server python3-pip python3-venv -y
sudo systemctl enable --now mysql
```

## 2. Create the database and user

```bash
sudo mysql < database.sql
```

This creates database `events`, table `events`, and user `eventuser`.
For a lab/demo only, the sample password is `event123`. Change it for real use.

## 3. Install Python packages and run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export DB_HOST=localhost
export DB_USER=eventuser
export DB_PASSWORD=event123
export DB_NAME=events

python app.py
```

Open `http://YOUR-EC2-PUBLIC-IP:5000` in your browser.
Allow inbound TCP port **5000** in the EC2 Security Group, preferably only from your own IP.

## 4. Docker build (optional next step)

```bash
docker build -t event-management:1.0 .
docker run --rm -p 5000:5000   -e DB_HOST=YOUR_MYSQL_HOST   -e DB_USER=eventuser   -e DB_PASSWORD=event123   -e DB_NAME=events   event-management:1.0
```

The MySQL server must be reachable from the container. For Kubernetes, deploy the app and MySQL as separate workloads and configure `DB_HOST` to the MySQL Service name.

## Useful route

- `/` — event form and event list
- `/health` — simple health check

**Note:** This is an educational starter project, not production-ready. It has no login, authorization, CSRF protection, or input validation beyond required fields.

FROM python:3.12-slim

ENV TZ=Asia/Dhaka

# Install cron
RUN apt-get update && apt-get install -y cron tzdata \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Copy cron job definition
COPY cronjob /etc/cron.d/python-cron

# Give execution rights on cron job
RUN chmod 0644 /etc/cron.d/python-cron

# Apply cron job
RUN crontab /etc/cron.d/python-cron

# Create log file
RUN touch /var/log/cron.log

# Run cron in foreground
CMD ["cron", "-f"]

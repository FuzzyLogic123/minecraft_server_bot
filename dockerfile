FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DISCORD_TOKEN="MTExNTg3NjI0MTg5NjEyODYwMg.G17Dyp.1LwOGKvIRFbKzUSSwCueR-MbNl5vnzyIm-ZpS4"

ENV INSTANCE_ID="i-03e95d7bb3185f3df"

ENV AWS_DEFAULT_REGION="us-east-1"

ENV AWS_ACCESS_KEY_ID="AKIAVIHVMRMM7DUENAVT"

ENV AWS_SECRET_ACCESS_KEY="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"

CMD [ "python3", "src/bot.py" ]
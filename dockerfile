FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV INSTANCE_ID="i-0314a39005a1b27ad"
ENV AWS_ACCESS_KEY_ID="AKIAZC2BCDTXZXT6ARL7"
ENV AWS_DEFAULT_REGION="us-east-1"



CMD [ "python3", "src/bot.py" ]
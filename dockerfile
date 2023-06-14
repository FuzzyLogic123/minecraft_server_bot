FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV INSTANCE_ID="i-03e95d7bb3185f3df"
ENV AWS_ACCESS_KEY_ID="AKIAVIHVMRMM6Y27SMOA"
ENV AWS_DEFAULT_REGION="us-east-1"



CMD [ "python3", "src/bot.py" ]
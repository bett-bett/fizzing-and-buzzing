FROM python:3.10

WORKDIR /app

COPY app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["flask run", "app.py"]
# what if ..
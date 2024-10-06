FROM python
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir requests
RUN chmod +x jokes.py
CMD ["python", "./jokes.py"]

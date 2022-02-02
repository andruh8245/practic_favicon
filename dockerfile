FROM python

WORKDIR /favicon

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "download_favicon.py"]
CMD ["www.google.com"]

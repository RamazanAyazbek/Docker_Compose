FROM python
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
ENV PORT 4200
EXPOSE $PORT 
VOLUME [ "/app/data" ]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]





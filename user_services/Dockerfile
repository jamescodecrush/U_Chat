FROM python:3.12

WORKDIR /user_services

COPY . /user_services

RUN pip install --no-cache-dir-r requirements.txt

EXPOSE 8000

ENV ENVIRONMENT=production

# RUN main.py when the container lunches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
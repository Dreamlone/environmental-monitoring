FROM python:3.10
RUN pip install "poetry==1.3.2"
RUN pip install "pandas==2.2.2"
RUN pip install "matplotlib==3.8.4"
RUN pip install "seaborn==0.13.2"
RUN pip install "uvicorn==0.29.0"
RUN pip install "fastapi==0.110.2"
RUN pip install "jinja2==3.1.3"
RUN pip install "python-multipart==0.0.9"
RUN pip install "fastparquet==2024.2.0"
RUN pip install "openpyxl==3.1.2"

# Copy code
WORKDIR /code

# Copy necessary code
COPY ./app /code/app
COPY ./data /code/data
COPY ./emo /code/emo
COPY ./app/templates /code/templates
COPY ./start.sh /code/start.sh

RUN chmod +x /code/start.sh

# Socket configuration
CMD ["./start.sh"]
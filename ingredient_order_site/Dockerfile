FROM ubuntu:bionic
RUN useradd -g users python
RUN apt-get update
RUN apt-get install -y \
	ca-certificates \
	python3-all-dev \
	python3-venv \
	postgresql-server-dev-all \
	build-essential
RUN python3 -m venv /env
ENV PATH="/env/bin/:$PATH"
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN pip install -U pip wheel
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install gunicorn
RUN pip install daphne
ENV PYTHONUNBUFFERED 1
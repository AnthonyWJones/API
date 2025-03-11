#
FROM docker.io/python:3.12.2-slim-bookworm AS python

#  Stage 1: Build our dependency wheels
FROM python AS python-build-stage

ARG apt-get update && apt-get install --no-install-recommends -y build-essential libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIROMENT}.txt

# Stage 2 : Run Stage
FROM python AS python-run-stage

ARG BUILD_ENVIROMENT=local

ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE=1
    PYTHONUNBUFFERED=1 \
    BUILD_ENV=${BUILD_ENVIROMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo git bash-completion nano ssh \
    libq-dev gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django && \
    adduser --system --ingroup django django && \
    mkdir -p ${APP_HOME}/staticfiles && \
    chown django:django ${APP_HOME}/staticfiles && \
    chmod 775 ${APP_HOME}/staticfiles

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY chown=django:django ./docker/local/django/entrypoint







# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 for Django development server
EXPOSE 8000

# Default command to run Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
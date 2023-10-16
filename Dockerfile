############
# Virtualenv
############
FROM python:3.11-alpine as builder

RUN apk add --update --no-cache --virtual .build-deps build-base libffi-dev git rust cargo openssl-dev \
  && python -m venv --copies /opt/venv

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PATH="/opt/venv/bin:$PATH"

COPY poetry.lock pyproject.toml /tmp/

RUN pip install --upgrade pip \
  && pip install --no-cache-dir poetry
RUN cd /tmp  \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi \
  && rm -fr /tmp/poetry.lock /tmp/pyproject.toml \
  && pip install setuptools

#########
# Runtime
#########
FROM python:3.11-alpine as runtime

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app
COPY . .

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENTRYPOINT ["python"]

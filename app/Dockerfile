# syntax=docker/dockerfile:1

########
# base #
########
FROM python:3.12-slim-bookworm AS base

ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONUNBUFFERED=true
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.8.5
ENV PATH=$POETRY_HOME/bin:$PATH

RUN rm /etc/apt/apt.conf.d/docker-clean

RUN \
--mount=type=cache,target=/var/lib/apt,sharing=locked \
--mount=type=cache,target=/var/cache/apt,sharing=locked \
<<EOF bash -ex
  apt-get update -y
  apt-get install -y --no-install-recommends \
  curl libopencv-dev
EOF

# Install Python package manager
RUN <<EOF bash -ex
  curl -sSL https://install.python-poetry.org | python3 -
  poetry config virtualenvs.create false
  mkdir -p /cache/poetry
  poetry config cache-dir /cache/poetry
EOF

# Install Python libraries required for run
RUN \
  --mount=type=cache,target=/cache/poetry \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  --mount=type=bind,source=poetry.lock,target=poetry.lock \
  poetry install --no-interaction --no-root --only main



###############
# development #
###############
FROM base AS development

ARG APP_HOME=/workspace
ENV PYTHONPATH=$APP_HOME/src:$PYTHONPATH

# Install Python libraries required for dev
RUN --mount=type=cache,target=/cache/poetry \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  --mount=type=bind,source=poetry.lock,target=poetry.lock \
  poetry install --no-interaction --no-root

WORKDIR $APP_HOME

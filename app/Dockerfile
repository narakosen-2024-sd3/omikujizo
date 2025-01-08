# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12
ARG APP_HOME=/workspace

########
# base #
########
FROM python:${PYTHON_VERSION}-slim-bookworm AS base



########
# deps #
########
FROM base AS deps

ENV PYTHONDONTWRITEBYTECODE=true
ENV PYTHONUNBUFFERED=true
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.8.5
ENV POETRY_REQUESTS_TIMEOUT=600
ENV PATH=$POETRY_HOME/bin:$PATH
ENV PYTHONPATH=$APP_HOME/src:$PYTHONPATH

RUN rm /etc/apt/apt.conf.d/docker-clean

RUN \
--mount=type=cache,target=/var/lib/apt,sharing=locked \
--mount=type=cache,target=/var/cache/apt,sharing=locked \
<<-EOF bash -ex
  apt-get update -y
  apt-get install -y --no-install-recommends \
  curl libopencv-dev build-essential
EOF

# Install Python package manager
RUN \
<<-EOF bash -ex
  curl -sSL https://install.python-poetry.org | python3 -
  poetry config virtualenvs.create false
  mkdir -p /cache/poetry
  poetry config cache-dir /cache/poetry
EOF

# Install Python packages required for run
RUN \
--mount=type=cache,target=/cache/poetry \
--mount=type=bind,source=pyproject.toml,target=pyproject.toml \
--mount=type=bind,source=poetry.lock,target=poetry.lock \
poetry install --no-interaction --no-root --only main



###############
# development #
###############
FROM deps AS development

# Install Python packages required for dev
RUN \
--mount=type=cache,target=/cache/poetry \
--mount=type=bind,source=pyproject.toml,target=pyproject.toml \
--mount=type=bind,source=poetry.lock,target=poetry.lock \
poetry install --no-interaction --no-root

WORKDIR $APP_HOME



##############
# production #
##############
FROM deps AS production

WORKDIR $APP_HOME

RUN \
--mount=type=cache,target=/var/lib/apt,sharing=locked \
--mount=type=cache,target=/var/cache/apt,sharing=locked \
<<-EOF bash -ex
  apt-get update -y
  apt-get install -y --no-install-recommends \
  libopencv-dev
EOF

COPY --from=deps /usr/local/lib/python*/site-packages /usr/local/lib/python*/site-packages
COPY . .

CMD ["python", "src/main.py"]

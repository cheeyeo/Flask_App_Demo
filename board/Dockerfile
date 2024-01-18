FROM python:3.10-slim-buster as base

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt alembic.ini entrypoint.sh .

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

FROM base as prod
# Production image
RUN pip install gunicorn
COPY . .
COPY ../migrations /migrations
ENTRYPOINT ["gunicorn", "--reload", "-w", "4", "--bind", "0.0.0.0:8000", "board:create_app()"]
FROM python:3.10-slim-buster as base

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt alembic.ini entrypoint.sh .

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

# Production image
FROM base as prod

RUN pip install gunicorn


COPY board/ /board
COPY migrations/ /migrations

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--access-logfile=-", "-w", "4", "--bind", "0.0.0.0:8000", "board:create_app()"]
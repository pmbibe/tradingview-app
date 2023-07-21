FROM python:3.9-slim AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.9-slim AS release

WORKDIR /app

COPY --from=builder /root/.local/lib/python3.9/site-packages /root/.local/lib/python3.9/site-packages

COPY ./sample/ .

ENV PATH=/root/.local:$PATH

# RUN addgroup --gid 1001 --system app && \
#     adduser --no-create-home --shell /bin/false --disabled-password --uid 1001 --system --group app

# USER app

CMD [ "python", "core.py" ]
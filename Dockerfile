FROM ghcr.io/randomicu/fakedata-backend-base:1.0.2

ENV FAKEDATA_DATABASE_URL postgresql://postgres:password@172.19.0.10/fakedata

WORKDIR $PYSETUP_PATH

COPY ./ ./

RUN chmod +x ./scripts/migrate.sh && \
    poetry install --no-root --no-dev

CMD ["./scripts/migrate.sh"]

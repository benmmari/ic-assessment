FROM python:3.6-onbuild
COPY . /usr/src/app
CMD ["nameko", "run", "--config", "config.yaml", "service"]


FROM python:3.10.12-alpine

COPY src /app
WORKDIR /app

RUN mkdir static
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY scripts/entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 8000

ENV ENVIRONMENT=development
ENV SECRET_KEY="django-insecure-jdsgb*65z1b6deez!^h$d1pe)g5fo2&)dz92gq+9tn-g(2g3@f"
ENV DEBUG=true
ENV LANGUAGE_CODE=en-us
ENV TIME_ZONE=UTC
ENV ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
ENV SESSION_COOKIE_SECURE=false
ENV SECURE_BROWSER_XSS_FILTER=false
ENV SECURE_CONTENT_TYPE_NOSNIFF=false
ENV SECURE_HSTS_INCLUDE_SUBDOMAINS=false
ENV SECURE_HSTS_SECONDS=31536000
ENV SECURE_REDIRECT_EXEMPT=""
ENV SECURE_SSL_REDIRECT=False
ENV BEHIND_PROXY=false
ENV SUPER_USER_NAME=admin
ENV SUPER_USER_PASSWORD=password123
ENV SUPER_USER_EMAIL="admin@example.com"

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
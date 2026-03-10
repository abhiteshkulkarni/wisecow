FROM ubuntu:latest
ENV PATH="$PATH:/usr/games"
RUN apt update && apt install -y fortune-mod cowsay netcat-openbsd
WORKDIR /app
COPY . .
RUN chmod +x wisecow.sh
EXPOSE 4499
CMD ["sh", "wisecow.sh"]

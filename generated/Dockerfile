
FROM debian:12-slim

RUN apt update && apt install -y nginx curl && apt clean

CMD ["nginx", "-g", "daemon off;"]

FROM python:3

WORKDIR /app

# 서버 코드 및 플래그 파일 복사
COPY src/server.py /app/server.py
COPY src/flag.txt /flag.txt
COPY start.sh /start.sh 

RUN chmod +x /start.sh

# 포트 노출
EXPOSE 7201

# 컨테이너 실행 시 `start.sh` 실행
ENTRYPOINT ["/start.sh"]


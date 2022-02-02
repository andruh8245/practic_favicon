# practic_favicon

Строка скачивания /n

docker build -t favicon .
docker run --name favicon -d --rm -v /home/andrey/docker/http_wget:/favicon/ favicon

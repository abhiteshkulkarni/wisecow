openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt

kubectl create secret tls wisecow-tls --key tls.key --cert tls.crt

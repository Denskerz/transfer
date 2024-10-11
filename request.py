curl -L --insecure -x 172.30.71.80:3128 -X POST 'http://172.30.71.10:50510/api/v2/oauth' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Accept: application/json' \
-H 'RqUID: 6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e' \
-H 'Authorization: Basic OGJiZTg3NGEtNjA0OS00NjQ3LTk1YWMtNzVhNDNjNzdmODUxOjU0MTY1OWNhLWI3NDctNDBlZS05MTM3LWY3Y2M0OGY3NWQ4Zg==' \
--data-urlencode 'scope=GIGACHAT_API_CORP'


curl -L --insecure -x 172.30.71.80:3128 -X POST 'http://172.30.71.10:50511/api/v1/chat/completions' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Authorization: Bearer токен' --data-raw '{  "model": "GigaChat",  "messages": [    {      "role": "system",      "content": "Ты опытный специалит контакт-центра Банка"    },    {      "role": "user",      "content": "текст"    }  ],  "temperature":1,  "top_p":0.1,  "n": 1,  "stream": false,  "max_tokens":100,  "update_interval": 0}'

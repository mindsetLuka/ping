# Ping

## Модули

* Точка входа, передача ключей `tcping.py`
* Связующий узел `ping_process.py`
* Вывод информации на консоль `printer.py`
* Работа с замерами времени `timer.py`
* Формирование ICMP запроса `icmp_echo_request.py`
* Класс ICMP ответа `icmp_echo_reply.py`
* Конфигурация и работа с RAW socket `icmp_socket.py`

## Запуск

Реализован help

win `python tcping.py -h`

linux `[sudo] python3 tcping.py -h`

Вот он:

```
usage: tcping.py [-h] [--port PORT] [--count COUNT] [--interval INTERVAL] [--wait WAIT] hosts

Usage tcping [options] <hosts>

positional arguments:
   hosts                             one or more dns name or ip address

optional arguments:
  -h, --help                         show this help message and exit
  --port PORT, -p PORT               port
  --count COUNT, -c COUNT            stop after <count> replies
  --interval INTERVAL, -i INTERVAL   seconds between sending each packet
  --wait WAIT, -w WAIT               seconds time to wait for response
```

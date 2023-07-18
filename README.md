# Тестовое задание SMIT

## Запуск

Cоздаем новый образ и запускаем контейнеры командой:

<code>docker-compose up -d --build</code>

Сервис будет доступен по локальному адресу [http://127.0.0.1:8008](http://127.0.0.1:8008)

## Функции веб-сервиса

![functions](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F7f%2Fhpwlpsdd7k3d5jxg70czn84m0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_h7J8qa%2FScreenshot%202023-07-18%20at%2017.05.15.png)
<ul>
<li><code> /rate/create</code> </li>
 - Позволяет добавить тарифы вручную
<li><code> /uploadjson/</code> </li>
 - Позволяет добавить тарифы через json-файл
<li> <code>/rates/</code> </li>
 - Просмотр всех тарифов в базе данных
<li> <code>/rate/</code> </li>
 - Возвращает (объявленную стоимость * rate) в зависимости от указанного в запросе типа груза и даты (даты записываются по формату "YYYY-MM-DD"
<li> <code>/calculate/rate</code> </li>
 - Просчитывает стоимость страхования для запроса
</ul>

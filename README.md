# Тестовое задание SMIT

## Запуск

Cоздаем новый образ и запускаем контейнеры командой:

<code>docker-compose up -d --build</code>

Сервис будет доступен по локальному адресу [http://127.0.0.1:8008](http://127.0.0.1:8008)

## Функции веб-сервиса

<img width="1391" alt="Screenshot 2023-07-18 at 17 43 16" src="https://github.com/ArtemusCoder/Intern_SMIT/assets/33132419/ba31cb82-bd38-47f6-bc11-40792d70680e">
<ul>
<li><code> /rate/create</code> </li>
 - Позволяет добавить тарифы вручную
<li><code> /uploadjson/</code> </li>
 - Позволяет добавить тарифы через json-файл
<li> <code>/rates/</code> </li>
 - Просмотр всех тарифов в базе данных
<li> <code>/rate/</code> </li>
 - Возвращает (объявленную стоимость * rate) в зависимости от указанного в запросе типа груза и даты (даты записываются по формату "YYYY-MM-DD")
<li> <code>/calculate/rate</code> </li>
 - Просчитывает стоимость страхования для запроса
</ul>

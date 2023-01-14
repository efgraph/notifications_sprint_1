# Проектная работа 10 спринта

## Сервис сообщений

##### Запуск проекта 

docker-compose up


- Админ панель для создания и отправки сообщений от администратора (admin)

    http://localhost:8000/admin (user/password)
    
- API для получения сообщений из внешних сервисов (event_api)

    http://localhost:10000/api/openapi

- Планировщик, отправляющий сообщения с определенной периодичностью (scheduler)


- Сервис, выбирающий из очереди сообщения и отправляющий их в нужный канал (worker)


![Схема API](./uml/notification.png?raw=true)


### Ссылка на репозиторий


https://github.com/efgraph/notifications_sprint_1
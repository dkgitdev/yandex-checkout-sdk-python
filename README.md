# Yandex.Checkout API Python Client Library

Russian | [English](https://github.com/dkgitdev/yandex-checkout-sdk-python/blob/master/README.en.md)

Клиент для работы с платежами по старому API Яндекс.Кассы
Подходит тем, у кого способ подключения к Яндекс.Кассе называется API.

## Требования

1. Python 2.7 или Python 3.x
2. pip

## Установка
### C помощью pip

1. Установите pip.
2. В консоли выполните команду
```bash
pip install --upgrade yandex_checkout
```

### С помощью easy_install
1. Установите easy_install.
2. В консоли выполните команду
```bash
easy_install --upgrade yandex_checkout
```

## Начало работы

1. Импортируйте модуль
```python
import yandex_checkout
```
2. Установите данные для конфигурации
```python
from yandex_checkout import Configuration

Configuration.configure('<Идентификатор магазина>', '<Секретный ключ>')
```

или

```python
from yandex_checkout import Configuration

Configuration.account_id = '<Идентификатор магазина>'
Configuration.secret_key = '<Секретный ключ>'
```

или через oauth

```python
from yandex_checkout import Configuration

Configuration.configure_auth_token('<Oauth Token>')
```

Если вы согласны участвовать в развитии SDK, вы можете передать данные о вашем фреймворке, cms или модуле:
```python
from yandex_checkout import Configuration
from yandex_checkout.domain.common.user_agent import Version

Configuration.configure('<Идентификатор магазина>', '<Секретный ключ>')
Configuration.configure_user_agent(
    framework=Version('Django', '2.2.3'),
    cms=Version('Wagtail', '2.6.2'),
    module=Version('Y.CMS', '0.0.1')
)
```

3. Вызовите нужный метод API. [Подробнее в документации к API Яндекс.Кассы](https://kassa.yandex.ru/docs/checkout-api/)



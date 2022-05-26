[Russian](https://github.com/dkgitdev/yandex-checkout-sdk-python/blob/master/README.md) | English

# Yandex.Checkout API Python Client Library

This product is used for managing payments under old The Yandex.Checkout API
For usage by those who implemented Yandex.Checkout using the API method.

## Requirements
1. Python 2.7 or Python 3.x
2. pip

## Installation
### Under console using pip

1. Install pip.
2. In the console, run the following command:
```bash
pip install --upgrade yandex_checkout_ng
```

### Under console using easy_install
1. Install easy_install.
2. In the console, run the following command:
```bash
easy_install --upgrade yandex_checkout_ng
```

## Commencing work

1. Import module
```python
import yandex_checkout
```

2. Configure a Client
```python
from yandex_checkout import Configuration

Configuration.configure('<Account Id>', '<Secret Key>')
```

or

```python
from yandex_checkout import Configuration

Configuration.account_id = '<Account Id>'
Configuration.secret_key = '<Secret Key>'
```

or via oauth

```python
from yandex_checkout import Configuration

Configuration.configure_auth_token('<Oauth Token>')
```

If you agree to participate in the development of the SDK, you can submit data about your framework, cms or module:

```python
from yandex_checkout import Configuration
from yandex_checkout.domain.common.user_agent import Version

Configuration.configure('<Account Id>', '<Secret Key>')
Configuration.configure_user_agent(
    framework=Version('Django', '2.2.3'),
    cms=Version('Wagtail', '2.6.2'),
    module=Version('Y.CMS', '0.0.1')
)
```

3. Call the required API method.
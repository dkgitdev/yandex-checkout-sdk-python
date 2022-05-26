# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = """
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
"""

setup(
    name="yandex_checkout_ng",
    version="1.6.6",
    description="Yandex Checkout SDK Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dkgitdev/yandex-checkout-ng",
    author="Yandex.Money",
    packages=["yandex_checkout", "yandex_checkout.domain.request", "yandex_checkout.domain.response",
              "yandex_checkout.domain.notification", "yandex_checkout.domain.models", "yandex_checkout.domain",
              "yandex_checkout.domain.models.confirmation", "yandex_checkout.domain.models.confirmation.request",
              "yandex_checkout.domain.models.confirmation.response", "yandex_checkout.domain.models.payment_data",
              "yandex_checkout.domain.models.payment_data.request", "yandex_checkout.domain.common",
              "yandex_checkout.domain.models.payment_data.response", "yandex_checkout.domain.exceptions"],
    install_requires=["requests", "uuid", "urllib3", 'distro'],
    zip_safe=False,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)

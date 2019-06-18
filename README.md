Требования
----------

Необходимо иметь следующее установленные пакеты:

- python 3.5
- Google Chrome версия 62 и выше
- python3-dev
- libssl-dev
- libffi-dev

Установка тестового окружения для Linux
-----------------------------

Для установки требуемого тестого окружния требуется сделать следующее:

* Если виртуальная среда не создана, нужно создать
```
#!bash

virtualenv -p /usr/bin/python3.5 .pytest_venv
```

* Активировать виртуальную среду. Из папки среды выполнить:
```
#!bash

. bin/activate
```

* Установить зависимости
```
#!bash

pip install --trusted-host pypi.python.org -U -r requirements.txt
```

Установка тестого окружения под Windows
----------------------------

* Установка Python 3.5

```
https://www.python.org/downloads/release/python-350/
```

* Клонирование репозитория


* Создание виртуальной среды

```
virtualenv shop-saint-gobain
```

* Активация виртуальной среды

```
shop-saint-gobain\Scripts> .\activate
```

* Установка зависимостей

- Переходим в склонированый на локальный компьютер репозиторий.
```
\src> python.exe -m pip install -U -r requirements.txt
```

* Запуск тестов

```
\src> pytest -s -v .\shop_tests

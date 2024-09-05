# Запуск через pypi (src)

Переходим в /Лабораторная работа 1/src

```bash
pypi-server run -p 8081 pypi-packages
```

После открываем новый терминал и переходим в Лабораторная работа 1/src/other-project

Запускаем файл

```bash
python3 main.py
```

Ожидаемый результат:

```bash
(venv) ➜  other-project git:(main) ✗ python3 main.py

Hello, World!

Package         Version
--------------- -------
packaging       24.1
pip             24.2
printHelloWorld 0.1        <- My package
pypiserver      2.1.1
setuptools      74.1.2
termcolor       2.4.0
```

# Запуск без pipy (other-src)

Переходим в other-src/rootserver

```bash
python3 -m http.server
```

В другом окне терминала запустите файл activation_script.py

```bash
python3 -i activation_script.py
```

```bash
sys.path.append("http://localhost:8000")
import myremotemodule
myremotemodule.myfoo()
```

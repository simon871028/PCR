# PCR

## Clone 專案
**git clone**
```sh
user@computer-name:~$ git clone https://github.com/juck89724/PCR.git
```

**Python & Django 版本**
```sh
Python 3 以上
pip 19.3.1
Django 3 以上
```

**Plotly**
```sh
pip3 install plotly
```

以下為PCR專案底下做的事

**建置資料庫**
```sh
python3 manage.py makemigrations gantt
python3 manage.py migrate
```

**開啟專案**
```shell
python3 manage.py runserver
```

連線至 localhost:8000/create 後
回到 localhost:8000/ 即可
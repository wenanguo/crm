### 基础开发命令



###### 启动命令
```
python manage.py runserver --host 0.0.0.0
```

###### 测试命令
```
python manage.py test
```



---
### 数据库迁移

###### 初始化
```
python manage.py db init
```

###### 生成脚本
```
python manage.py db migrate -m "initial migration"
```

###### 更新数据库
```
python manage.py db upgrade
```

###### 代码性能分析
```
python manage.py profile  启动，浏览器请求
```

###### 服务器启动命令
```
gunicorn -b 0.0.0.0:8000  manage:app
```


UI框架

DOC http://spin.webkom.co/docs/docs.html



#### 打包
```
python setup.py sdist

twine upload dist/pyfw-1.0.6.tar.gz
```
### 基础开发命令



###### 启动命令
```
python manage.py runserver --host 0.0.0.0
```

###### 测试命令
```
python manage.py test
```

###### 覆盖报告
```
python manage.py test --coverage
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

对第一个迁移来说， 其作用和调用db.create_all() 方法一样。但在后续的迁移中，
upgrade 命令能把改动应用到数据库中，且不影响其中保存的数据。

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
python3 setup.py sdist bdist_wheel

twine upload  dist/*
```



#### 使用pip生成依赖文件：


```
pip freeze >requirements.txt
```



安装或升级包后，最好更新这个文件。

#### 根据依赖文件安装包：


```
pip install -r requirements.txt
```

### 移除所有包
```
pip freeze | xargs pip uninstall -y
```
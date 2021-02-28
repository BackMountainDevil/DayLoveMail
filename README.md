# DayLoveMail

## Mail

[发送邮件](mail.py)  
由于设计收发QQ和授权码的隐私问题，相关的信息保存在`.env`文件中，该文件默认被python的gitignore忽略，不会上传到repo。因此在使用该代码的时候你需要自己创建`.env`文件，并在文件中写入对应的数据，如（PWD为授权码，非QQ邮箱密码）  

```bash
QQ = '123456789'
PWD = '345adf456qsd0asd'
```


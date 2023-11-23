# 下载

Github [https://github.com/getsentry/self-hosted]

# 安装
## 安装
根目录下执行 ./install.sh
## 启动
根目录下执行 docker-compose up -d
# 配置
## 邮箱
config.yml
Mail Server 相关
```yaml
mail.host: 
mail.port: 
mail.username: 
mail.password: 
mail.use-tls: true
```

## HTTPS
sentry.conf.py
SSL/TLS 注释打开相关
```python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
```

# 文档
docs.sentry.io [https://docs.sentry.io/]
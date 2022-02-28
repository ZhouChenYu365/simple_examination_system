DEBUG = True
DOMAIN = ''
ALLOWED_HOSTS = ['*']
BANK_REPO = '/root/tmp/b'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exam',
        'USER': 'root',
        'PASSWORD': ''
    }
}
# send e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
# Email address that error messages come from.
# Default email address to use for various automated correspondence from
# the site managers.
SERVER_EMAIL = DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# People who get code error notifications.
# In the format [('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com')]
ADMINS = [(),]
# Not-necessarily-technical managers of the site. They get broken link
# notifications and other various emails.
MANAGERS = ADMINS


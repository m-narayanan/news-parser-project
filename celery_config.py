from celery import Celery

app = Celery('news_pro')
app.config_from_object('celeryconfig')

if __name__ == '__main__':
    app.start()
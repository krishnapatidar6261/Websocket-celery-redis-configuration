from celery import shared_task
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

#ensure that your redis server is runing

@shared_task
def run_task(name):    
    r.set(f"name:{name}", name)
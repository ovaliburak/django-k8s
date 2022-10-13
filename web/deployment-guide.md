1- Test Django 
```
python3 manage.py test
```

2- Build Container

```
docker build -t burakovali/django-k8s:latest .
```

3- Push Container to Docker Hub

```
docker push burakovali/django-k8s:latest
```

4- Update Secrets

5- Update Depyloyments

6- Wait for Rollouts to Finish
```
kubectl rollout status deployment/django-k8s-web-deployment
```
7- Migrate Database 

```
kubectl exec -it <podname> -- /bin/bash
sh migrate.sh
```

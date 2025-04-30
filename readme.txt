prerequisites:
- minikube
- ngrok
- kubectl
- python

steps:
- minikube start
- run "webhook_listener.py"
- ngrok http 5000
- setup dockerhub webhook using *ngrok-url*/dockerhub-webhook
- kubectl apply -f deployment.yaml
- push new image on dockerhub for updating the deployment 
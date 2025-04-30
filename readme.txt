Prerequisites:
- minikube
- ngrok
- kubectl
- python

Steps:
- minikube start
- run "webhook_listener.py"
- ngrok http 5000
- Setup dockerhub webhook using *ngrok-url*/dockerhub-webhook
- kubectl apply -f deployment.yaml
- Push new image on dockerhub for updating the deployment 

kubectl apply -f kubernetes/persistent-volume.yml
kubectl apply -f kubernetes/persistent-volume-claim.yml


echo "Creating the database credentials..."

kubectl apply -f kubernetes/secret.yml


echo "Creating the postgres deployment and service..."

kubectl create -f kubernetes/postgres-deployment.yml
kubectl create -f kubernetes/postgres-service.yml



echo "Creating the flask deployment and service..."

kubectl create -f kubernetes/flask-deployment.yml
kubectl create -f kubernetes/flask-service.yml


kubectl create -f kubernetes/ui-deployment.yml
kubectl create -f kubernetes/ui-service.yml
kubectl create -f kubernetes/devicemanagement-deployment.yml
kubectl create -f kubernetes/devicemanagement-service.yml
kubectl create -f kubernetes/usermanagement-deployment.yml
kubectl create -f kubernetes/usermanagement-service.yml


echo "Adding the ingress..."

minikube addons enable ingress
kubectl apply -f kubernetes/minikube-ingress.yml


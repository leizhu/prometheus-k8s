kubectl create configmap pg-exporter-configmap --from-file=queries.yaml
kubectl create -f node-exporter.yaml
kubectl create -f node-service.yml
kubectl create -f postgres-exporter.yaml
#kubectl create -f pgpool-exporter.yaml
kubectl create configmap kafka-jmx-exporter-config --from-file=kafka-0-8-2.yml         
kubectl create -f kafka-jmx-exporter.yaml   
kubectl create -f kafka-exporter.yaml
kubectl create -f redis-exporter.yaml
kubectl create -f prometheus-service.yml
kubectl create -f prometheus-configmap.yaml
kubectl create -f prometheus-deployment.yaml

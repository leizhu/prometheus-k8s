kubectl delete configmap pg-exporter-configmap 
kubectl delete -f prometheus-configmap.yaml
kubectl delete -f prometheus-deployment.yaml
kubectl delete -f prometheus-service.yml
kubectl delete -f node-exporter.yaml
kubectl delete -f node-service.yml
kubectl delete -f postgres-exporter.yaml
#kubectl delete -f pgpool-exporter.yaml
kubectl delete -f kafka-exporter.yaml
kubectl delete -f redis-exporter.yaml
kubectl delete configmap kafka-jmx-exporter-config 
kubectl delete -f kafka-jmx-exporter.yaml   

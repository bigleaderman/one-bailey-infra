#!/bin/bash

helm repo add influxdata https://helm.influxdata.com/
helm repo update

helm install influxdb influxdata/influxdb2 \
  --version 2.1.1 \
  --namespace db --create-namespace \
  -f influxdb-values.yaml

# Chapter 9 - Scalable Inference Serving on Cloud with TensorFlow Serving and KubeFlow

Note: All images in this directory, unless specified otherwise, are licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

## Figure List

| Figure number | Description | Notes |
|:---|:---|:---|
| [9-1](1-stacks-chart.png) | A high-level overview and comparison of different inference serving options | |
| [9-2](2-flask-hello-world.png) | Navigate to http://localhost:5000/hello within a web browser to view the “Hello World!” web page | |
| [9-3](3-mlmodels-listing.png) | Listing page for machine learning models on the Google Cloud ML Engine dashboard | |
| [9-4](4-model-creation-page.png) | Model creation page on Google Cloud ML Engine | |
| [9-5](5-models-listing-page.png) | Model listings page on Google Cloud ML Engine | |
| [9-6](6-model-detail-page.png) | Details page of the just-created Dog/Cat classifier | |
| [9-7](7-cloudml-model-create-version.png) | Creating a new version for a machine learning model | |
| [9-8](8-creating-storage-bucket.png) | Creating a new Google Cloud Storage bucket within the ML model version creation page | |
| [9-9](9-bucket-details.png) | Google Cloud Storage Browser page showing the uploaded Dog/Cat classifier model in TensorFlow format | |
| [9-10](10-uri-gcs.png) | Add the URI for the model you uploaded to Google Cloud Storage | |
| [9-11](11-kubeflow-pipeline.png) | An end-to-end pipeline illustrated in KubeFlow | |
| [9-12](12-kubeflow-notebook-server.png) | Creating a new Jupyter Notebook server on KubeFlow | |
| [9-13](13-kubeflow-creation-obfuscated.png) | Creating a KubeFlow deployment on GCP using the browser | |
| [9-14](14-model-monitoring.png) | Google Cloud ML Engine showing incoming queries and latency of serving the calls, with end-to-end latency at user’s end of about 3.5 seconds | |
| [9-15](15-cost-vs-qps-gcml-byos.png) | Cost comparison of infrastructure as a service (Google Cloud ML Engine) versus building your own stack over virtual machines (Azure VM) (costs as of August 2019) | |
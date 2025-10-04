# Hands-on GCP DevOps Spring 
## Project Overview 
This project is a **hands-on lab** designed to demostrate **modern DevOps methodologies** in the context of **cloud-native applications**. Originally inspired by workflows for deploying Python Flask applications, this lab **replace the Python app with a multi-module Spring Cloud Native project**, providing a realistic simulation of enterprise DevOps pipelines. 

The goal is to give developers and cloud engineers **practical experience in deploying**, **scaling**, and **managing microservices on Google Cloud Platform (GCP)** while leveraging key DevOps principles. 

## Project Background 
In modern software delivery, **end-to-end automation** and **cloud-native practices** are crucial for fast, reliable, and maintainable deployments. This lab simulates a real-world scenario where developers must: 
- Manage multiple microservices in a modular architecture
- Handle routing and API gateway responsibilities
- Implement CI/CD pipelines to automate builds, tests, and deployments
- Use cloud-native tools for orchestration, monitoring, and resource management

By transitioning from a Flask/Python approach to a **Spring Boot** + **Spring Cloud project**, this lab emphasizes **Java cloud-native development** while still teaching core DevOps skills. 

## Key Technologies
- **Spring Boot** & **Spring Cloud Gateway** - Modular microservices with routing and gateway capabilities
- **Jib** - Containerless packaging for building and publishing Docker images directly from Java projects
- **Redis** - In-memory caching solution for high-performance microservices
- **GKE (Google Kubernetes Engine)** - Kubernetes orchestration for deploying and managing microservices
- **GCP Google Cloud Build & GitHub Actions** - Continuous Integration and Deployment pipelines
- **Terraform** - Infrastructure-as-Code for provisioning cloud resources
- **CI/CD Concepts** - Full DevOps lifecycle impelmentation including versioning, automated builds, and deployment pipelines

## Project Structure 
The project follows a **parent-child Maven structure**:
- **Parent project**: Manages dependencies and versions centrally
- **Modules**: Independent microservices packaged via Jib
- **Gateway module**: API gateway for routing and service discovery
- **Kubernetes manifests**: Define deployments, services, and namespaces
- **Terraform scripts**: Optional provisioning of GCP resources like GKE clusters, Redis, and Cloud Build triggers

## Learning Outcomes 
- Gain hands-on experience in **GCP DevOps workflows**
- Learn how to **structure multi-module Spring Boot projects** for cloud-native deployments
- Understand **API gateway routing patterns** with Spring Cloud Gateway
- Deploy applications using **containerless builds via Jib**
- Implement **CI/CD pipelines** integration **GitHub** and **GCP Cloud Build**
- Configure **Redis caching** for microservices
- Master **Kubernetes deployment concepts**, including namespaces, scaling, and service validatoin
- Leverage **Terraform for infrastructure provisioning**

## Why This Project Matters 
This lab bridges the gap between academic exercises and **real-world enterprise DevOps practices**. It equips developers with practical experience in cloud-native application design, scalable microservice architecture, and automated deployments, all focused on **GCP** and **Java ecosystems**.

Whether aiming for roles such as **DevOps engineer**, **cloud-native developer**, or **Java backend developer**, this project highlights key enterprise-ready skills employers look for: **automation**, **scalability**, **cloud deployment expertise**, and **microservice architecture**. 


## References 
- [Google Cloud Documentation](https://cloud.google.com/docs)
- [Google Kubernetes Engine Documentation](https://cloud.google.com/kubernetes-engine/docs)
- [KodeKloud: GCP DevOps Project](https://learn.kodekloud.com/user/courses/gcp-devops-project)
- [Google Cloud and HashiCorp](https://github.com/terraform-google-modules)
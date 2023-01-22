# Wave 1 - Application definition and development

This prototype is composed of tools specialized in the definition and continuous delivery of new software versions in container environments.

It is important to mention that there are numerous strategies and with a different composition of tools that fulfill this role.

__Software Requirements:__

Tool | Version
:----|:-------
Docker-desktop | ```4.15.0```
DockerHub account | _None_
Docker engine | ```20.10.21```
ArgoCD | ```2.5.7```
Backstage | ```1.10.1```
Dummy-application | _None_
Yarn | ```1.22.19```
NodeJS | ```v16.18.0```
Helm | ```v3.8.0+gd141386```
Kustomize | ```v4.5.7```
Kubernetes Server | ```v1.25.2```
Kubernetes Client | ```v1.25.2```


Get starting ```Dummy-application``` in local environment:

1. Pull docker image
```bash
docker pull 8eab29e/wave-1:v1.0
```

2. Running container
```bash
docker run --name=dummy-app -p :8080 8eab29e/wave-1:v1.0
```
3. Testing connection
```bash
curl -iv http://localhost:8080/ping
```

Output:

```bash
'pong'
```

__DoR - Definiton of Ready__

- Automated release process

> The above definition nicely summarizes the following steps in building a deployable version:
> - Development and construction process. 
> - Building the container image. 
> - Launching the application version in the environment.

__Diagram__

![image](https://user-images.githubusercontent.com/99411965/213672667-e492bc12-2242-4bcd-a115-0fd7a1973e30.png)

__DoD - Definition of Done__

- Automatic deployment of a release in a container environment.
- Automatic synchronization of the application when it detects any difference between the repository and the target cluster.

# Make it yourself 💡 

```
Before anything, clone this project.
```
First, start ```Backstage```. for this:

- Go to project directory.

```bash
cd devops-tools/backstage/app
```

 - Dependecies install.

```bash
yarn install
```

- Start Backstage application

```bash
yarn dev
```

Second, GitOps tool install, in this case ```ArgoCD```. For this:

- Add ArgoCD repo.

```bash
helm repo add argo https://argoproj.github.io/argo-helm
```

- Create ArgoCD namespace
```bash
kubectl create ns argocd
```

- Implement ArgoCD charts

```bash
helm install gitops argo/argo-cd --version 5.19.3 -n argocd
```

- ArgoCD service expose

```bash
kubectl port-forward svc/gitops-argocd-server -n argocd 8000:80 &
```

- Login to ArgoCD

Before, you need to get password in a secrets:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

```bash
argocd login localhost:8000
```

output:

```bash
Username: admin <--- ArgoCD default user
Password:
Handling connection for 8000
'admin:login' logged in successfully
Context 'localhost:8000' updated
```
# Pin points 🚧 

Item | Component |Description
:----|:----------|:-----------
Config as-a-code|ArgoCD|Create new application, external cluster connection, configure projects, LDAP service integration and connect repo.
Branching|Backstage|Support to multi-branches (e.g Staging and Production) and protection branch (minimal reviewer with approval process).
Manifests|Repo|Manifest update, e.g tag image, replicas or resources.

# Parking lot  ⚠️ 

- Strategy for defining ArgoCD projects.
- Define where to deploy Argocd, e.g _K8s cluser - common service_.
- Define convention to: _project name_ and _application name_.


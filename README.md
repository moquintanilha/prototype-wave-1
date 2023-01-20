# Getting Starting

This prototype is composed of tools specialized in the continuous delivery of new versions of software in container environments.

It is important to mention that there are numerous strategies and with a different composition of tools that fulfill this role.

__Software Requirements:__

Tool | Version
:----|:-------
Docker-desktop | ```4.15.0```
DockerHub account | _None_
Docker engine | ```20.10.21```
ArgoCD | ```2.5.4```
Backstage | ```1.10.1```
Dummy-application | _None_

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


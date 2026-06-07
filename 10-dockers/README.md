# Dockers

1. What is Docker
2. What are containers
3. Containers vs. Virtual Machine
4. Docker image vs container
5. Practical implmentation of Dockers


## What are containers and why to use them?

It works on machine

- Developer -> QA 
> Developer A (Windows)
> Developer B (Linux) Says doesn't work on my machine
> QA Says doesn't work on my machine
The library mismatch issue. 


### Conatiners
A way to package application with all the necessary dependencies and configurat ion. 

Protable Artifact: Easily share and move this package to any environment

This makes the development and deployment easy and efficient. 


Ex: House A to House B 
House A: tv, machine, clothes, etc
If we move each and every item one by one there are chances that we may miss something. So what we do is, we pack all these things in the House A and will unpack them in House B


### What is Docker
- Docker is an open platform for developing shipping, and running applications. 
- Docker enables you to separate your application from your infrstructure so you can deliver software quickly. 
- With Docker, you can manage your infrastructure in the same ways you manage your applications. 
- By taking advantage of Docker's methodologies for shipping, testing and deploying code quickly, you can significantly reduce the delay between writing code and running in production. 


### Docker Image and Containers
Container: Layers of Images, Let's the Base image be linux
Application: Mysql/mongodb


Docker Image: Package or Artifact (Shareable)
Docker Container: Executes Docker Image by Starting the application -> Creates a container (Environment) -> Runs it


### Docker vs. Vitual Machine

Docker 

|Application(Docker)|
--------------------
|   OS Kernel       |
|   Hardware        |
---------------------

VM 

----------------
|Application(VM)|
|   OS(VM)      |
-----------------
|   Hardware    |
-----------------

Docker Image is Smaller usually in MBs
VM size will be huge GBs


Compatability:
VM can run on any OS
Docker images: compatability issues


### Docker Installation
- Enable Virtualization (Turn Windows Features on or off)
- Install Docker Desktop

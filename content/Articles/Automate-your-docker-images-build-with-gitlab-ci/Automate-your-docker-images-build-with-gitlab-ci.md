# Automate your docker Images build with Gitlab CI

I want to fully automate the deployment of one of my servers using Ansible. I want it to be Test Driven, and I want my tests to be fast.
My server is a Centos 7 and I want to be able to deploy docker containers on it.

The first step of this new projet is to build and use a docker container that can be used as a "development environment", and since I will most probably modify it quite a few times in the following weeks I want my image to be built and tested automatically.

So, to do it, let's use Gitlab CI ! The overall process is as follow:

<TODO: Rajouter un schéma>

je commit sur mon poste, ça pousse sur gitlab, j'ai la CI qui se met en route et pousse sur la registry du Hub Docker

## 1/ Prepare your Dockerfile

My Dockerfile is quite simple, i am pretty sure it is not the best but at least it works:

    FROM centos:7

    ENV container docker

    RUN yum -y install sudo procps-ng net-tools iproute iputils wget docker docker-compose && yum clean all

    RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
    systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    rm -f /lib/systemd/system/multi-user.target.wants/*;\
    rm -f /etc/systemd/system/*.wants/*;\
    rm -f /lib/systemd/system/local-fs.target.wants/*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*;\
    rm -f /lib/systemd/system/anaconda.target.wants/*;\
    rm -f /lib/systemd/system/*.wants/*update-utmp*;

    # https://www.freedesktop.org/wiki/Software/systemd/ContainerInterface/
    STOPSIGNAL SIGRTMIN+3

    CMD ["/sbin/init"]

## 2/ Build, Run, Test & Push your container

Make sure the build is working:

    $ docker build --tag silefort/docker-ci-dind .

Make sure it can be ran properly:

    $ docker run -id -v /sys/fs/cgroup -v /var/lib/docker --privileged --name docker-ci-dind silefort/docker-ci-dind

Lets use docker within docker to test our image ( first start the docker daemon within our container, then run an hello-world container to make sure it works)

    $ docker exec docker-ci-dind systemctl start docker && docker run hello-world

Finally, let's push our new image to docker hub so that it can be pulled. To do that you need an account on hub.docker.com

    $ docker login -u <username>
    $ docker push silefort/docker-ci-dind:latest

## 3/ Prepare your CI file

What we have right now is a working container that can be built, ran, tested and pushed to a registry, we just need to automate the process so that we don't have do to it manually everytime we change something

Let's add a new .gitlab-ci.yml file to our Gitlab repo:

	---
	image: docker:19.03.1

	variables:
		CI_REGISTRY_IMAGE: silefort/docker-ci-dind

	services:
		- docker:19.03.1-dind

	before_script:
		- docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD

	build:
		stage: build
		script:
			- docker pull $CI_REGISTRY_IMAGE:latest || true
			- docker build --cache-from $CI_REGISTRY_IMAGE:latest
										 --tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
										 --tag $CI_REGISTRY_IMAGE:latest .
			- docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
			- docker push $CI_REGISTRY_IMAGE:latest


This CI file will run within a container, login to your docker account, build and push your image

## 4/ Add your credentials

To make it work you need to add the necessary variables ( CI_REGISTRY_IMAGE, CI_REGISTRY_USER, CI_REGISTRY_PASSWORD).
CI_REGISTRY_IMAGE can be added directly in the CI file but your password but be stored elsewhere, Gitlab allows to add "protected" variables that can be used by the runners without exposing it in your .gitlab-ci.yml file

To do so, just go to your gitlab repo, and then "Settings" / "CI/CD" / "Variables", you can then add:

CI_REGISTRY_USER and CI_REGISTRY_PASSWORD variables ( do not forget to "Mask" those values)

## 5/ Build your container and push it

Just push your new .gitlab-ci.yml file to your repo and it should start a new build job. Jobs can be check in "CI/CD" / "Jobs"

## 6/ Add a Test stage after the build to make sure it still works

Edit your .gitlab-ci.yml file to add the following:

		test:
			stage: test
			script:
				- docker pull $CI_REGISTRY_IMAGE:latest
				- docker run -id -v /sys/fs/cgroup -v /var/lib/docker --privileged --name docker-ci-dind $CI_REGISTRY_IMAGE
				- docker ps
				- docker exec docker-ci-dind yum install -y docker
				- docker exec docker-ci-dind systemctl start docker
				- docker exec docker-ci-dind docker info
				- docker exec docker-ci-dind docker run hello-world

As you can see, the only thing we do here is pull back the container we just built, run it and exec a few things in it to make sure everything works properly

That's it, you now have a complete CI that build a new container version for you everytime you make any modification to your Dockerfile


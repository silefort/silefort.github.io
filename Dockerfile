FROM centos:7

WORKDIR '/app'

# Update the package repos and install epel-release
RUN yum makecache
RUN yum install -y epel-release
RUN yum makecache

# Install necessary packages
RUN yum install -y  python3-pip \
                    python36 dev \
                    make

RUN export LC_ALL="en_US.UTF-8"

# Install Pelican and dependencies
RUN pip3 install pelican==4.2.0      \
                markdown     

COPY . .
EXPOSE 80

CMD ["pelican","--listen","-p","80","-b","0.0.0.0"]

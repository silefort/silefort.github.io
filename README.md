# Tech this Out

This repo is used to build and host my personal Tech Blog on github pages

* I use pelican ( https://blog.getpelican.com/ ) to build the html pages
* I use TravisCI to deploy it ( https://travis-ci.org/ )

## Development Process:

### Build the development container

    $ docker build -t pelican .

### Run your development container

    $ docker run --rm -di -p 80:80 -v $(pwd):/app --name pelican pelican

### Quickstart your website ( you will do it only once to setup your pelican project)

Follow the instructions provided, it will create the files/directories structure needed

    $ docker exec -ti pelican pelican-quickstart

### Update your website

Once you've worked on your website (mostly working with markdown pages and pelicanconf ), you can update your html pages using the following command:

    $ docker exec pelican pelican content -o output -s publishconf.py

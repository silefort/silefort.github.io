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

Here is an example of my answers during the process:

```
Please answer the following questions so this script can generate the files
needed by Pelican.


Where do you want to create your new web site? [.]
> What will be the title of this web site? Tech This Out
> Who will be the author of this web site? Simon
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) https://silefort.github.io
You must answer 'yes' or 'no'
> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) y
> What is your URL prefix? (see above example; no trailing slash) https://silefort.github.io
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10]
> What is your time zone? [Europe/Paris]
> Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) N
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
> Do you want to upload your website using Rackspace Cloud Files? (y/N) N
> Do you want to upload your website using GitHub Pages? (y/N) N
> Done. Your new project is available at /app
```

### Update your website

Once you've worked on your website (mostly working with markdown pages and pelicanconf ), you can update your html pages using the following command:

    $ docker exec pelican pelican content -o output -s publishconf.py

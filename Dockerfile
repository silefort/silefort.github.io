FROM python:3.9.19

WORKDIR '/app'

RUN export LC_ALL="en_US.UTF-8"

# Install Pelican and dependencies
RUN pip3 install pelican==4.9.1      \
                markdown     

COPY . .
EXPOSE 80

RUN make html

CMD ["make","serve-global","PORT=80"]

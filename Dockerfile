# set base image
FROM python:3.8-alpine

# add make to python alpine image
RUN apk add --update make

# set
WORKDIR app

# copy the content of the local src directory to the working directory
ADD MANIFEST.in .
ADD setup.py .
ADD hacktoberfest_jems/ hacktoberfest_jems/
ADD Makefile .

# install dependencies
RUN make install

# command to run on container start
CMD [ "hacktoberfest_jems"]
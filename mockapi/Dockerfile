FROM node:7
RUN npm install -g drakov
ADD . /wd
WORKDIR /wd
CMD drakov -f "api_heritages.md" -p 3000 --public
EXPOSE 3000

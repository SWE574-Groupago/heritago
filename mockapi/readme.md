# Api Blueprint For Heritago REST Api

Api documentation can be found [here](api_heritages.md)

# Mock Server Installation

## Using Npm

+ Requirements
  + Node.js and Npm [how to install](https://docs.npmjs.com/getting-started/installing-node)

1. Open CLI and navigate to this folder
2. Run `npm install -g drakov`
3. After installation is done run `drakov -f "api_heritages.md" -p 3000`

You should be able to get an example json at `http://0.0.0.0:3000/heritages`

## Using Docker

+ Requirements
  + Docker [how to install](https://docs.docker.com/engine/installation/)

1. Start docker
2. Open CLI and navigate to this folder
3. Run `docker build -t heritago/mockapi .`
4. After image is built run `docker run -itd -p 3000:3000 --name mockapi heritago/mockapi`

You should be able to get an example json at `http://0.0.0.0:3000/heritages`

To see running containers `docker ps -a` <br>
To stop docker container `docker stop mockapi` <br>
To delete docker container `docker rm mockapi` <br>

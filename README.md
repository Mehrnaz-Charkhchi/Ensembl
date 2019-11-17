### Search interface

- Connect to a Mysql app using Flask.
- Search in Mysql and retrieve data.
- Rest API is provided



## Pre-requirements
Install docker and docker compose:
https://docs.docker.com/compose/install/

## How to deploy for development
Run in terminal:
`$ git clone https://github.com/Mehrnaz-Charkhchi/Ensembl.git`
`$ cd Ensembl`
`$ sudo docker-compose -f docker-compose.yml up`
To run as a demon run:
`$ sudo docker-compose -f docker-compose.yml up -d`

## Swagger interface
[Swagger API interface can be accessed via url:][1]

[1]: http://0.0.0.0:5000/api/

## API interface

[API interface can be accessed via url:][2]

[2]: http://0.0.0.0:5000/api/genes?lookup=BRCA2&species=aotus_nancymaae

## How to run unit tests
`$ sudo docker exec -it ensembl_flask python -m unittest`


### End

## Search interface

- Connect to a Mysql app using Flask.
- Search in Mysql and retrieve data.
- Rest API and Swagger interface is provided



## Pre-requirements
[Install docker and docker compose][3]

[3]: https://docs.docker.com/compose/install/

## How to deploy for development
Run in terminal:
- `$ git clone https://github.com/Mehrnaz-Charkhchi/Ensembl.git`
- `$ cd Ensembl`
- `$ sudo docker-compose -f docker-compose.yml up`
- To run as a demon run:
- `$ sudo docker-compose -f docker-compose.yml up -d`

## Swagger interface
[Swagger API interface][1]

[1]: http://0.0.0.0:5000/api/

## API interface

[API interface][2]

[2]: http://0.0.0.0:5000/api/genes?lookup=BRCA2&species=aotus_nancymaae

## How to run unit tests
`$ sudo docker exec -it ensembl_flask python -m unittest`


### End

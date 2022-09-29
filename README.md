# Part 1: Minimum Requirements
### Overview
The `IngestLocal.py` script satisfies the two minimum requirements of the exercise. Before execution, make sure that either `pyarrow` or `fastparquet` is installed in the environment with pip, as one will be necessary for the conversion to parquet. The output after execution will be a `countries.db` file, where the sqlite database data is stored, and an `output.parquet` file for the database.

### Notes
The schema used is a partially normalized version of [Countries Query](https://trevorblades.github.io/countries/queries/countries). The unicode emoji and states fields have been ommitted due to high duplication in normalized form, but could be included later. 

# Part 2: Seperate Tables and Containerisation
### Overview


docker build -t country_db:v1 .
docker run -v "/C/Users/Forest Yang/Documents/InDebted":"/project" -it country_db:v1


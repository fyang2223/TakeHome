# Part 1: Minimum Requirements
### Instructions
The `IngestLocal.py` script satisfies the two minimum requirements of the exercise. Before execution, make sure that either `pyarrow` or `fastparquet` is installed in the environment with pip, as one will be necessary for the conversion to parquet. The output after execution will be a `countries.db` file, where the sqlite database data is stored, and an `output.parquet` file for the database.

### Notes
The schema used is a partially normalized version of [Countries Query](https://trevorblades.github.io/countries/queries/countries). The unicode emoji and states fields have been ommitted due to high duplication in normalized form, but could be included later. 

# Part 2: Seperate Tables and Containerisation
### Instructions
Now splitting the single table into four, we have the `countries`, `currency`, `languages` and `continents` tables. The primary key for the `countries` table is `code`, which is referenced as a foreign key by the three other tables with the name `country_code`. To run the script, execute the following.

```
docker build -t country_db:v1 .

# In the following, replace pwd with the path of the current working directory of this repository.

docker run -v pwd:/project -it country_db:v1
```

An sqlite database file named `multitable_countries.db` will be written to the the present directory, containing the four tables.

# Part 3: AWS Implementation
Due to the small size and short runtime of the script, one of the least expensive and quickest options would be to migrate the scripts into Lambda, either by sending the packaged code and dependencies to AWS or by using a public lambda image such as `public.ecr.aws/lambda/python:3.9` if the package exceeds size limits. If only a `.db` file is required, the database can be held in lambda's temporary storage, but the number of concurrent lambda instances will need to be set to 1.
A much more robust option is to use a python script in Glue and output to either Redshift or RDS, which has the advantage of being more scalable due to its longer maximum runtime and would be a benefit should the amount of data ingested increase. These services would all need to be run in a private subnet with a NAT gateway for security and to allow Glue to access the API over the internet. 
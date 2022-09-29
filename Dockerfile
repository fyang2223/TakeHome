FROM python:3.9

RUN pip install -U pip
RUN pip install requests fastparquet

WORKDIR /project

# VOLUME ["/project/data"]

COPY [ "CreateTables.py", "IngestData.py", "IngestMultiTable.py", "IngestLocal.py", "/project/" ]

CMD [ "python3", "IngestMultiTable.py" ]
🎯 Objective : This application ingest medical data provided in CSV format to Mongodb by converting the file in json.

The project involves first analyzing the CSV file structure to propose an appropriate MongoDB data model. This includes identifying relevant fields, deciding between embedding or referencing documents.

Next, a multi-container environment is set up using Docker Compose. The setup includes a Python container with required libraries such as pymongo and pandas, a MongoDB container configured with credentials, and a shared volume (./data) for the CSV files.

The Python ETL script watches the mounted folder for new CSV files, converts them to JSON, performs necessary data transformations, then inserts the processed data into MongoDB.

Once the data is loaded, Mongosh is used to query and manipulate the data, enabling analysis such as counting patients, filtering by admission dates, examining medical conditions, and calculating medication usage frequencies.
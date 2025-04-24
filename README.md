# Data-transformations-castor
Castor - home assigment - python script used to demonstrate data transformation skills


### Running script

After pulling repoistory you should have install uv - https://docs.astral.sh/uv/getting-started/installation/
Then you can run this commands

```bash
uv install
uv run main.py user_sample.csv transformed_data.csv
```

Note that you need to provide filename of input csv file which should reside in data/input directory

### Scalability

1. Reading input file in chunks
2. Using parquet files instead of csv
3. Using other tools/services like Apache spark
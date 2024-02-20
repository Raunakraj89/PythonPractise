# This PYSpark program reads the data from BQ table and perform sum of salary and write the results in GCS bucket

from pyspark.sql import SparkSession
import pandas
spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('spark-bigquery-demo') \
  .getOrCreate()

bucket = "temp_bucket_for_practise"
spark.conf.set('gs://temp_bucket_for_practiset', bucket)

# Load data from BigQuery.
empdata = spark.read.format('bigquery') \
  .option('table', 'strategic-hull-412800.EMP_dataset.empdata') \
  .load()
empdata.createOrReplaceTempView('empdata')

# Perform sum of salary.
result = (empdata.groupby('dept_name')['salary'].sum())

# Save the data to GCS
result.saveAsTextFile('gs://temp_bucket_for_practise')

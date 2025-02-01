import os
from pyspark.sql import SparkSession
from duckdb import DuckDBPyConnection
import duckdb

def create_spark_session():
    """Creates a PySpark session."""
    return SparkSession.builder \
        .appName("PySpark-DuckDB Demo") \
        .config("spark.jars.packages", "org.duckdb:duckdb_jdbc:0.9.0") \
        .getOrCreate()

def create_duckdb_connection():
    """Creates a DuckDB connection."""
    return duckdb.connect(database=':memory:')


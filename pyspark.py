import sys
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import pyspark

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


def main(argv):
  print("hello")


if __name__ == '__main__':
    # If user want to test OBS, please input OBS path, ak, sk and endpoint.
    main(sys.argv)
    print("Success")

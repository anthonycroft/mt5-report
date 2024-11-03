import pandas as pd


if __name__ == '__main__' and __package__ is None:
  from os import sys, path
  # __file__ should be defined in this case
  PARENT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
  sys.path.append(PARENT_DIR)

from data.cleaner import clean

path = 'C:\\Users\\tonyj\\OneDrive\\Documents\\Trading\\synergy\\data.csv'

def main():
  # Load the data
  data = pd.read_csv(filepath_or_buffer=path, sep=',')
  clean(data)

if __name__ == "__main__":
    main()  # execute only if run as a script

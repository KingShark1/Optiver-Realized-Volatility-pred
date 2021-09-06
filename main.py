import savepoints
import os

def unpack(path):
  # Unpacks the data file if not already unpacked
  filepath = os.path.join(path, "Dataset/optiver-realized-volatility-prediction.zip")
  import zipfile
  with zipfile.ZipFile(filepath, 'r') as zep_ref:
    zep_ref.extractall(path + '/Dataset')

def pathname(path):
  pathnames = []

  return 
def main():
  # Prints working directory of current file
  PATH = os.path.dirname(os.path.abspath(__file__))
  
  unpack(PATH)
  
  print('Unpacked Successfully!')

if __name__=='__main__':
  main()
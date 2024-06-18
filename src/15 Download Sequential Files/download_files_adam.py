import urllib.request, urllib.error, os
from urllib.parse import urlparse
import re

def increment_val(stringVal, num):
  strLen = len(stringVal)
  strNum = str(num)
  if len(strNum) < strLen:
    #Add zeros
    numZeros = strLen - len(strNum)
    for i in range(numZeros):
      strNum = '0' + strNum
  return strNum

def download_files(firstUrl, downloadPath):
  parsed = urlparse(firstUrl)
  fileName = parsed.path.split('/')[1]
  matchedVal = re.findall(r'\d+',fileName)
  if not os.path.exists(downloadPath):
    os.makedirs(downloadPath)
  #print(matchedVal)
  if(len(matchedVal)) > 0:
    fileDownloaded = True
    x = 0
    while fileDownloaded:
      for val in matchedVal:
        newVal = int(val) + x
        dFileName = fileName.replace(val, increment_val(val, int(newVal)))
      try:
        with urllib.request.urlopen(parsed.scheme + '://' + parsed.netloc + '/' + dFileName) as u:
          print("Downloading file: " + dFileName)
          with open(downloadPath + '\\' + dFileName, 'wb') as f:
            f.write(u.read())
      except urllib.error.HTTPError as hErr:
        if hErr.code == 404:
          fileDownloaded = False
          print("File " + dFileName + " not found!")
        else:
          raise hErr
        
      x = x + 1
      
  

if __name__ == '__main__':
  download_files('http://699340.youcanlearnit.net/image001.jpg', './images')
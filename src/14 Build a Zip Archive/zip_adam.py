from pathlib import Path
from zipfile import ZipFile

def zip_all(folderPath, extensions, zipFileName):
  folder = Path(folderPath)

  zipList = []

  if not folder.exists():
    raise "FolderPath does not exist"

  for ext in extensions:
    pattern = '**/*' + ext
    for fl in folder.glob(pattern):
      print("Adding file to zip: " +fl.name)
      zipList.append(fl)

  if len(zipList) > 0:
    with ZipFile(zipFileName, 'w') as newZip:
      for fl in zipList:
        newZip.write(fl)
  else:
    raise "No files found to zip"


if __name__ == '__main__':
  zip_all('my_stuff', ['.jpg', '.txt'], 'my_stuff.zip')
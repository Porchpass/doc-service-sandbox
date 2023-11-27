def write_file(file_path: str, content: str):
  f = open(file_path, 'w')
  f.write(content)
  f.close()
  print('file written to ' + file_path)
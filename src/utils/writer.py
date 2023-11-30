def write_file(file_path: str, content: str, mode: str = 'w') -> None:
  f = open(file_path, mode)
  f.write(content)
  f.close()
  print('file written to ' + file_path)
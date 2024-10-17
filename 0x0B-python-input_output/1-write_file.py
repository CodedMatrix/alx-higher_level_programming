def write_file(filename="", text=""):
  """Writes a string to a UTF-8 encoded text file and returns the number of characters written.

  Args:
      filename: The name of the file to write to. Defaults to "".
      text: The string to write to the file. Defaults to "".

  Returns:
      The number of characters written to the file, or 0 if there was an error.
  """

  try:
    # Open the file in write mode with UTF-8 encoding using 'with' statement
    with open(filename, "w", encoding="utf-8") as file:
      # Write the text to the file
      written_chars = file.write(text)
  except (IOError, OSError):
    # Handle potential file system errors
    written_chars = 0
  
  return written_chars

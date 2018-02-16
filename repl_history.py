import readline

def write_history_to_file(filename):
  with open(filename, "w") as output_file:
    for line in range(readline.get_current_history_length()):
      output_file.write(readline.get_history_item(line + 1))
      output_file.write("\n")


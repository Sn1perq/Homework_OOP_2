import os
def sort_files_by_lines(directory):
  files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f != 'main.py']
  files.sort(key=lambda f: len(open(os.path.join(directory, f)).readlines()))
  return files
def merge_files(directory, output_file):
  with open(output_file, "w") as outfile:
    for filename in sort_files_by_lines(directory):
      filepath = os.path.join(directory, filename)
      with open(filepath, "r") as infile:
        lines = infile.readlines()
        outfile.write(f"{filename}\n{len(lines)}\n")
        outfile.writelines(lines)
if __name__ == "__main__":
  directory = "."
  output_file = "merged.txt"
  merge_files(directory, output_file)
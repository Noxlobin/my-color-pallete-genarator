import sys

hex_file = open("pallete.txt", "x")
var_dict = []


while True:
  prompt = input("Enter the color: ")
  if prompt == "done":
    break

  prompt_arr = prompt.split("=")


  if len(prompt_arr) != 2:
    print("err: Seperator should be = (name=value)")
    sys.exit(1)

  var_dict.append({"name": prompt_arr[0], "hex": prompt_arr[1]})


for var in var_dict:
  hex_file.write(var["name"] +  ": " + var["hex"])
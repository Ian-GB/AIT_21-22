with open('04_inmatrix2.txt', 'r') as f:
  data = f.readlines()
  # read raw lines into an array

cleaned_matrix = []
for raw_line in data:

  split_line = raw_line.strip().split(",")
  # ["1", "0" ... ]

  nums_ls = [int(x.replace('"', '')) for x in split_line]
  # get rid of the quotation marks and convert to int

  cleaned_matrix.append(nums_ls)

print(cleaned_matrix)
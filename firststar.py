file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
count = 0
# Strips the newline character 
for index, line in enumerate(Lines):
    first_item= int(line)
 #   print("Line{}: {}, {}".format(index, first_item, len(Lines) )    )
    for nested_index in range(index+1,len(Lines),1):
        second_item= int(Lines[nested_index])
      #  print("Line{}: {}, {}".format(nested_index, second_item, len(Lines) )    )
        for inside_index in range(nested_index+1,len(Lines),1):
            third_item= int(Lines[inside_index])
            if(first_item + second_item +third_item == 2020):
                print("found solution, {} and {} and {}".format(first_item, second_item, third_item))
                print(first_item*second_item*third_item)
      #  print("Line{}: {}, {}".format(nested_
       
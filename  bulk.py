import os
i=0
path=os.chdir('/Users/apple/Desktop/image bulk')

for file in os.listdir(path):
    if file == ".DS_Store":
      continue
         
    new_file = f"car_image_{i}.png"
    os.rename(file,new_file)
    print(f" Renamed :{file}  {new_file}")
    i=i+1
 
   




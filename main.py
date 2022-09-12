import os

cwd = os.getcwd()

print("current directory:",cwd)

lsdata = os.getcwdb()

print(lsdata)

# Function to Get the current  
# working directory 
def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
    
    
# Driver's code 
# Printing CWD before 
current_path() 
    
# Changing the CWD 
os.chdir('../') 
    
# Printing CWD after 
current_path() 
#make directory in Current path 
'''ath = os.path.join(test1) 
os.mkdir(path)'''

# Directory 
#directory = "test1"
  
# Parent Directory path 
parent_dir = "c:/users/nallag/"
  
# Path 
path = os.path.join(parent_dir, directory) 
  
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
os.mkdir(path) 
print("Directory '% s' created" % directory) 
  
# Directory 
directory = "Geeks"
  
# Parent Directory path 
parent_dir = "c:/users/nallag/"
  
# mode 
mode = 0o666
  
# Path 
path = os.path.join(parent_dir, directory) 
  
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
# with mode 0o666 
os.mkdir(path, mode) 
print("Directory '% s' created" % directory) 
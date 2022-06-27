import filecmp
from difflib import Differ


def get_diff_files(paths):
    differences = [] 
    
    for file_name in paths.diff_files:
        differences.append(file_name)
        
    return differences



def get_diff_details(list_file): 
    for file_name in list_file:
        with open(f'./data/old/{file_name}') as file_1, open(f'./data/new/{file_name}') as file_2:
            
            differ = Differ()
            
            print (f"\n\n \33[37m Le fichier \033[91m{file_name}\33[37m à muté \n\n ")

            for line in differ.compare(file_1.readlines(), file_2.readlines()):
                if (line.startswith('-')):
                    print(f"\033[92m{line}")
                elif (line.startswith('+')):
                    print(f"\033[91m{line}")
        
        
                    
list_files = get_diff_files(filecmp.dircmp('./data/old/', './data/new/'))                   
get_diff_details(list_files)
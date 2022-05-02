import os
import shutil

def file_sorter(path):
    """
    A function to sort the files in a download folder
    into their respective categories.
    """
    
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    ft_list=[] # ft (file type)
    ft_folder_dict={}
    
    # Creating folders for each kind el file
    for file in files:
        # Storing file stype extension
        ft = file.split('.')[1]

        if ft not in ft_list:
            ft_list.append(ft)
            new_folder_name = path + '/' + ft + '_folder'
            ft_folder_dict[str(ft)] = str(new_folder_name)

            if os.path.isdir(new_folder_name) == True:  # Folder exists
                continue
            
            else:
                os.mkdir(new_folder_name)
    
    # Moving files to respectively folder
    for file in files:
        src_path = path + '/' + file
        ft = file.split('.')[1]

        if ft in ft_folder_dict.keys():
            dest_path = ft_folder_dict[str(ft)]
            shutil.move(src_path, dest_path)
            
    print(src_path + ('\033[92m' + ' >>> ' + '\033[0m') + dest_path)

if __name__=="__main__":
    # Folder's path
    path = input('Paste the desired path:')
    file_sorter(path)
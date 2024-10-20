import os

to_edit = 'card_png'
folder = os.path.join(os.getcwd(), to_edit)
for file in os.listdir(folder):
    split = file.split('_')
    
    if len(split) == 3:
        newname = f'{split[0]}{split[2][0]}.png'.capitalize()
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, newname)
        
        try:
            os.rename(old_path, new_path)
            print(f'Renamed {file} to {newname}')
        except FileExistsError:
            print(f'Skipped {file}: {newname} already exists')
        except PermissionError:
            print(f'Skipped {file}: Permission denied')
        except Exception as e:
            print(f'Error renaming {file}: {str(e)}')
    else:
        print(f'Skipped {file}: Incorrect format')

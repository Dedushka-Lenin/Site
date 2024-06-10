import json
import os


def get_subdirectories(directory):
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
 
t = get_subdirectories('controll_auction/auction')

print(type(t))

for i in range(len(t)):

    with open(f'controll_auction/auction/{t[i]}/description.json') as f:
            file_content = f.read()
            templates = json.loads(file_content)
        
    t[i] = {
        "name": templates['name'],
        "price": templates['price'],
        "Description": templates['Description'],
    }


print(t)
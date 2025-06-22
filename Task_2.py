from typing import Optional

def get_cats_info(path: str) -> Optional[list[dict]]:
    """
    Create the Cat list (dictionaries) based on the input data (file)

    Args:
        path (str): The path to the input data.
    Returns:
        Optional[list[dict]]: 
       Cat list with dictionaries and atributes: "id", "name", and "age".
            - if the file is not found or has incorect structure, then None is reterned
    """
    cats_info = []
    line_number = 0
    try:
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                parts =line.strip().split(',') 
                line_number += 1
                try:
                    cats_info.append({
                        "id": parts[0],
                        "name": parts[1],
                        "age": int(parts[2])
                    })  
                # Handle invalid data in the file   
                except Exception as exp:
                    print(f"File {path} is not valid: {exp}, line {line_number}   ")
                    return  None
    except FileNotFoundError:   
        print(f"File {path} not found.")
        return None
    except Exception as exp:
        print(f"An unexpected error occurred while reading file {path}: {exp}")
        return None
    return cats_info


print(get_cats_info("Cats.txt"))   

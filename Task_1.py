from typing import Optional

def total_salary(path: str) -> tuple[Optional[int], Optional[float]]:
    """
    Calculates the total and average salary from a file.

    Args:
        path (str): The path to the file contains the salary data.
    Returns:
        tuple[Optional[int], Optional[float]] 
        Tuple contains:
            - if the function is completed successfuly, then the total salary, average salary (float) is returned; 
            - if the function is completed unsuccussfuly, then the None is returned.
        Salary data:
            -if the file with Salary is empty, then the (0, 0.0) returns
            -if the file with Salary has incorrect data, then (None, None) returns
    """
    total_salary = 0
    count = 0   
    line_number = 0
    try:
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                line_number += 1
                parts =line.strip().split(',') 
                try:
                    total_salary+=int(parts[1])
                    count+=1
                except Exception as exp:
                    print(f"File {path} is not valid: {exp}: line {line_number}")
                    return  (None, None)
    except FileNotFoundError:   
        print(f"File {path} not found.")
        return (None, None)
    except Exception as exp:
        print(f"An unexpected error occurred while reading file {path}: {exp}")
        return (None, None)
    return (total_salary, total_salary/count) if count > 0 else (0, 0.0)


total, average = total_salary("Salary.txt")    
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
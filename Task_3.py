import sys, pathlib
from colorama import Fore, Style

def print_directory_contents(path: str, level: int = 0) -> None :
    """
    Prints directory with subdirectories.
    
    Args:
        path (str): The path to the directory.
        level (int): The level of directory for indentation formatting.
    """
    try:
        if level == 0:
            # Root directory 
            print(f"{Fore.BLUE}{'   '*level}{pathlib.Path(path).name}/{Style.RESET_ALL}")
            level= 1  # Subdirectory increasing level 
        for item in sorted(pathlib.Path(path).iterdir()):
            if item.is_dir():
                print(f"{Fore.BLUE}{'   '*level}{item.name}/{Style.RESET_ALL}")
                # Subdirectory call (recursion)
                print_directory_contents(str(item), level+1) 
            else:
                print(f"{Fore.GREEN}{'   '*level}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}{'   ' * level}Permission denied to access {path}{Style.RESET_ALL}")
    except Exception as exp:
        # If unexpected errors
        print(f"An error occurred while accessing the directory {path}: {exp}") 


def main():
    """
    Function prints the directory with subdirectories.
    """
    if len(sys.argv) == 1:
        print("Path to directory must be provided")
        sys.exit(1) 

    path_dir= sys.argv[1]
    if not pathlib.Path(path_dir).exists():
        print(f"Error: The path '{path_dir}' is not found")
        sys.exit(1)
    if not pathlib.Path(path_dir).is_dir():
        print(f"The found path is not a directory: {path_dir}")
        sys.exit(1)

    print(f"Directory structure for: {Fore.YELLOW}{path_dir}{Fore.RESET}")
    print_directory_contents(path_dir)

if __name__ == "__main__":
   main()
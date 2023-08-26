import os
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def create_random_empty_files(directory, num_files_per_directory):
    for root, dirs, _ in os.walk(directory):

        for _ in range(num_files_per_directory):
            random_name = generate_random_string(10) + '.txt'
            random_file_path = os.path.join(root, random_name)

            with open(random_file_path, 'w'):
                pass

            print(f"Created empty file '{random_file_path}'")


def main():
    target_directory = input("Enter the path to the target directory: ")
    num_files_per_directory = int(input("Enter the number of files to create per directory: "))

    create_random_empty_files(target_directory, num_files_per_directory)
    print("Random empty files created successfully.")


if __name__ == "__main__":
    main()

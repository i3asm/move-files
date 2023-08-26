import os
import argparse
import shutil


def move_files(source_dir, dest_dir):
    result_dir_name = os.path.basename(dest_dir)

    for root, dirs, files in os.walk(source_dir):
        if result_dir_name in dirs:
            dirs.remove(result_dir_name)  # Exclude the result directory from traversal
        if '.git' in dirs:
            dirs.remove('.git')  # Exclude the git directory from traversal
        if '.idea' in dirs:
            dirs.remove('.idea')  # Exclude the idea directory from traversal

        for file in files:
            if file == 'generate-files.py':
                continue
            if file == 'move-file.py':
                continue
            file_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)
            shutil.move(file_path, dest_path)
            print(f"Moved '{file_path}' to '{dest_path}'")


def main():
    parser = argparse.ArgumentParser(
        description="Move files from subdirectories to a specified result directory under the source directory.")
    parser.add_argument("-f", "--source-directory", default=os.getcwd(),
                        help="Path to the source directory (default: current directory)")
    parser.add_argument("-d", "--dest-directory", default="result",
                        help="Name of the result directory (default: 'result')")
    parser.add_argument("-p", "--dest-path", help="Path to the destination directory")
    args = parser.parse_args()

    source_directory = args.source_directory

    if args.dest_path:
        result_directory = args.dest_path
    else:
        result_directory = os.path.join(source_directory, args.dest_directory)

    if not os.path.exists(result_directory):
        os.makedirs(result_directory)

    move_files(source_directory, result_directory)
    print("All files moved successfully.")


if __name__ == "__main__":
    main()

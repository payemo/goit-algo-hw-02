import argparse
import os
import shutil

def cp_files(src_dir: str, dest_dir: str) -> None:
    try:
        for item in os.listdir(src_dir):
            src_item = os.path.join(src_dir, item)

            if os.path.isdir(src_item):
                # Fall into subdirectory
                cp_files(src_item, dest_dir)
            elif os.path.isfile(src_item):
                # Get file's extension
                file_ext = os.path.splitext(src_item)[1][1:] or 'noname'
                dst_subdir = os.path.join(dest_dir, file_ext)

                # Create subdirectory for appropriate extension  if it doesn't exist.
                os.makedirs(dst_subdir, exist_ok=True)

                # Copy files to subdirectory
                shutil.copy2(src_item, dst_subdir)

                print(f"'{src_item}' was successfully copied into '{dst_subdir}' directory.")

    except Exception as e:
        print(f"Error during processing '{src_dir}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursive copy and files sorting by its extension.")
    parser.add_argument('src_dir', help="Path to the source directory.")
    parser.add_argument('dest_dir', help="Path to the destination directory.")
    args = parser.parse_args()

    src_dir = args.src_dir
    dst_dir = args.dest_dir

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    
    # Creating destination directory if it doesn't exist.
    if not os.path.exists(dst_dir):
        try:
            os.makedirs(dst_dir)
        except Exception as e:
            print(f"Unable to create directory: '{dst_dir}'")
            return
        
    cp_files(src_dir, dst_dir)

if __name__ == '__main__':
    main()
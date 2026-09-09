from pathlib import Path
import shutil
import argparse

parser=argparse.ArgumentParser(description="Organize files based on extension")
parser.add_argument("folder")
parser.add_argument("--dry-run", action="store_true")
args=parser.parse_args()
root = Path(args.folder)
print(root)
extension_map = {
    ".jpg": "Images",
    ".pdf": "Documents",
    ".exe": "Applications",
}
count={}

for subdir in root.iterdir():
    if subdir.is_file():
        ext=subdir.suffix.lower()
        dest=root / extension_map.get(ext,"Other")
        dest_file=dest/subdir.name
        if dest_file.exists():
            seq=1
            new_name=f"{dest_file.stem}+{seq:02d}{dest_file.suffix}"
            while (dest/new_name).exists():
                seq+=1
                new_name=f"{dest_file.stem}_{seq:02d}{dest_file.suffix}"
            dest_file=dest/new_name
            print(f"{subdir.name} changed to {new_name}")
        try:
            if args.dry_run:
                print(f"{subdir.name} will be moved to {dest.name}")
            else:
                dest.mkdir(parents=True,exist_ok=True)
                shutil.move(str(subdir),str(dest_file))
                count[dest]=count.get(dest,0)+1
        except Exception as e:
            print(f"Error moving {subdir.name}: {e}")

for category,num in count.items():
    print(f"Number of files copied in {category.name} is {num}.")

#TODO: Handle naming conflicts
#TODO: Create a copy of this file with argpath to get directory directly from CLI which removes user dependency and can be integrated with other programs
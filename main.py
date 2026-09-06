from pathlib import Path
import shutil

root = Path("C:/Users/dntri/Downloads")
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
        try:
            dest.mkdir(parents=True,exist_ok=True)
            shutil.copy(str(subdir),str(dest/subdir.name))
            count[dest]=count.get(dest,0)+1
        except Exception as e:
            print(f"Error moving {subdir.name}: {e}")

for category,num in count.items():
    print(f"Number of files copied in {category.name} is {num}.")


#TODO: Add logic to make the program dynamic in choosing the directory i.e. argpath
#TODO: Handle naming conflicts
from pathlib import Path

files = {}
for soubor in Path("C:/dev").rglob("*"):
    if soubor.is_file():
        files[soubor] = soubor.stat().st_size/(1024*1024)

sorted_files = sorted(files.items(), key=lambda item: item[1], reverse=True)[:10]

for key, value in sorted_files:
    print(f"{value:.2f} MB  {str(key):<5}")

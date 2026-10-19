import os
from sys import argv

dirPath: str = argv[1]

fileNodes: list[str] = []

for file in os.listdir(dirPath):
    fileNodes.append(f'<li><a href="{file}">{file}</a></li>')

if '<li><a href="index.html">index.html</a></li>' in fileNodes:
    fileNodes.remove('<li><a href="index.html">index.html</a></li>')

with open (os.path.join(dirPath, "index.html"), "w") as index:
    index.write(
        f"""<!DOCTYPE html>
<html>
    <head>
        <title>{dirPath} @ Teague W. Burkey</title>
    </head>
    <body>
        <h1>/{dirPath}</h1>
        <ul>{"".join(fileNodes)}</ul>
        </body>
</html>
""")
    
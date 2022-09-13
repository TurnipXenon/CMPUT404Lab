import requests

content = requests.get("https://raw.githubusercontent.com/TurnipXenon/CMPUT404Lab/main/lab01/get.py").content
with open("source_code.txt", "w") as f:
    print(content, file=f)
print(content)
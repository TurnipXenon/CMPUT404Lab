import requests

def get_source():
    response = requests.get("https://raw.githubusercontent.com/TurnipXenon/CMPUT404Lab/main/lab01/get.py")
    
    if response.status_code != 200 and response.status_code != 201:
        print(f"Error: status code: {response.status_code}")
        return
        
    content = response.content.decode("utf-8")
    with open("source_code.txt", "w") as f:
        print(content, file=f)
    print(content)

get_source()

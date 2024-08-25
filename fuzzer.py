import requests
import sys

def loop():
    for word in sys.stdin:
        word = word.strip()  # Remove any trailing newline or whitespace characters
        response = requests.get(url=f"https://your-target/{word}")
        
        if response.status_code == 404:
            print(f"Resource not found for: {word}")
            continue  # Skip to the next word instead of calling loop again
        elif response.status_code == 200:
            data = response.json()  # Correct assignment
            print(data)
        else:
            print(f"Unexpected status code {response.status_code} for: {word}")
        print(word)  # This might be redundant, but it's retained from the original code

loop()

import requests


def main():
    url = "http://localhost:5000/Bobbit"
    for i in range(100):
        data = {"bit": 1, "index": i}
        response = requests.post(url, json=data)
        print(response.status_code)
        print(response.json())


if __name__ == "__main__":
    main()

import requests

def main():
    response = requests.get('https://baidu.com')
    print(response.status_code)

if __name__ == '__main__':
    main()
import requests

def main():
    url = 'http://localhost:5000/upload'
    try:
        with open('path_to_your_file.csv', 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files)
            print(response.text)
    except FileNotFoundError:
        print("O arquivo especificado não foi encontrado.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer o pedido: {e}")

if __name__ == "__main__":
    main()

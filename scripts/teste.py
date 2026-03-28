import requests


def get_valid_cep(cep) -> dict | None:
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    if 'erro' not in data:
        return data
    return None


if __name__ == '__main__':
    cep = '04823-050'
    endereco = get_valid_cep(cep)
    print(endereco)

# 'logradouro': 'Rua Windsor'
# 'bairro': 'Parque Alto do Rio Bonito'
# 'localidade': 'São Paulo'

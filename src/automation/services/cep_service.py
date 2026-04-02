import requests


class CepService:
    VIA_CEP_URL = 'https://viacep.com.br/ws/{cep}/json/'

    @staticmethod
    def get_valid_cep(cep: str) -> dict:
        response = requests.get(
            CepService.VIA_CEP_URL.format(cep=cep), timeout=10
        )
        response.raise_for_status()
        data = response.json()
        if 'erro' in data:
            raise ValueError(f'Invalid or not found CEP: {cep}')
        return data

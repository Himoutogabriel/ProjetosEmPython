from ClassePessoa import Pessoa
import requests
class Cliente(Pessoa):

    def __init__(self):
        super().__init__()
        self.idade=None
        self.cep=''
        self.estado=''
        self.cidade=''
        self.bairro=''

    def calculo_idade(self):
        data=''.join(caractere for caractere in self.data_nascimento if caractere.isdigit())
        ano=data[4:8]
        ano=int(ano)
        return 2026-ano
    
    def consulta_dados(self):
        cep=''.join(caractere for caractere in self.cep if caractere.isdigit())
        cep=str(cep)
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        dados = resposta.json()   
        self.estado=dados["uf"]
        self.cidade=dados["localidade"]
        self.bairro=dados["bairro"]
        print(f"Nome={self.nome}\nCPF={self.cpf}\nData de nascimento={self.data_nascimento}\nIdade={self.idade}\nEndereço={self.estado}/{self.cidade}/{self.bairro}\n")




# language: pt
# encoding: utf-8
@registration
Funcionalidade: Cadastro de Entregador Buger Eats
  Como um candidato a entregador
  Eu quero me cadastrar na plataforma Buger Eats
  Para que eu possa fazer entregas e ganhar dinheiro

  Contexto:
    Dado que estou na pagina inicial do Buger Eats
    Quando clico em "Cadastre-se para fazer entregas"
    Então devo ser direcionado para a pagina de cadastro

  @regression @delivery_moto
  Cenário: Cadastro completo com sucesso - Moto
    Dado que estou na pagina de cadastro
    Quando preencho os dados pessoais:
    | campo        | valor     |
    | Nome completo| <random>  |
    | CPF          | <random>  |
    | E-mail       | <random>  |
    | Whatsapp     | <random>  |
    | CEP          | <random>  |
    E clico em "Buscar CEP"
    E aguardo o preenchimento automático do endereço
    E preencho o número "500"
    E preencho o complemento "Apto 101"
    E seleciono o método de entrega "Moto"
    E faço upload da foto da CNH
    E clico em "Cadastre-se para fazer entregas" no formulário
    Então devo ver a mensagem de sucesso
    E quando clicar em "OK" na mensagem de sucesso, devo ser redirecionado para a pagina inicial

  @regression @delivery_bike
  Cenário: Cadastro completo com sucesso - Bicicleta
    Dado que estou na pagina de cadastro
    Quando preencho os dados pessoais:
    | campo        | valor     |
    | Nome completo| <random>  |
    | CPF          | <random>  |
    | E-mail       | <random>  |
    | Whatsapp     | <random>  |
    | CEP          | <random>  |
    E clico em "Buscar CEP"
    E aguardo o preenchimento automático do endereço
    E preencho o número "500"
    E preencho o complemento "Apto 101"
    E seleciono o método de entrega "Bicicleta"
    E faço upload da foto da CNH
    E clico em "Cadastre-se para fazer entregas" no formulário
    Então devo ver a mensagem de sucesso
    E quando clicar em "OK" na mensagem de sucesso, devo ser redirecionado para a pagina inicial

  @regression @delivery_van
  Cenário: Cadastro completo com sucesso - Van/Carro
    Dado que estou na pagina de cadastro
    Quando preencho os dados pessoais:
    | campo        | valor     |
    | Nome completo| <random>  |
    | CPF          | <random>  |
    | E-mail       | <random>  |
    | Whatsapp     | <random>  |
    | CEP          | <random>  |
    E clico em "Buscar CEP"
    E aguardo o preenchimento automático do endereço
    E preencho o número "500"
    E preencho o complemento "Apto 101"
    E seleciono o método de entrega "Van/Carro"
    E faço upload da foto da CNH
    E clico em "Cadastre-se para fazer entregas" no formulário
    Então devo ver a mensagem de sucesso
    E quando clicar em "OK" na mensagem de sucesso, devo ser redirecionado para a pagina inicial

  @negative @validation_required
  Cenário: Tentativa de cadastro sem preencher campos obrigatórios
    Dado que estou na pagina de cadastro
    Quando clico em "Cadastre-se para fazer entregas" no formulário
    Então devo ver mensagens de erro nos campos obrigatórios
      | campo             | mensagem                                    |
      | Nome              | É necessário informar o nome                |
      | CPF               | É necessário informar o CPF                 |
      | E-mail            | É necessário informar o email               |
      | CEP               | É necessário informar o CEP                 |
      | Número            | É necessário informar o número do endereço  |
      | Método de entrega | Selecione o método de entrega               |
      | CNH               | Adicione uma foto da sua CNH                |

  @negative @validation_cpf
Esquema do Cenário: Cadastro com CPF inválido
  Dado que estou na pagina de cadastro
  Quando preencho o CPF com "<cpf_invalido>"
  E clico em "Cadastre-se para fazer entregas" no formulário
  Então devo ver a mensagem "Oops! CPF inválido"

  Exemplos:
    | cpf_invalido   |
    | 123            |
    | abc123         |
    | 123.456.789-0  |
    | 11111111111    |
    | 1234567890a    |
    | @@@@           |

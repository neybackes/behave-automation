# language: pt
# encoding: utf-8
Funcionalidade: Cadastro de Entregador Buger Eats
  Como um candidato a entregador
  Eu quero me cadastrar na plataforma Buger Eats
  Para que eu possa fazer entregas e ganhar dinheiro

  Contexto:
    Dado que estou na página inicial do Buger Eats
    Quando clico em "Cadastre-se para fazer entregas"
    Então devo ser direcionado para a página de cadastro

  @cadastro_sucesso @smoke
  Cenário: Cadastro completo com sucesso - Moto
    Dado que estou na página de cadastro
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
    E quando clicar em "OK" na mensagem de sucesso, devo ser redirecionado para a página inicial

@cadastro_sucesso @bicicleta
  Cenário: Cadastro completo com sucesso - Bicicleta
    Dado que estou na página de cadastro
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
    E quando clicar em "OK" na mensagem de sucesso, devo ser redirecionado para a página inicial

@cadastro_sucesso @van_carro
  Cenário: Cadastro completo com sucesso - Van/Carro
    Dado que estou na página de cadastro
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
    E quando clicar em "OK" na mensagem de sucesso, devo ser redirecionado para a página inicial


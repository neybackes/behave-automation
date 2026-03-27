# language: pt
# encoding: utf-8

Funcionalidade: Navegação no Site Buger Eats
  Como um usuário
  Eu quero navegar pelo site Buger Eats
  Para que eu possa acessar as diferentes seções e funcionalidades

  @navegacao @smoke
  Cenário: Acessar pagina inicial
    Quando acesso a pagina inicial
    Então devo ver a pagina inicial
    E devo ver o logo "Buger Eats"
    E devo ver o título "Seja um parceiro entregador pela Buger Eats"
    E devo ver o texto "Em vez de oportunidades tradicionais de entrega de refeições em horários pouco flexíveis, seja seu próprio chefe."
    E devo ver o botão "Cadastre-se para fazer entregas"

  @navegacao @smoke
  Cenário: Navegar da home para pagina de cadastro
    Dado que estou na pagina inicial
    Quando clico no botão "Cadastre-se para fazer entregas"
    Então devo ser redirecionado para "/deliver"
    E devo ver o formulário de cadastro

  @navegacao 
  Cenário: Navegar da pagina de cadastro para home
    Dado que estou na pagina de cadastro
    Quando clico no link "Voltar para home"
    Então devo ser redirecionado para a pagina inicial "/"
    E devo ver o título "Seja um parceiro entregador pela Buger Eats"

  @performance
  Cenário: Tempo de carregamento da pagina inicial
    Quando acesso a pagina inicial
    Então a pagina deve carregar em menos de 3 segundos
    E todos os recursos devem ser carregados corretamente

  @performance
  Cenário: Tempo de carregamento da pagina de cadastro
    Quando acesso a pagina de cadastro diretamente
    Então a pagina deve carregar em menos de 3 segundos
    E todos os recursos devem ser carregados corretamente

  
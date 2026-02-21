# language: pt
# encoding: utf-8

Funcionalidade: Navegação no Site Buger Eats
  Como um usuário
  Eu quero navegar pelo site Buger Eats
  Para que eu possa acessar as diferentes seções e funcionalidades

  @navegacao @smoke
  Cenário: Acessar página inicial
    Quando acesso a pagina inicial
    Então devo ver a página inicial
    E devo ver o logo "Buger Eats"
    E devo ver o título "Seja um parceiro entregador pela Buger Eats"
    E devo ver o texto "Em vez de oportunidades tradicionais de entrega de refeições em horários pouco flexíveis, seja seu próprio chefe."
    E devo ver o botão "Cadastre-se para fazer entregas"

  @navegacao @smoke
  Cenário: Navegar da home para página de cadastro
    Dado que estou na página inicial
    Quando clico no botão "Cadastre-se para fazer entregas"
    Então devo ser redirecionado para "/deliver"
    E devo ver o formulário de cadastro

  @navegacao 
  Cenário: Navegar da página de cadastro para home
    Dado que estou na página de cadastro "/deliver"
    Quando clico no link "Voltar para home"
    Então devo ser redirecionado para a página inicial "/"
    E devo ver o título "Seja um parceiro entregador pela Buger Eats"

  @performance
  Cenário: Tempo de carregamento da página inicial
    Quando acesso a página inicial
    Então a página deve carregar em menos de 3 segundos
    E todos os recursos devem ser carregados corretamente

  @performance
  Cenário: Tempo de carregamento da página de cadastro
    Quando acesso a página de cadastro diretamente
    Então a página deve carregar em menos de 3 segundos
    E todos os recursos devem ser carregados corretamente

  
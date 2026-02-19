# language: pt
# encoding: utf-8
Funcionalidade: Acessa página inicial da aplicação
  Descrição: Acessando página inicial para verificar se está funcionando corretamente

  Cenário: Acessar página inicial
    Dado que acesso a aplicação
    Quando a página carrega
    Então devo ver a página inicial
  
# Guia de Branching e Versionamento

## Estratégia de Branches

Este projeto segue o modelo **Git Flow** com as seguintes branches:

### 🎯 Branches Principais

#### `master` (Production)
- **Propósito**: Contém apenas código pronto para produção
- **Versão**: Release final testada e validada
- **Quem faz merge**: Apenas Pull Requests de `release/` ou hotfixes
- **Exemplo**: Código que está em produção

#### `develop` (Development)
- **Propósito**: Branch de integração para desenvolvimento
- **Versão**: Contém features e fixes prontos para próxima release
- **Quem faz merge**: Pull Requests de `feature/` e `bugfix/`
- **Exemplo**: Código em desenvolvimento antes de ir para production

### 🌿 Branches de Suporte

#### `feature/*` (Novas Funcionalidades)
- **Saída de**: `develop`
- **Retorna para**: `develop` (via Pull Request)
- **Exemplo**: `feature/login-page`, `feature/checkout-flow`
- **Ciclo de vida**: Criada, desenvolvida, testada, mergeada, deletada

```bash
git checkout develop
git pull origin develop
git checkout -b feature/nome-da-feature
# ... fazer mudanças ...
git push origin feature/nome-da-feature
# Criar Pull Request no GitHub
```

#### `bugfix/*` (Correção de Bugs)
- **Saída de**: `develop`
- **Retorna para**: `develop` (via Pull Request)
- **Exemplo**: `bugfix/login-error`, `bugfix/missing-element`

```bash
git checkout develop
git pull origin develop
git checkout -b bugfix/nome-do-bug
# ... corrigir ...
git push origin bugfix/nome-do-bug
# Criar Pull Request no GitHub
```

#### `release/*` (Preparação para Release)
- **Saída de**: `develop`
- **Retorna para**: `master` (via Pull Request) + `develop`
- **Exemplo**: `release/v1.0.0`, `release/v1.1.0`
- **Propósito**: Preparar versão para produção, bump de versão, testes finais

```bash
git checkout -b release/v1.0.0 develop
# Atualizar versão em arquivos
git commit -am "Bump version to v1.0.0"
git push origin release/v1.0.0
# Criar Pull Request para master
```

#### `hotfix/*` (Correções em Produção)
- **Saída de**: `master`
- **Retorna para**: `master` + `develop`
- **Exemplo**: `hotfix/critical-bug`, `hotfix/security-patch`
- **Propósito**: Correção urgente em produção

```bash
git checkout -b hotfix/nome-da-correcao master
# ... corrigir ...
git push origin hotfix/nome-da-correcao
# Criar Pull Request para master
```

---

## Workflow Passo a Passo

### 1. Criar Nova Feature

```bash
# Começar do develop
git checkout develop
git pull origin develop

# Criar feature branch
git checkout -b feature/nova-pagina-login

# Fazer mudanças...
git add .
git commit -m "Feat: Implementar página de login"

# Enviar para repositório remoto
git push origin feature/nova-pagina-login

# No GitHub: Criar Pull Request de feature/nova-pagina-login → develop
# Após review e testes: Mergeá-lo
# Deletar branch remota
```

### 2. Criar Release

```bash
# Começar do develop
git checkout -b release/v1.0.0 develop

# Atualizar versão
# - Editar VERSION file
# - Editar setup.py ou requirements
git commit -am "Release: Versão 1.0.0"

git push origin release/v1.0.0

# No GitHub: Criar Pull Request de release/v1.0.0 → master
# Após merge em master:
git checkout master
git pull origin master

# Fazer tag da versão
git tag -a v1.0.0 -m "Versão 1.0.0"
git push origin v1.0.0

# Fazer merge de volta em develop
git checkout develop
git pull origin develop
git merge release/v1.0.0
git push origin develop

# Deletar release branch
git push origin --delete release/v1.0.0
```

### 3. Hotfix em Produção

```bash
# Começar do master
git checkout -b hotfix/correcao-critica master

# Corrigir...
git commit -am "Fix: Corrigir bug crítico"

# Enviar
git push origin hotfix/correcao-critica

# No GitHub: Criar PR de hotfix → master
# Após merge:
git checkout master
git pull origin master
git tag -a v1.0.1 -m "Versão 1.0.1 - Hotfix"
git push origin v1.0.1

# Fazer merge de volta em develop
git checkout develop
git pull origin develop
git merge hotfix/correcao-critica
git push origin develop

# Deletar hotfix branch
git push origin --delete hotfix/correcao-critica
```

---

## Convenção de Commits

Use a seguinte convenção:

```
<tipo>: <descrição curta>

<descrição detalhada opcional>

<referências opcionais>
```

### Tipos de Commit

- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Documentação
- **style**: Formatação de código (sem mudança lógica)
- **refactor**: Refatoração de código
- **test**: Adicionar ou atualizar testes
- **chore**: Tarefas de manutenção
- **ci**: Configuração de CI/CD

### Exemplos

```bash
# Feature
git commit -m "feat: Adicionar página de checkout"

# Bug fix
git commit -m "fix: Corrigir erro de login com email inválido"

# Documentation
git commit -m "docs: Atualizar guia de setup"

# Refactor
git commit -m "refactor: Simplificar BasePage.wait_element"

# Test
git commit -m "test: Adicionar testes de login"

# Chore
git commit -m "chore: Atualizar dependencies"
```

---

## Versionamento Semântico

Use **Semantic Versioning** (SemVer): `MAJOR.MINOR.PATCH`

- **MAJOR** (1.0.0 → 2.0.0): Mudança incompatível na API
- **MINOR** (1.0.0 → 1.1.0): Nova funcionalidade compatível com versão anterior
- **PATCH** (1.0.0 → 1.0.1): Correção de bug

### Exemplos

```
v0.1.0  - Primeira versão alfa (features iniciais)
v0.2.0  - Mais features, melhorias
v1.0.0  - Versão estável para produção
v1.0.1  - Bug fix
v1.1.0  - Novas features
v2.0.0  - Mudanças que quebram compatibilidade
```

---

## Padrão de Pull Request

Ao criar um PR, use este template:

```markdown
## 📝 Descrição
Breve descrição do que foi implementado/corrigido.

## 🎯 Tipo de Mudança
- [ ] New feature
- [ ] Bug fix
- [ ] Breaking change
- [ ] Documentation update

## ✅ Checklist
- [ ] Código testado localmente
- [ ] Testes adicionados/atualizados
- [ ] Documentação atualizada
- [ ] Sem conflicts com a branch de destino
- [ ] CI/CD passa com sucesso

## 📸 Screenshots (se aplicável)
```

---

## Status das Branches

```
master (v1.0.0)         ← Production (estável)
  ↑
release/v1.1.0         ← Preparação para release
  ↑
develop                 ← Integration (em desenvolvimento)
  ↑
├─ feature/nova-funcionalidade
├─ feature/outra-feature
└─ bugfix/correcao
```

---

## Dúvidas Frequentes

**P: Em qual branch devo trabalhar?**
R: Sempre comece do `develop`. Crie `feature/` ou `bugfix/` a partir dele.

**P: Como sincronizar minha branch com develop?**
R: 
```bash
git fetch origin
git rebase origin/develop
# ou
git merge origin/develop
```

**P: Posso deletar uma branch local?**
R: Sim, após fazer merge em develop/master:
```bash
git branch -d feature/nome  # Local
git push origin --delete feature/nome  # Remota
```

**P: Como fazer merge manualmente?**
R: Sempre use Pull Request no GitHub, não faça merge local.

---

**Última atualização**: Dezembro 2025

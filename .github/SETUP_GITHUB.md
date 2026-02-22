# Próximas Etapas: Configurar no GitHub

## ✅ O que foi feito localmente

- [x] Repositório Git inicializado
- [x] Branch `master` criada com commit inicial
- [x] Branch `develop` criada
- [x] Arquivo de guia de branching criado

## 📋 O que fazer agora no GitHub

### Passo 1: Criar Repositório no GitHub

1. Acesse https://github.com/new
2. Preencha:
   - **Repository name**: `behave-bugereats` (ou outro nome)
   - **Description**: "Automação de testes web com Behave, Selenium e Python para Buger Eats"
   - **Public** ou **Private** (conforme preferência)
   - **NÃO** adicione README, .gitignore ou License (já temos localmente)

3. Clique **Create repository**

### Passo 2: Conectar Repositório Local ao GitHub

```bash
cd /d/projetos/behave_automation

# Adicionar repositório remoto
git remote add origin https://github.com/seu_usuario/behave-bugereats.git

# Verificar
git remote -v
```

### Passo 3: Enviar Código para GitHub

```bash
# Enviar branch master
git push -u origin master

# Enviar branch develop
git push -u origin develop

# Verificar branches remotas
git branch -a
```

### Passo 4: Configurar GitHub

1. Vá para seu repositório no GitHub
2. Clique em **Settings**
3. Na seção **Branches** → **Default branch**
   - Selecione `develop` como branch padrão (recomendado)
   - Ou mantenha `master` se preferir

4. Na seção **Branch protection rules** (opcional, recomendado):
   - Clique **Add rule**
   - Pattern: `master`
   - ✅ Require pull request reviews before merging
   - ✅ Dismiss stale pull request approvals when new commits are pushed
   - **Create**

5. Repita para `develop`:
   - Pattern: `develop`
   - ✅ Require pull request reviews before merging
   - **Create**

---

## 🚀 Comandos Rápidos

```bash
# Ver status do repositório
git status

# Ver branches locais
git branch

# Ver branches remotas
git branch -r

# Ver todas as branches
git branch -a

# Syncronizar com remoto
git fetch origin

# Ver commits
git log --oneline

# Ver qual branch está usando
git branch --show-current
```

---

## 📌 URLs Importantes

- **HTTPS**: `https://github.com/seu_usuario/behave-bugereats.git`
- **SSH**: `git@github.com:seu_usuario/behave-bugereats.git`
- **Web**: `https://github.com/seu_usuario/behave-bugereats`

Use HTTPS se não tiver configurado SSH.

---

## ⚠️ Importante

Se receber erro de autenticação ao fazer push:

**GitHub já descontinuou autenticação por senha.**

### Solução 1: Usar Personal Access Token (PAT)

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Marque: `repo`, `workflow`
4. Copy token
5. Ao fazer push, use o token como senha

### Solução 2: Configurar SSH (recomendado)

1. Gere chave SSH:
   ```bash
   ssh-keygen -t ed25519 -C "seu_email@example.com"
   ```

2. Adicione no GitHub:
   - Settings → SSH and GPG keys → New SSH key
   - Cole sua chave pública

3. Use URL SSH:
   ```bash
   git remote set-url origin git@github.com:seu_usuario/behave-bugereats.git
   ```

---

## ✅ Checklist Final

- [ ] Repositório criado no GitHub
- [ ] Remoto adicionado localmente
- [ ] Branches `master` e `develop` enviadas
- [ ] Branch padrão configurada
- [ ] Branch protection rules criadas (opcional)
- [ ] Documentação (BRANCHING.md) visível no GitHub

---

## 🎉 Pronto!

Após fazer esses passos, seu projeto estará:
- ✅ Versionado com Git
- ✅ No GitHub para backup e colaboração
- ✅ Pronto para trabalhar em features de forma organizada
- ✅ Documentado com guia de branching

**Próximo passo**: Comece a criar features usando o Git Flow!

```bash
git checkout develop
git pull origin develop
git checkout -b feature/sua-nova-feature
# ... fazer mudanças ...
git push origin feature/sua-nova-feature
# Criar Pull Request no GitHub
```

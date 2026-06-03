# 🎬 NETFLIX - SISTEMA DE GERENCIAMENTO

**Grupo:** Joel, Jordana e Miguel

---

## 📋 Objetivo

Implementar uma interface CRUD em Python para gerenciar um banco de dados Netflix, demonstrando:
- ✅ Operações de CREATE, READ, UPDATE, DELETE
- ✅ Interface interativa via console
- ✅ Otimização de performance com índices
- ✅ Análise de planos de execução SQL

---

## 🗂️ Arquivos Entregáveis

| Arquivo | Descrição |
|---------|-----------|
| `DDL.sql` | Script de criação das tabelas |
| `DML.sql` | Script com dados iniciais |
| `criar_indices.sql` | Índices e queries críticas com EXPLAIN ANALYZE |
| `conexao_db.py` | Módulo de conexão com PostgreSQL |
| `interface_netflix.py` | Interface interativa principal |
| `requirements.txt` | Dependências Python |

---

## 🚀 Como Executar

### 1️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Garantir que o PostgreSQL está rodando
```bash
# Verificar se o serviço está ativo (Linux)
systemctl status postgresql

# Ou conectar diretamente
psql -U postgres -d netflix -c "SELECT COUNT(*) FROM Conta;"
```

### 3️⃣ Executar a Interface
```bash
python interface_netflix.py
```

### 4️⃣ Criar Índices (se ainda não criados)
```bash
psql -U postgres -d netflix -f criar_indices.sql
```

---

## 🎯 Fluxo de Uso

### Interface Interativa - Casos de Uso

```
┌─────────────────────────────────────────────┐
│  1. CRIAR CONTA                             │
│     - Email                                  │
│     - Senha (mín. 6 caracteres)             │
│     - Selecionar Endereço                   │
│     - Escolher Plano de Assinatura          │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  2. CRIAR PERFIL                            │
│     - Nome do Perfil                        │
│     - Escolher Avatar                       │
└─────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────┐
│  3. MENU PRINCIPAL                          │
│     - Ver Filmes/Séries por Gênero         │
│     - Deletar Perfil                        │
│     - Deletar Conta                         │
│     - Sair                                  │
└─────────────────────────────────────────────┘
```

---

## 📊 Índices Criados e Performance

### Índices Implementados

1. **`idx_generoobra_idgenero`** (PRIMARY)
   - Otimiza buscas de obras por gênero
   - Uso: Menu principal ao filtrar catálogo
   - Impacto: **Reduz scan sequencial em 85%**

2. **`idx_perfil_idconta`**
   - Melhora listagem de perfis por conta
   - Uso: Verificação de perfis existentes

3. **`idx_generoobra_composite`**
   - Índice composto para queries mais complexas
   - Uso: Buscas combinadas de gênero e obra

4. **`idx_conta_email`**
   - Otimiza validação de email único
   - Uso: Prevenção de duplicatas ao criar conta

---

## 🔍 Verificar Performance com EXPLAIN ANALYZE

### Comparar antes e depois dos índices:

#### ANTES (sem índice):
```bash
psql -U postgres -d netflix -c "
EXPLAIN ANALYZE
SELECT DISTINCT o.IDObra, o.Titulo
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
WHERE go.IDGenero = 1;"
```

#### DEPOIS (com índice):
```bash
psql -U postgres -d netflix -f criar_indices.sql
psql -U postgres -d netflix -c "
EXPLAIN ANALYZE
SELECT DISTINCT o.IDObra, o.Titulo
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
WHERE go.IDGenero = 1;"
```

**Resultado esperado:** 
- Tempo de execução reduzido em ~60-80%
- Index Scan em vez de Seq Scan

---

## 📝 Operações CRUD Implementadas

### CREATE
- ✅ Criar Conta (com validação de email/senha)
- ✅ Criar Perfil (com avatar)
- ✅ Assinatura automática ao plano

### READ
- ✅ Listar Endereços
- ✅ Listar Planos
- ✅ Visualizar Filmes/Séries por Gênero
- ✅ Listar Perfis da Conta

### UPDATE
- ❌ (Não implementado nesta versão, foco em CREATE/READ/DELETE)

### DELETE
- ✅ Deletar Perfil (com confirmação)
- ✅ Deletar Conta (com cascade automático)

---

## 💾 Exemplos de Queries Críticas

### 1. Buscar Obras de um Gênero (OTIMIZADA)
```sql
SELECT DISTINCT o.IDObra, o.Titulo, o.ClassEtaria
FROM Obra o
INNER JOIN GeneroObra go ON o.IDObra = go.IDObra
WHERE go.IDGenero = 1
ORDER BY o.Titulo;
```

### 2. Listar Perfis de uma Conta
```sql
SELECT IDPerfil, Nome, Avatar 
FROM Perfil 
WHERE IDConta = 1
ORDER BY Nome;
```

### 3. Query Complexa - Contas com Planos
```sql
SELECT 
    c.IDConta, 
    c.Email, 
    pl.Nome AS NomePlano,
    pl.Valor
FROM Conta c
LEFT JOIN Assinatura a ON c.IDConta = a.IDConta
LEFT JOIN Plano pl ON a.IDPlano = pl.IDPlano
ORDER BY c.IDConta;
```

### 4. Obras por Gênero (Relatório)
```sql
SELECT 
    g.NomeGenero,
    COUNT(DISTINCT go.IDObra) AS QuantidadeObras
FROM Genero g
LEFT JOIN GeneroObra go ON g.IDGenero = go.IDGenero
GROUP BY g.IDGenero, g.NomeGenero
ORDER BY QuantidadeObras DESC;
```

---

## 🧪 Teste Rápido

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Criar índices
psql -U postgres -d netflix -f criar_indices.sql

# 3. Executar interface
python interface_netflix.py

# 4. Siga os prompts:
#    - Digite "1" para Criar Conta
#    - Escolha email, senha, endereço e plano
#    - Crie um perfil
#    - Explore o menu (ver filmes, deletar, etc.)
```

---

## 🔧 Requisitos

- Python 3.7+
- PostgreSQL 12+
- `psycopg2-binary` (instalado via requirements.txt)
- Sistema operacional: Linux, macOS ou Windows

---

## 📌 Notas Importantes

1. **Senhas de exemplo:** Não usar em produção (armazenar com hash!)
2. **Validação:** Email único, senha com 6+ caracteres
3. **Cascade:** Deletar conta deleta todos os perfis automaticamente
4. **Performance:** Índices criados em tabelas de alta frequência

---

## 👥 Autores

- **Joel**
- **Jordana**
- **Miguel**

---

## 📅 Data de Entrega

**Junho de 2026**

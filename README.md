# Automation Challenges – Test Scenarios Overview

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)

Projeto de automação desenvolvido com foco em **Python** e **Playwright**, cobrindo cenários práticos de:

- Validação de Login
- Tratamento de exceções em automação web
- Filtros, ordenação e estados dinâmicos de interface

---

## Stack Utilizada

- Python
- Playwright
- Automação de testes E2E
- Assertions e sincronização explícita

---

## 1️⃣ Login Scenarios

### Positive Login
Valida:
- Redirecionamento correto de URL
- Exibição de mensagem de sucesso
- Presença do botão de logout

### Negative Username
Valida:
- Exibição de mensagem de erro
- Texto correto para usuário inválido

### Negative Password
Valida:
- Exibição de mensagem de erro
- Texto correto para senha inválida

---

## 2️⃣ Exception Handling Scenarios

Simulação de falhas comuns em aplicações web dinâmicas:

- Elemento não encontrado (problema de sincronização)
- Elemento não interagível (invisível ou bloqueado)
- Estado inválido de elemento desabilitado
- Referência obsoleta após atualização do DOM
- Timeout por espera insuficiente

---

## 3️⃣ Filters and Sorting Scenarios

### Filtros Individuais
- Linguagem
- Nível
- Número mínimo de matrículas (comparação numérica correta)

### Filtros Combinados
Validação da interseção correta entre múltiplos critérios.

### Estado Sem Resultados
Exibição adequada quando não há correspondências.

### Reset de Filtros
- Visibilidade condicional do botão Reset
- Restauração dos valores padrão
- Reexibição completa dos dados

### Ordenação
- Ordenação numérica (Enrollments)
- Ordenação alfabética (Course Name)
- Reaplicação dinâmica após alteração de filtros

---

## Objetivo

Consolidar fundamentos de automação com foco em:

- Sincronização robusta
- Manipulação de DOM dinâmico
- Validação consistente de regras de negócio
- Escrita de testes confiáveis e escaláveis

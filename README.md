# 📦 Dashboard de Otimização Operacional – Inbound DHL

## 🎯 Objetivo

Este projeto tem como objetivo demonstrar, de forma visual e analítica, os ganhos operacionais obtidos a partir da otimização do processo Inbound logístico, com foco em produtividade, capacidade e eficiência de recursos.

O dashboard foi desenvolvido como complemento ao estudo de caso, permitindo uma visão clara do cenário **AS-IS (atual)** versus **TO-BE (proposto)**.

---

## 📊 Principais Indicadores (KPIs)

* **Produtividade Individual (peças/hora)**

  * AS-IS: 944
  * TO-BE: 1.132
  * 🔼 +20%

* **Capacidade Mensal**

  * AS-IS: 5,48 milhões de peças
  * TO-BE: 6,57 milhões de peças
  * 🔼 +1,09 milhão

* **Headcount Operacional**

  * AS-IS: 30 colaboradores
  * TO-BE: 25 colaboradores
  * 🔽 Redução de 16%

---

## ⚙️ Tecnologias Utilizadas

* **Python**
* **Streamlit** (visualização interativa)
* **Pandas** (tratamento de dados)

---

## 🧠 Racional da Melhoria

Os ganhos apresentados são resultado das seguintes iniciativas:

* Implementação de **Célula Integrada de Conferência e Packaging**
* Eliminação de atividades sem valor agregado (ex: puxada manual)
* Introdução de **automação de escoamento (esteiras)**
* Aplicação de conceitos **Lean (eliminação de desperdícios - muda)**
* Redução de movimentação desnecessária e filas operacionais

---

## 🚀 Como Executar o Projeto

1. Instale as dependências:

```
pip install streamlit pandas
```

2. Execute o dashboard:

```
streamlit run dashboard_inbound_dhl.py
```

3. Acesse no navegador:

```
http://localhost:8501
```

---

## 📁 Estrutura do Projeto

* `dashboard_inbound_dhl.py` → Código principal do dashboard
* `README.md` → Documentação do projeto

---

## 💡 Insight Estratégico

A combinação entre **redução de headcount (-16%)** e **aumento de produtividade (+20%)** evidencia um ganho direto de eficiência operacional, sustentado por redesenho de processo e automação.

---

## 👩‍💻 Autora

**Daiane Nicacio**
Analista de Processos e Projetos de TI

Projeto desenvolvido como parte de estudo de caso para otimização de processos logísticos com base em BPMN, Lean e análise de dados.

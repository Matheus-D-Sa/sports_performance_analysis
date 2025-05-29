# ⚽ Projeto Esportivo: Análise de Performance de Atletas e Clubes

## 🧩 1. Problema e Justificativa

A performance esportiva é influenciada por diversos fatores, como preparação física, incidência de lesões, tempo de jogo, e histórico de conquistas. Com a popularização de dados esportivos e a facilidade de acesso a bases públicas, torna-se possível analisar e entender padrões que impactam o rendimento de atletas e clubes em diversas modalidades.

Este projeto tem como objetivo explorar dados relacionados ao desempenho de atletas olímpicos, histórico de clubes de futebol e relação entre fadiga e lesões. A análise permitirá compreender os fatores mais relevantes para o sucesso esportivo, o impacto das lesões sobre a performance e as características dos atletas medalhistas.

A abordagem baseada em dados pode ser aplicada por clubes, federações, técnicos e preparadores físicos na tomada de decisão e elaboração de estratégias mais eficientes.

---

## 🔍 2. Coleta e Fontes de Dados Selecionadas

Foram utilizados três conjuntos de dados principais, todos disponíveis publicamente via Kaggle:

### 1. [Football Data from Transfermarkt](https://www.kaggle.com/datasets/davidcariboo/player-scores?utm_source=chatgpt.com)
- **Descrição**: Informações detalhadas sobre competições, jogos, clubes, jogadores e suas aparições.
- **Formato**: Múltiplos arquivos CSV.

### 2. [Athlete Injury and Performance Dataset](https://www.kaggle.com/datasets/ziya07/athlete-injury-and-performance-dataset?utm_source=chatgpt.com)
- **Descrição**: Dados sobre atletas, regimes de treino, fadiga e riscos de lesão.
- **Formato**: CSV.

### 3. [Olympic Athlete Performance Dataset](https://www.kaggle.com/datasets/jaberimohamedhabib/olympic-athlete-performance-dataset?utm_source=chatgpt.com)
- **Descrição**: Informações detalhadas sobre atletas olímpicos e seus desempenhos ao longo dos anos.
- **Formato**: CSV.

**Arquivos utilizados no projeto**:
- `athlete_injury.csv`
- `olympic_athletes.csv`
- `transfermarkt.csv`

---

## 💠 3. Análise Exploratória

As análises foram feitas utilizando Python, organizadas nos scripts da pasta `src/`. As etapas incluíram:

- Leitura e limpeza dos dados brutos;
- Padronização de colunas, filtros e tratamento de nulos;
- Análises estatísticas e visuais exploratórias;
- Preparação de arquivos para visualização no Looker Studio.

### Bibliotecas utilizadas:
- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `pyspark.sql` (`SparkSession`, `col`, `to_date`, `when`, `count`, `mean`, `month`)
- `plotly`

---

## 📊 4. Indicadores e Visualizações

As visualizações produzidas e incorporadas ao dashboard incluem:

- 📌 Comparação de índice de massa corporal (BMI) entre atletas lesionados e não lesionados;
- 📌 Correlação entre variáveis de treino, fadiga e risco de lesão;
- 🥇 Distribuição de medalhas por país nos Jogos Olímpicos;
- ⏱️ Média de minutos jogados por mês por atletas de futebol;
- 🌍 Proporção de medalhistas por país.

Todas as visualizações estão disponíveis no dashboard interativo criado no Looker Studio.

---

## 💡 5. Insights e Conclusões

- **Fadiga e tempo de treino** são fortemente correlacionados com o aumento do risco de lesão.
- Clubes com maior média de tempo de jogo por atleta tendem a ter menor rotatividade e desempenho mais estável.
- Países com histórico esportivo forte (como EUA, China e Rússia) concentram a maior parte das medalhas olímpicas.
- Há indícios de que variáveis como altura, peso e idade estão associadas ao perfil dos atletas medalhistas em determinadas modalidades.

### Propostas de aplicação:
- Monitorar os níveis de treino e fadiga dos atletas em tempo real;
- Reduzir carga em momentos críticos de risco elevado de lesão;
- Identificar padrões de sucesso de medalhistas e replicar modelos de treinamento.

---

## 📂 6. Estrutura do Repositório

```
📁 sports_performance_analysis/
├── 📁 data/
│ ├── athlete_injury.csv
│ ├── athlete_injury_clean.csv
│ ├── olympic_athletes.csv
│ ├── olympic_athletes_clean.csv
│ ├── transfermarkt.csv
│ ├── transfermarkt_clean.csv
│ └── transfermarkt_clean_amostra.csv
├── 📁 figures/
│ ├── comparacao_bmi_lesionados.png
│ ├── correlacao_injury.png
│ ├── distribuicao_medalhas.png
│ ├── media_minutos_por_mes.png
│ └── proporcao_medalhistas_pais.png
├── 📁 src/
│ ├── eda_analise_exploratoria.py
│ ├── eda_analise_exploratoria_pyspark.py
│ ├── exploracao_inicial.py
│ └── reduzir_csv_looker.py
├── 📄 coleta_modelagem_conclusoes.md
├── 🔗 dashboard_looker_studio.pdf
├── 📄 README.md
├── 📄 relatorio_insights.md
└── 📄 requirements.txt
```

### 📝 Sobre os arquivos:

- `athlete_injury_clean.csv`, `olympic_athletes_clean.csv`, `transfermarkt_clean.csv`:  
  Arquivos tratados e limpos a partir das versões brutas, gerados via o script `exploracao_inicial.py`. Contêm dados prontos para análise.

- `transfermarkt_clean_amostra.csv`:  
  Arquivo amostral derivado de `transfermarkt_clean.csv`, gerado com o script `reduzir_csv_looker.py`. Usado para visualização mais leve no Looker Studio.

- Pasta `figures/`:  
  Contém visualizações geradas pelo script `eda_analise_exploratoria.py`, utilizadas no relatório de insights e dashboard.

- Scripts da pasta `src/`:  
  - `exploracao_inicial.py`: tratamento e limpeza dos dados brutos.  
  - `eda_analise_exploratoria.py`: análise estatística e geração de gráficos.  
  - `eda_analise_exploratoria_pyspark.py`: versão com PySpark para análise escalável.  
  - `reduzir_csv_looker.py`: script para gerar uma amostra menor dos dados para Looker.

- Arquivos auxiliares do projeto: 
  - `coleta_modelagem_conclusoes.md`: documento que detalha o processo de coleta de dados, etapas de modelagem e as conclusões extraídas das análises.
  - `dashboard_looker_studio.pdf`: versão em PDF do dashboard publicado no Looker Studio, contendo capturas de tela das páginas e explicações visuais dos insights.
  - `README.md`: arquivo principal de documentação do repositório, descreve o objetivo do projeto, a estrutura de pastas, instruções de uso e links importantes.
  - `relatorio_insights.md`: relatório com os principais achados das análises exploratórias, baseados nos dados limpos e visualizações geradas.
  - `requirements.txt`: lista de bibliotecas Python necessárias para execução dos scripts. Pode ser utilizada para instalação via `pip install -r requirements.txt`.

---

## 🔗 7. Acesso ao Dashboard

Acesse o dashboard interativo com os principais gráficos e filtros clicando no link abaixo:

👉 [Dashboard no Looker Studio](https://lookerstudio.google.com/reporting/1e220428-2b3b-4eb4-b6d1-13dc17659fa8)

# 📥 Coleta de Dados, Modelagem e Conclusões

## 📥 Coleta de Dados

Este projeto utilizou três conjuntos de dados relevantes para a análise de performance de atletas e clubes em diferentes contextos esportivos. Todos foram obtidos na plataforma Kaggle:

1. **Football Data from Transfermarkt**  
   - Descrição: Informações detalhadas sobre competições, jogos, clubes, jogadores e suas aparições.  
   - Link: [Transfermarkt Dataset](https://www.kaggle.com/datasets/davidcariboo/player-scores?utm_source=chatgpt.com)  
   - Arquivo: `transfermarkt.csv`

2. **Athlete Injury and Performance Dataset**  
   - Descrição: Dados sobre lesões, fadiga, treinos e performance de atletas.  
   - Link: [Injury & Performance Dataset](https://www.kaggle.com/datasets/ziya07/athlete-injury-and-performance-dataset?utm_source=chatgpt.com)  
   - Arquivo: `athlete_injury.csv`

3. **Olympic Athlete Performance Dataset**  
   - Descrição: Informações históricas sobre atletas olímpicos, como nacionalidade, eventos e medalhas.  
   - Link: [Olympic Dataset](https://www.kaggle.com/datasets/jaberimohamedhabib/olympic-athlete-performance-dataset?utm_source=chatgpt.com)  
   - Arquivo: `olympic_athletes.csv`

Os dados foram carregados localmente e analisados utilizando bibliotecas como `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly` e `pyspark.sql`.

## 🧰 Modelagem e Preparação

### Padronização e Limpeza

A limpeza inicial foi realizada com o script `exploracao_inicial.py`, aplicando os seguintes passos:

- Renomeação das colunas para o padrão `snake_case`.
- Conversão de formatos de datas, padronização de categorias e remoção de inconsistências.
- Verificação e tratamento de valores ausentes ou duplicados.
- Conversão de variáveis categóricas e numéricas para facilitar a análise posterior.

Os arquivos resultantes da limpeza foram:

- `athlete_injury_clean.csv`
- `olympic_athletes_clean.csv`
- `transfermarkt_clean.csv`

Além disso, o arquivo `transfermarkt_clean_amostra.csv` foi criado pelo script `reduzir_csv_looker.py`, contendo uma amostra reduzida dos dados, otimizada para uso no Looker Studio.

### Estrutura dos Dados

- Dados de atletas olímpicos incluem país, ano, cidade, evento, medalha, idade, altura e peso.
- Dados de lesões atléticas incluem variáveis como gênero, idade, IMC, posição, carga de treino, fadiga e risco de lesão.
- Dados de jogadores de futebol abrangem clube, nome, idade, minutos jogados, competição e data da partida.

As análises visuais foram geradas com o script `eda_analise_exploratoria.py` e salvas na pasta `figures/`.

## 💡 Conclusões

- Atletas com alto índice de fadiga ou excesso de treino demonstram maior propensão a lesões.
- O IMC médio entre atletas lesionados apresenta variação em relação ao total, sugerindo correlação indireta com risco de lesão.
- A distribuição de medalhas entre países mostra forte domínio de nações como EUA, Rússia e China, enquanto muitos países participam com poucos ou nenhum medalhista.
- A idade média de atletas medalhistas varia de acordo com o esporte, evidenciando padrões de pico de performance distintos por modalidade.
- No futebol, os minutos jogados por mês apresentam picos sazonais compatíveis com os calendários de ligas europeias.
- A média de idade dos jogadores profissionais gira em torno de 25 anos, com posições ofensivas concentrando atletas mais jovens.

Essas conclusões oferecem subsídios para treinadores, comitês esportivos e clubes no desenvolvimento de estratégias de prevenção de lesões, otimização de performance e planejamento de competições. A análise integrada dos dados possibilita uma visão abrangente e baseada em evidências do universo esportivo.

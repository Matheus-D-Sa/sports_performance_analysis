import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados limpos
df_transfer = pd.read_csv('../data/transfermarkt_clean.csv')
df_injury = pd.read_csv('../data/athlete_injury_clean.csv')
df_olympic = pd.read_csv('../data/olympic_athletes_clean.csv')

# Converter colunas de data
df_transfer['date'] = pd.to_datetime(df_transfer['date'], errors='coerce')

# --- Análise 1: Comparação de BMI entre Lesionados e Não Lesionados (Athlete Injury) ---
plt.figure(figsize=(10,6))
sns.boxplot(data=df_injury, x='injury_indicator', y='bmi', palette='pastel')
plt.title('Comparação de BMI entre Lesionados (1) e Não Lesionados (0)')
plt.xlabel('Lesionado (1) vs Não (0)')
plt.ylabel('Índice de Massa Corporal (BMI)')
plt.savefig('../figures/comparacao_bmi_lesionados.png')
plt.close()

# --- Análise 2: Correlação entre métricas físicas e performance (Athlete Injury) ---
plt.figure(figsize=(10,8))
sns.heatmap(df_injury.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Variáveis Numéricas (Athlete Injury)')
plt.savefig('../figures/correlacao_injury.png')
plt.close()

# --- Análise 3: Proporção de Medalhistas por País (Top 10) ---
df_olympic['is_medalist'] = ~df_olympic['medal'].isna()
top_countries = df_olympic['noc'].value_counts().head(10).index

medal_stats = df_olympic[df_olympic['noc'].isin(top_countries)].groupby('noc').agg(
    medal_proportion=('is_medalist', 'mean'),
    medal_count=('is_medalist', 'sum')
)

# Reordenar por quantidade de medalhistas
medal_stats = medal_stats.sort_values(by='medal_count', ascending=False)

plt.figure(figsize=(10,6))
barplot = sns.barplot(
    x='medal_proportion',
    y=medal_stats.index,
    data=medal_stats.reset_index(),
    palette='magma'
)
plt.title('Proporção de Medalhistas por País (Top 10)')
plt.xlabel('Proporção de Medalhistas')
plt.ylabel('País (NOC)')
plt.xlim(0, 1)

for i, (prop, count) in enumerate(zip(medal_stats['medal_proportion'], medal_stats['medal_count'])):
    plt.text(prop + 0.02, i, f'{int(count)} medalhistas', va='center')

plt.tight_layout()
plt.savefig('../figures/proporcao_medalhistas_pais.png')
plt.close()

# --- Análise 4: Média de minutos jogados por mês (Transfermarkt) ---
df_transfer['month'] = df_transfer['date'].dt.to_period('M')
grouped_minutes = df_transfer.groupby('month')['minutes_played'].mean()
plt.figure(figsize=(12,6))
grouped_minutes.plot(marker='o')
plt.title('Média de Minutos Jogados por Mês')
plt.xlabel('Mês')
plt.ylabel('Minutos Médios')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../figures/media_minutos_por_mes.png')
plt.close()

# --- Análise 5: Frequência de medalhas por tipo (Olympic Athletes) ---
plt.figure(figsize=(8,6))
sns.countplot(data=df_olympic, x='medal', order=df_olympic['medal'].value_counts().index, palette='muted')
plt.title('Distribuição de Medalhas')
plt.xlabel('Tipo de Medalha')
plt.ylabel('Quantidade')
plt.savefig('../figures/distribuicao_medalhas.png')
plt.close()

print("\nGráficos atualizados e salvos na pasta ../figures")

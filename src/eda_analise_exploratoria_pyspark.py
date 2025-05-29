from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, isnan, when, count, mean, year, month
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Criar sessão Spark
spark = SparkSession.builder.appName("EDA_Performance_Esportiva").getOrCreate()

# Carregar dados
df_transfer = spark.read.csv('../data/transfermarkt_clean.csv', header=True, inferSchema=True)
df_injury = spark.read.csv('../data/athlete_injury_clean.csv', header=True, inferSchema=True)
df_olympic = spark.read.csv('../data/olympic_athletes_clean.csv', header=True, inferSchema=True)

# --- Conversão de datas
df_transfer = df_transfer.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

# --- Análise 1: Comparação de BMI entre Lesionados e Não Lesionados
df_injury_pd = df_injury.select("injury_indicator", "bmi").dropna().toPandas()

plt.figure(figsize=(10,6))
sns.boxplot(data=df_injury_pd, x='injury_indicator', y='bmi', palette='pastel')
plt.title('Comparação de BMI entre Lesionados (1) e Não Lesionados (0)')
plt.xlabel('Lesionado (1) vs Não (0)')
plt.ylabel('Índice de Massa Corporal (BMI)')
plt.savefig('../figures/comparacao_bmi_lesionados.png')
plt.close()

# --- Análise 2: Correlação entre métricas físicas e performance
df_corr_pd = df_injury.select(
    [col for col in df_injury.columns if str(df_injury.schema[col].dataType) in ['DoubleType', 'IntegerType']]
).dropna().toPandas()

plt.figure(figsize=(10,8))
sns.heatmap(df_corr_pd.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre Variáveis Numéricas (Athlete Injury)')
plt.savefig('../figures/correlacao_injury.png')
plt.close()

# --- Análise 3: Proporção de Medalhistas por País (Top 10)
df_olympic = df_olympic.withColumn("is_medalist", col("medal").isNotNull())
top_noc = df_olympic.groupBy("noc").count().orderBy(col("count").desc()).limit(10).select("noc").rdd.flatMap(lambda x: x).collect()

df_top_noc = df_olympic.filter(col("noc").isin(top_noc))

medal_stats = df_top_noc.groupBy("noc").agg(
    mean("is_medalist").alias("medal_proportion"),
    count(when(col("is_medalist") == True, True)).alias("medal_count")
).orderBy(col("medal_count").desc())

medal_stats_pd = medal_stats.toPandas()

plt.figure(figsize=(10,6))
sns.barplot(
    x='medal_proportion',
    y='noc',
    data=medal_stats_pd,
    palette='magma'
)
plt.title('Proporção de Medalhistas por País (Top 10)')
plt.xlabel('Proporção de Medalhistas')
plt.ylabel('País (NOC)')
plt.xlim(0, 1)

for i, (prop, count) in enumerate(zip(medal_stats_pd['medal_proportion'], medal_stats_pd['medal_count'])):
    plt.text(prop + 0.02, i, f'{int(count)} medalhistas', va='center')

plt.tight_layout()
plt.savefig('../figures/proporcao_medalhistas_pais.png')
plt.close()

# --- Análise 4: Média de minutos jogados por mês
df_transfer = df_transfer.withColumn("month", col("date").cast("date"))
df_monthly = df_transfer.groupBy(year("date").alias("year"), month("date").alias("month")) \
    .agg(mean("minutes_played").alias("avg_minutes")) \
    .orderBy("year", "month")

df_monthly_pd = df_monthly.withColumn("month_str",
    col("year").cast("string") + "-" + col("month").cast("string")
).toPandas()

plt.figure(figsize=(12,6))
plt.plot(df_monthly_pd["month_str"], df_monthly_pd["avg_minutes"], marker='o')
plt.title('Média de Minutos Jogados por Mês')
plt.xlabel('Mês')
plt.ylabel('Minutos Médios')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../figures/media_minutos_por_mes.png')
plt.close()

# --- Análise 5: Frequência de medalhas por tipo
df_medal = df_olympic.filter(col("medal").isNotNull()) \
    .groupBy("medal").count() \
    .orderBy(col("count").desc())

df_medal_pd = df_medal.toPandas()

plt.figure(figsize=(8,6))
sns.barplot(data=df_medal_pd, x='medal', y='count', palette='muted')
plt.title('Distribuição de Medalhas')
plt.xlabel('Tipo de Medalha')
plt.ylabel('Quantidade')
plt.savefig('../figures/distribuicao_medalhas.png')
plt.close()

print("\nGráficos atualizados e salvos na pasta ../figures")

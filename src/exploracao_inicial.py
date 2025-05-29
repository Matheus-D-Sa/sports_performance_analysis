import pandas as pd

# Caminhos dos arquivos
path_transfermarkt = '../data/transfermarkt.csv'
path_athlete_injury = '../data/athlete_injury.csv'
input_path = '../data/olympic_athletes.csv'
output_path = '../data/olympic_athletes_clean.csv'

# Corrigir problemas de aspas no arquivo olímpico
with open(input_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', newline='', encoding='utf-8') as outfile:
    for line in infile:
        clean_line = line.replace('""', '"').strip()
        if clean_line.startswith('"') and clean_line.endswith('"'):
            clean_line = clean_line[1:-1]
        outfile.write(clean_line + '\n')

# Carregar datasets
df_transfer = pd.read_csv(path_transfermarkt)
df_injury = pd.read_csv(path_athlete_injury)
df_olympic = pd.read_csv(output_path)

# Padronizar nomes de colunas
for df in [df_transfer, df_injury, df_olympic]:
    df.columns = df.columns.str.strip().str.lower()

# === TRANSFERMARKT ===
df_transfer['date'] = pd.to_datetime(df_transfer['date'], errors='coerce')

# Tipos numéricos
numeric_cols_transfer = ['yellow_cards', 'red_cards', 'goals', 'assists', 'minutes_played']
df_transfer[numeric_cols_transfer] = df_transfer[numeric_cols_transfer].apply(pd.to_numeric, errors='coerce')

# Preencher valores ausentes com 0 nas colunas de performance
df_transfer[numeric_cols_transfer] = df_transfer[numeric_cols_transfer].fillna(0)

# Criar colunas derivadas
df_transfer['goal_contribution'] = df_transfer['goals'] + df_transfer['assists']
df_transfer['discipline_score'] = df_transfer['yellow_cards'] + 2 * df_transfer['red_cards']

# === ATHLETE INJURY ===
numeric_cols_injury = df_injury.columns.drop(['athlete_id', 'gender', 'position', 'training_intensity', 'injury_indicator'])
df_injury[numeric_cols_injury] = df_injury[numeric_cols_injury].apply(pd.to_numeric, errors='coerce')

# Tratar nulos com média ou mediana
df_injury[numeric_cols_injury] = df_injury[numeric_cols_injury].fillna(df_injury[numeric_cols_injury].median())

# Padronizar categorias
df_injury['gender'] = df_injury['gender'].fillna('Unknown').astype(str).str.upper().str.strip()
df_injury['position'] = df_injury['position'].fillna('Unknown').astype(str).str.title().str.strip()
df_injury['training_intensity'] = df_injury['training_intensity'].fillna('Unknown').astype(str).str.title().str.strip()

# Criar colunas derivadas
df_injury['bmi'] = df_injury['weight_kg'] / ((df_injury['height_cm'] / 100) ** 2)
df_injury['weekly_load'] = df_injury['training_hours_per_week'] * df_injury['training_intensity'].map({'Low': 1, 'Medium': 2, 'High': 3})

# === OLYMPIC ATHLETES ===
df_olympic['medal'] = df_olympic['medal'].fillna('None')  # Medalhas ausentes = Nenhuma
df_olympic['edition'] = df_olympic['edition'].astype(str)
df_olympic['gender'] = df_olympic['gender'].str.upper().str.strip()
df_olympic['event_gender'] = df_olympic['event_gender'].str.upper().str.strip()

# Criar colunas derivadas
df_olympic['is_medalist'] = df_olympic['medal'].apply(lambda x: 0 if x == 'None' else 1)
df_olympic['year'] = df_olympic['edition'].str.extract(r'(\d{4})').astype(int)

# Regravar arquivos limpos
df_transfer.to_csv('../data/transfermarkt_clean.csv', index=False)
df_injury.to_csv('../data/athlete_injury_clean.csv', index=False)
df_olympic.to_csv('../data/olympic_athletes_clean.csv', index=False)

# Confirmação
print("\nTodos os datasets foram tratados e estão prontos para análise e visualização.")

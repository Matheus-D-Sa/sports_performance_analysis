import pandas as pd
import os

# Caminho relativo para o CSV original
csv_path = "../data/transfermarkt_clean.csv"

# Caminho relativo para salvar o novo CSV amostrado
output_path = "../data/transfermarkt_clean_amostra.csv"

# Carregar o DataFrame
df = pd.read_csv(csv_path)

# Amostragem aleatória: 100.000 linhas
df_amostra = df.sample(n=100_000, random_state=42)

# Salvar na mesma pasta dos dados
df_amostra.to_csv(output_path, index=False)

# Informações
print("Arquivo original:", len(df), "linhas")
print("Arquivo amostrado:", len(df_amostra), "linhas")
print(f"Salvo como: {output_path}")


# # Caminho do arquivo para excluir
# arquivo_para_excluir = "../data/transfermarkt_amostra.csv"
#
# # Verifica se o arquivo existe antes de tentar excluir
# if os.path.exists(arquivo_para_excluir):
#     os.remove(arquivo_para_excluir)
#     print(f"Arquivo removido: {arquivo_para_excluir}")
# else:
#     print("Arquivo não encontrado.")
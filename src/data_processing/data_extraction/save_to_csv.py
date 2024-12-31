import os


def save_to_csv(df, filename, output_dir):
    if df is not None:
        # Criando diretório se não existir
        output_dir = 'data/database'
        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

        output_dir = os.path.join(project_dir, output_dir)
        os.makedirs(output_dir, exist_ok=True)

        file_path = os.path.join(output_dir, filename)

        # Salvando os dados no CSV
        df.to_csv(file_path, index=False)
        print(f"Dados salvos em: {file_path}")
    else:
        print("Nenhum dado para salvar.")

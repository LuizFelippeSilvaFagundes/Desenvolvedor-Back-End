import xml.etree.ElementTree as ET
import json

def corrigir_xml(caminho_arquivo):
    """
    Corrige um XML que pode estar mal formatado, adicionando um único elemento raiz.
    Retorna o caminho do arquivo corrigido.
    """
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()

    # Envolvendo o conteúdo em uma única tag raiz
    conteudo_corrigido = "<faturamento>\n" + "".join(linhas) + "\n</faturamento>"

    # Salvando o XML corrigido em um novo arquivo temporário
    caminho_corrigido = "corrigido.xml"
    with open(caminho_corrigido, 'w') as file:
        file.write(conteudo_corrigido)

    return caminho_corrigido

def processar_xml(caminho_arquivo):
    """
    Processa o arquivo XML e extrai os valores de faturamento,
    ignorando valores zerados.
    """
    tree = ET.parse(caminho_arquivo)
    root = tree.getroot()

    # Extrair valores de faturamento, ignorando valores zero
    valores = [float(row.find('valor').text) for row in root.findall('row') if float(row.find('valor').text) > 0]
    return valores

def processar_json(caminho_arquivo):
    """
    Processa o arquivo JSON e extrai os valores de faturamento,
    ignorando valores zerados.
    """
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)

    # Extrair valores de faturamento, ignorando valores zero
    valores = [d["valor"] for d in dados if d["valor"] > 0]
    return valores

def calcular_estatisticas(valores):
    """
    Calcula o menor valor, maior valor, média mensal e
    número de dias acima da média.
    """
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for v in valores if v > media_mensal)

    return menor_valor, maior_valor, media_mensal, dias_acima_media

def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\nEscolha o arquivo para análise:")
    print("1. Faturamento XML")
    print("2. Faturamento JSON")
    print("3. Sair")

while True:
    # Exibir o menu
    exibir_menu()
    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        caminho_arquivo = r"C:\dev\teste\dados (2).xml"
        # Corrigir o XML se necessário
        caminho_arquivo_corrigido = corrigir_xml(caminho_arquivo)
        valores = processar_xml(caminho_arquivo_corrigido)
    elif opcao == 2:
        caminho_arquivo = r"C:\dev\teste\dados.json"
        valores = processar_json(caminho_arquivo)
    elif opcao == 3:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")
        continue

    # Calcular estatísticas
    menor_valor, maior_valor, media_mensal, dias_acima_media = calcular_estatisticas(valores)

    # Exibir os resultados
    print(f"\nResultados:")
    print(f"Menor valor de faturamento: R${menor_valor:.2f}")
    print(f"Maior valor de faturamento: R${maior_valor:.2f}")
    print(f"Média mensal de faturamento: R${media_mensal:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

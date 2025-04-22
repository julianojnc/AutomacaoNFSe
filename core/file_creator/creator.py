import os
import json
from pathlib import Path

def criar_estrutura_inicial():
    try:
        # Caminhos bases
        documentos_path = Path.home() / 'Documents'
        pasta_nfse = documentos_path / 'NFSE'  # Pasta principal NFSE
        
        # Subpastas
        subpastas_nfse = [
            '3D',
            'Aura',
            'Camburi',
            'CasaAcqua',
            'Facom',
            'Flexu',
            'Matrix'
        ]
        
        # Cria pasta NFSE em Documentos
        pasta_nfse.mkdir(exist_ok=True)
        
        # Cria as subpastas dentro de NFSE
        for subpasta in subpastas_nfse:
            (pasta_nfse / subpasta).mkdir(exist_ok=True)
        
        # Cria pasta ParametrosNFSe e suas subpastas Chaves e Logs
        pasta_principal = Path('C:/ParametrosNFSe')
        pasta_principal.mkdir(parents=True, exist_ok=True)
        (pasta_principal / 'Chaves').mkdir(exist_ok=True)
        (pasta_principal / 'Logs').mkdir(exist_ok=True)
        
        # Cria arquivos de configurações
        arquivos = {
            pasta_principal / 'dados_automacao.json': {
                "email": "",
                "assunto": "NFSe",
                "assunto-cancelada": "NFSe-Cancelada",
                "dt-venc-cert-dig-3d": "2025-08-04",
                "dt-venc-cert-dig-aura": "2025-08-04",
                "dt-venc-cert-dig-camburi": "2025-08-04",
                "dt-venc-cert-dig-casaacqua": "2025-08-04",
                "dt-venc-cert-dig-facom": "2025-08-04",
                "dt-venc-cert-dig-flexu": "2025-08-04",
                "dt-venc-cert-dig-matrix": "2025-08-04"
            },
            pasta_principal / 'chaves-nfse.txt': ""
        }
        
        for caminho_arquivo, conteudo in arquivos.items():
            if not caminho_arquivo.exists():
                if isinstance(conteudo, dict):
                    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                        json.dump(conteudo, f, indent=4)
                else:
                    caminho_arquivo.write_text(conteudo, encoding='utf-8')

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    criar_estrutura_inicial()
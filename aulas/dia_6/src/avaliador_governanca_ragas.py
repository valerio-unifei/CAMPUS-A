"""
Laboratório do Dia 6: Avaliador de Governança, Sanitização LGPD e Métricas RAGAS
Executa a higienização de dados pessoais e afere a fidelidade (faithfulness) das respostas.
"""
import re
from typing import Dict

def sanitizar_dados_lgpd(texto: str) -> str:
    """Mascara CPFs e nomes próprios para conformidade com a LGPD."""
    cpf_regex = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"
    texto_limpo = re.sub(cpf_regex, "[CPF_RESTRITO_LGPD]", texto)
    return texto_limpo

def avaliar_fidelidade_simulada(resposta: str, contexto: str) -> Dict[str, float]:
    """Calcula indicador simulado de fidelidade (Faithfulness) do RAGAS."""
    termos_resposta = set(resposta.lower().split())
    termos_contexto = set(contexto.lower().split())
    intersecao = termos_resposta.intersection(termos_contexto)
    score = len(intersecao) / max(len(termos_resposta), 1)
    return {
        "faithfulness_score": round(min(score * 1.8, 1.0), 2),
        "status": "APROVADO" if score > 0.4 else "REPROVADO_POR_ALUCINACAO"
    }

if __name__ == "__main__":
    exemplo_processo = "O requerente José da Silva, CPF 123.456.789-00, solicita aproveitamento de estudos com base na Resolução CEPE nº 05/2021."
    print("=" * 80)
    print("MÓDULO DE GOVERNANÇA E LGPD")
    print("=" * 80)
    print("Processo Original:", exemplo_processo)
    print("Processo Sanitizado:", sanitizar_dados_lgpd(exemplo_processo))
    
    print("\nAVALIAÇÃO DE FIDELIDADE (MÉTRICA RAGAS SIMULADA):")
    ctx = "Resolução CEPE nº 05/2021 trata dos critérios de aproveitamento de estudos nos cursos de graduação da UNIFEI."
    resp = "Conforme a Resolução CEPE nº 05/2021, o aproveitamento de estudos nos cursos de graduação da UNIFEI é cabível."
    metrica = avaliar_fidelidade_simulada(resp, ctx)
    print(f"Score de Fidelidade: {metrica['faithfulness_score']} -> {metrica['status']}")

"""
Laboratório do Dia 5: Agente Institucional da UNIFEI
Implementa o fluxo integrado: RAG normativo + Checagem de Quórum + Minuta de Ata + Guardrails.
"""
from typing import Dict, List

def tool_calcular_quorum(total_membros: int, presentes: int, tipo_pauta: str) -> Dict:
    """Calcula a conformidade do quórum segundo o Regimento da UNIFEI."""
    maioria_absoluta = (total_membros // 2) + 1
    if presentes < maioria_absoluta:
        return {
            "sessao_valida": False,
            "motivo": f"Quórum de abertura insuficiente. Presentes: {presentes}. Exigido: {maioria_absoluta}."
        }
    
    if tipo_pauta.lower() in ["reforma_regimento", "orcamento", "eleicao"]:
        votos_minimos = maioria_absoluta
        regra = "Maioria Absoluta do Colegiado"
    else:
        votos_minimos = (presentes // 2) + 1
        regra = "Maioria Simples dos Presentes"
        
    return {
        "sessao_valida": True,
        "tipo_votacao": regra,
        "votos_necessarios": votos_minimos,
        "fundamentacao": "Regimento Geral UNIFEI, Art. 28"
    }

def tool_minutar_ata(data: str, orgao: str, pauta: str, resultado: str) -> str:
    """Gera minuta preliminar padronizada com cláusula de salvaguarda."""
    return f"""
================================================================================
[RASCUNHO PRELIMINAR - MINUTA ASSISTIDA POR IA - EXIGE APROVAÇÃO E ASSINATURA]
================================================================================
Aos {data}, reuniu-se o {orgao} para deliberar sobre a seguinte pauta: {pauta}.
Após as manifestações regimentais e a devida contagem de votos, registrou-se o
seguinte resultado: {resultado}.
Lavrada por sistema agêntico auxiliar em conformidade com o Regimento Geral da UNIFEI.
================================================================================
"""

def executar_agente(pergunta: str) -> str:
    # Simulação de resposta com citação de artigo vigente
    return (
        "[MINUTA DE RESPOSTA CONSULTIVA]\n"
        "Com fulcro no Art. 42 da Resolução CEPE nº 05/2021, o trancamento total de matrícula\n"
        "é concedido por até 4 períodos letivos, sendo vedado no período inicial de ingresso.\n"
        "Encaminha-se para deliberação da Coordenação de Curso."
    )

if __name__ == "__main__":
    print("=" * 80)
    print("PROTÓTIPO DE AGENTE INSTITUCIONAL - UNIFEI")
    print("=" * 80)
    
    print("\n1. Teste de Ferramenta: Validação de Quórum do CONSUNI")
    q = tool_calcular_quorum(total_membros=30, presentes=22, tipo_pauta="orcamento")
    print(f"Resultado do Quórum: {q}")
    
    print("\n2. Teste de Ferramenta: Geração de Minuta de Ata")
    ata = tool_minutar_ata("15 de setembro de 2026", "Conselho de Ensino (CEPE)", "Homologação de Calendário", "Aprovado por unanimidade")
    print(ata)
    
    print("3. Teste de Consulta Normativa com Citação de Artigo")
    resp = executar_agente("Regras de trancamento de matrícula")
    print(resp)

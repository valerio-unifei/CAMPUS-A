"""
Laboratório do Dia 1: Comparativo entre Geração Paramétrica e RAG Normativo
Simula a diferença de confiabilidade entre um LLM consultado 'a seco' e um LLM ancorado
em um extrato normativo da UNIFEI.
"""

EXTRATO_NORMATIVO_UNIFEI = """
[RESOLUÇÃO CEPE/UNIFEI Nº 05/2021 - REGIME DIDÁTICO-CIENTÍFICO]
Art. 42. O trancamento total de matrícula poderá ser concedido pela Coordenação de Curso 
ao discente de graduação por no máximo 4 (quatro) períodos letivos, consecutivos ou não.
Parágrafo único. Não será concedido trancamento de matrícula no primeiro período letivo 
de ingresso do discente, ressalvados casos de prestação de serviço militar obrigatório 
ou tratamento de saúde próprio devidamente comprovado por junta médica oficial.

Art. 43. O trancamento parcial em componente curricular poderá ser requerido até o limite 
de 25% (vinte e cinco por cento) dos dias letivos previstos no Calendário Acadêmico, 
desde que o estudante permaneça inscrito na carga horária mínima regimental.
"""

def simular_llm_sem_contexto(pergunta: str) -> str:
    """Simula resposta sem contexto (alucinação plausível)."""
    return (
        "[RESPOSTA SEM CONTEXTO - ALUCINAÇÃO PLAUSÍVEL]\n"
        "O estudante pode solicitar trancamento de matrícula em qualquer momento no portal do aluno,\n"
        "sendo permitido trancar até 6 semestres consecutivos mediante taxa administrativa.\n"
        "(AVISO CRÍTICO: Não cita artigo nem resolução. Informações incorretas para a UNIFEI!)"
    )

def simular_llm_com_rag(pergunta: str, contexto: str) -> str:
    """Simula resposta fidedigna ancorada no documento oficial."""
    return (
        "[RESPOSTA ANCORADA EM RAG - FIDEDIGNA]\n"
        "Conforme a Resolução CEPE/UNIFEI Nº 05/2021:\n"
        "1. Trancamento Total (Art. 42): Permitido por até 4 períodos letivos (consecutivos ou não).\n"
        "   É vedado no 1º período letivo de ingresso, salvo serviço militar obrigatório ou junta médica.\n"
        "2. Trancamento Parcial (Art. 43): Permitido até 25% dos dias letivos do Calendário Acadêmico,\n"
        "   exigindo permanência na carga horária mínima regimental.\n"
        "(FONTE: Resolução CEPE/UNIFEI Nº 05/2021, Art. 42 e 43. Status: VIGENTE)"
    )

if __name__ == "__main__":
    pergunta = "Quais são as regras e prazos para trancamento de matrícula na UNIFEI?"
    print("=" * 80)
    print(f"CONSULTA: {pergunta}")
    print("=" * 80)
    print("\n--- CENÁRIO 1: MODELO SEM CONTEXTO (ZERO-SHOT) ---")
    print(simular_llm_sem_contexto(pergunta))
    print("\n--- CENÁRIO 2: MODELO ANCORADO EM REGIMENTO (RAG) ---")
    print(simular_llm_com_rag(pergunta, EXTRATO_NORMATIVO_UNIFEI))
    print("=" * 80)

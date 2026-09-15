"""
Laboratório do Dia 3: Roteador de Subagentes e Guardrail de Competência
Demonstra o padrão de triagem semântica para subagentes e a atuação de guardrails.
"""
from typing import Dict

def subagente_academico(consulta: str) -> str:
    return "Minuta Técnica: O requerimento discente encontra amparo na Resolução CEPE nº 05/2021."

def subagente_rh(consulta: str) -> str:
    return "Minuta Técnica: A concessão de licença capacitação subordina-se ao Art. 87 da Lei 8.112/1990."

def subagente_compras(consulta: str) -> str:
    return "Minuta Técnica: O termo de referência atende aos requisitos do Art. 18 da Lei 14.133/2021."

def guardrail_competencia_publica(texto_resposta: str) -> str:
    """Impede que o agente afirme ter deliberado ou assinado o ato."""
    gatilhos_proibidos = ["eu autorizo", "fica deferido", "minha decisão é", "declaro aprovado"]
    for gatilho in gatilhos_proibidos:
        if gatilho in texto_resposta.lower():
            return "[INTERCEPTAÇÃO GUARDRAIL]: Resposta suspensa. O agente não possui competência decisória. O parecer foi convertido para minuta consultiva."
    return f"[MINUTA CONSULTIVA HITL] {texto_resposta} [Requer assinatura da autoridade competente]"

def roteador_institucional(consulta: str) -> Dict[str, str]:
    c_lower = consulta.lower()
    if any(k in c_lower for k in ["aluno", "matrícula", "disciplina", "curso", "cepe"]):
        subagente = "Subagente Acadêmico"
        resposta = subagente_academico(consulta)
    elif any(k in c_lower for k in ["servidor", "férias", "licença", "capacitação", "progep"]):
        subagente = "Subagente de RH"
        resposta = subagente_rh(consulta)
    elif any(k in c_lower for k in ["licitação", "pregão", "contrato", "compra", "empenho"]):
        subagente = "Subagente de Compras"
        resposta = subagente_compras(consulta)
    else:
        return {
            "status": "RECUSA_SEGURA",
            "mensagem": "Matéria não identificada nos normativos pré-configurados. Encaminhado ao Protocolo Geral."
        }
        
    resposta_filtrada = guardrail_competencia_publica(resposta)
    return {
        "status": "SUCESSO",
        "subagente_acionado": subagente,
        "resposta_final": resposta_filtrada
    }

if __name__ == "__main__":
    consultas = [
        "Como funciona a licença para capacitação do servidor docente?",
        "Qual a regra de trancamento de disciplina do curso de Engenharia?",
        "Qual o prazo para impugnação de edital de pregão eletrônico?",
        "Desejo fazer uma viagem particular sem autorização."
    ]
    
    print("=" * 80)
    print("SIMULADOR DE ROTEADOR E GUARDRAILS INSTITUCIONAIS")
    print("=" * 80)
    for c in consultas:
        res = roteador_institucional(c)
        print(f"\nConsulta: {c}")
        print(f"Roteamento: {res.get('subagente_acionado', 'Nenhum')}")
        print(f"Retorno: {res.get('resposta_final', res.get('mensagem'))}")

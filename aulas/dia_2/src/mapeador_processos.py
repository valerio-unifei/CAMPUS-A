"""
Laboratório do Dia 2: Avaliador de Elegibilidade de Processos Administrativos
Analisa processos da UNIFEI e classifica se são adequados para automação agêntica ou
se exigem tramitação puramente humana.
"""
import json
import os

PROCESSOS_AMOSTRA = [
    {
        "id_processo": "UNIFEI-PROC-01",
        "nome": "Verificação de Pré-requisitos para Colação de Grau",
        "orgao": "Secretaria de Registro Acadêmico / PRG",
        "volume_mensal": 450,
        "regras_determinadas": True,
        "envolve_juizo_merito": False,
        "norma_base": "Resolução CEPE nº 10/2020"
    },
    {
        "id_processo": "UNIFEI-PROC-02",
        "nome": "Julgamento de Recurso de Processo Administrativo Disciplinar (PAD)",
        "orgao": "Comissão de Ética / CONSUNI",
        "volume_mensal": 3,
        "regras_determinadas": False,
        "envolve_juizo_merito": True,
        "norma_base": "Lei 8.112/1990 e Regimento Geral UNIFEI"
    },
    {
        "id_processo": "UNIFEI-PROC-03",
        "nome": "Emissão de Minuta de Despacho para Validação de Estágio Não Obrigatório",
        "orgao": "Coordenação de Curso de Engenharia",
        "volume_mensal": 180,
        "regras_determinadas": True,
        "envolve_juizo_merito": False,
        "norma_base": "Instrução Normativa PRG nº 02/2022"
    }
]

def classificar_processo(proc: dict) -> dict:
    if proc["envolve_juizo_merito"]:
        status = "NAO_ELEGIVEL"
        recomendacao = "Processo requer juízo discricionário e mérito humano. Automação autônoma vedada."
    elif proc["regras_determinadas"] and proc["volume_mensal"] >= 100:
        status = "ALTA_PRIORIDADE"
        recomendacao = "Candidato ideal para agente com minutas supervisionadas (Human-in-the-Loop)."
    else:
        status = "MEDIA_PRIORIDADE"
        recomendacao = "Automatizável com pipeline assistivo pontual."
        
    resultado = dict(proc)
    resultado["classificacao_agente"] = status
    resultado["parecer_tecnico"] = recomendacao
    return resultado

if __name__ == "__main__":
    analisados = [classificar_processo(p) for p in PROCESSOS_AMOSTRA]
    output_dir = os.path.join(os.path.dirname(__file__), "..", "exemplos")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "processos_mapeados.json")
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(analisados, f, indent=2, ensure_ascii=False)
        
    print(f"[SUCESSO] Processos avaliados salvos em: {output_file}")
    for item in analisados:
        print(f"- {item['nome']} -> [{item['classificacao_agente']}]")

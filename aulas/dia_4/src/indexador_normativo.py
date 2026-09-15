"""
Laboratório do Dia 4: Estruturação de Base Normativa com Grafo de Vigência
Cria chunks jurídicos estruturados com metadados de vigência e executa busca filtrada.
"""
import json
import os
from typing import List, Dict

NORMAS_BRUTAS = [
    {
        "id": "UNIFEI-RES-CEPE-2021-05-ART-10",
        "documento": {"tipo": "Resolução", "orgao": "CEPE", "numero": "05", "ano": 2021},
        "artigo": "Art. 10",
        "texto": "Art. 10. O regime letivo nos cursos de graduação da UNIFEI é semestral, estruturado em períodos letivos regulares de no mínimo 100 (cem) dias de trabalho acadêmico efetivo.",
        "status_vigencia": "VIGENTE",
        "tags": ["regime letivo", "calendário", "graduação"]
    },
    {
        "id": "UNIFEI-RES-CEPE-2015-01-ART-10",
        "documento": {"tipo": "Resolução", "orgao": "CEPE", "numero": "01", "ano": 2015},
        "artigo": "Art. 10",
        "texto": "Art. 10. O período letivo terá duração de 90 dias úteis de aulas presenciais.",
        "status_vigencia": "REVOGADO",
        "revogado_por": "UNIFEI-RES-CEPE-2021-05-ART-10",
        "tags": ["regime letivo", "calendário", "graduação"]
    },
    {
        "id": "UNIFEI-RES-CONSUNI-2022-12-ART-04",
        "documento": {"tipo": "Resolução", "orgao": "CONSUNI", "numero": "12", "ano": 2022},
        "artigo": "Art. 4º",
        "texto": "Art. 4º. O Conselho Universitário reúne-se ordinariamente a cada 60 (sessenta) dias e extraordinariamente sempre que convocado pelo Reitor ou por um terço de seus membros.",
        "status_vigencia": "VIGENTE",
        "tags": ["consuni", "reunião", "convocação", "quórum"]
    }
]

def buscar_norma(termo: str, base: List[Dict], apenas_vigentes: bool = True) -> List[Dict]:
    resultados = []
    termo_l = termo.lower()
    for doc in base:
        if apenas_vigentes and doc["status_vigencia"] != "VIGENTE":
            continue
        if any(termo_l in tag for tag in doc["tags"]) or termo_l in doc["texto"].lower():
            resultados.append(doc)
    return resultados

if __name__ == "__main__":
    output_dir = os.path.join(os.path.dirname(__file__), "..", "exemplos")
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "base_unifei_estruturada.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(NORMAS_BRUTAS, f, indent=2, ensure_ascii=False)
        
    print(f"[OK] Base de normas indexada com sucesso em: {out_file}")
    
    consulta = "regime letivo"
    print(f"\nBusca por: '{consulta}' (Apenas VIGENTES):")
    res_vigentes = buscar_norma(consulta, NORMAS_BRUTAS, apenas_vigentes=True)
    for r in res_vigentes:
        print(f"-> [{r['status_vigencia']}] {r['documento']['tipo']} {r['documento']['numero']}/{r['documento']['ano']} - {r['texto']}")

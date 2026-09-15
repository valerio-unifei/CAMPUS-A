# DIA 4: Construção da Base de Conhecimento Normativa

**Carga Horária:** 3h30 | **Nível:** Médio  
**Estudo de Caso Institucional:** UNIFEI (Universidade Federal de Itajubá)

---

## 1. Visão Geral e Objetivos de Aprendizagem
Nesta aula, os participantes aprendem a construir o alicerce de dados do agente institucional: a ingestão, o tratamento e a indexação de normas jurídicas e regulamentos internos da UNIFEI. Abordamos os gargalos de PDFs históricos (OCR), a técnica de chunking estruturado por unidades regimentais e o tratamento de grafos de vigência e revogação temporal.

### Objetivos Específicos:
1. Implementar pipelines de ingestão documental superando desafios de digitalização, OCR e tabelas anexas.
2. Dominar a técnica de **Chunking Estruturado por Artigo**, rejeitando o chunking ingênuo por tamanho fixo.
3. Modelar esquemas JSON ricos em metadados com controle rigoroso de vigência (`VIGENTE`, `REVOGADO`, `ALTERADO_PARCIALMENTE`).
4. Configurar bancos vetoriais com filtros relacionais booleanos para exclusão de normas pretéritas revogadas.
5. Produzir a **Entrega 3 do Projeto Final**: Amostra da base de conhecimento normativa estruturada em JSON.

---

## 2. Cronograma Minuto a Minuto

| Horário | Bloco | Atividade | Metodologia |
|:---:|:---:|---|---|
| **00:00 - 00:50** | 1.0 | Ingestão Documental no Setor Público: OCR, Ruídos e Limpeza | Engenharia de Dados |
| **00:50 - 01:40** | 2.0 | Por que o chunking de 500 tokens falha no Direito: Chunking por Artigo | Análise Comparativa |
| **01:40 - 02:30** | 3.0 | O Problema da Norma Revogada: Grafos de Vigência e Versionamento | Modelagem de Dados |
| **02:30 - 03:00** | 4.1 | Simulação do indexador com filtro de vigência em Python | Execução Prática |
| **03:00 - 03:30** | 4.2 | **Prática Guiada 4 (Entrega 3 do Projeto Final):** Estruturação do JSON | Exercício Prático |

---

## 3. Desenvolvimento Teórico Aprofundado

### Bloco 1: A Falha do Chunking de Comprimento Fixo
Sistemas RAG genéricos costumam fatiar documentos a cada 500 caracteres ou 256 tokens com sobreposição (*overlap*). Em textos jurídicos, isso gera desastres interpretativos:

```
[Exemplo de Chunking Ingênuo Cortando a Norma ao Meio]

CHUNK 1:
"Art. 15. O estudante que obtiver rendimento acadêmico inferior a 5,0 (cinco) 
em três disciplinas consecutivas será imediatamente desligado da UNIFEI." 
<--- FIM DO CHUNK 1 (Modelo interpreta como regra absoluta de jubilamento!)

CHUNK 2:
"Parágrafo único. O disposto no caput deste artigo não se aplica aos discentes 
que comprovarem vínculo empregatício formal ou responsabilidade de cuidado familiar."
<--- FIM DO CHUNK 2 (A exceção vital ficou desvinculada da regra geral!)
```

* **A Solução do Chunking por Artigo:**
  O bloco atômico no banco de dados deve ser o **Artigo Completo**:
  $$\text{Chunk} = \text{Caput} + \sum \text{Parágrafos} + \sum \text{Incisos} + \sum \text{Alíneas}$$

---

## 4. Laboratório Prático 4 e Entrega 3 do Projeto Final
1. Execute o indexador normativo:
   ```bash
   python dia_4/src/indexador_normativo.py
   ```
2. Analise a base JSON estruturada em `dia_4/exemplos/base_unifei_estruturada.json`.
3. **Entrega 3 do Projeto Final:** Cada grupo salva sua amostra em `projeto_final_template/3_base_normativa_amostra.json`.

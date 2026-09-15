# CAMPUS-A
**Capacitação em Agentes e Modelos de Processos na Universidade e Setor Administrativo**

**Formato:** 21 horas | 6 dias | 3h30 por dia | Níveis Básico → Médio → Avançado
**Estudo de caso institucional:** UNIFEI (Universidade Federal de Itajubá)

## Estrutura geral

| Dia | Nível | Tema | Duração |
|---|---|---|---|
| 1 | Básico | Fundamentos de Agentes de IA | 3h30 |
| 2 | Básico | Panorama Normativo e Mapeamento de Processos | 3h30 |
| 3 | Médio | Arquitetura de Agentes para o Setor Público | 3h30 |
| 4 | Médio | Construção da Base de Conhecimento Normativa | 3h30 |
| 5 | Avançado | Desenvolvimento Prático de um Agente Institucional | 3h30 |
| 6 | Avançado | Governança, Avaliação e Implantação + Projeto Final | 3h30 |

---

## NÍVEL BÁSICO

### Dia 1 — Fundamentos de Agentes de IA (3h30)

**Objetivo:** entender o que é um agente de IA e por que isso importa para o setor público.

| Bloco | Duração | Conteúdo |
|---|---|---|
| 1 | 1h00 | O que é um LLM; diferença entre chatbot, RAG e agente autônomo com ferramentas |
| 2 | 1h00 | Componentes de um agente: percepção, raciocínio/planejamento, ação (ferramentas), memória |
| 3 | 1h00 | Por que RAG é o ponto de partida para o domínio normativo: o agente deve buscar a norma, não "inventá-la"; riscos de alucinação e de citar norma revogada |
| 4 | 0h30 | **Prática:** comparar, em uma plataforma de IA, uma resposta sem contexto normativo vs. uma resposta ancorada em um trecho real de Regimento fornecido como contexto |

---

### Dia 2 — Panorama Normativo e Mapeamento de Processos (3h30)

**Objetivo:** conhecer a hierarquia normativa da universidade e identificar processos administrativos automatizáveis.

| Bloco | Duração | Conteúdo |
|---|---|---|
| 1 | 1h00 | Hierarquia normativa: Constituição/leis federais (LDB, Lei 8.112/90, Lei 9.784/99, LAI, LGPD) → Estatuto → Regimento Geral → Regimentos de Conselhos → Resoluções/Portarias |
| 2 | 1h00 | Estrutura de órgãos administrativos: Reitoria, Pró-Reitorias, Conselhos Superiores, Colegiados de unidades, Comissões, Secretarias de Conselhos |
| 3 | 1h00 | Critérios para escolher processos a automatizar (alto volume repetitivo, prazos bem definidos, redação estruturada) vs. o que **não** automatizar sem forte supervisão (deliberações de mérito, casos omissos) |
| 4 | 0h30 | **Prática:** preencher tabela classificando 3–5 documentos reais da UNIFEI por nível hierárquico, órgão emissor e vigência; mapear 2 processos candidatos à automação |

---

## NÍVEL MÉDIO

### Dia 3 — Arquitetura de Agentes para o Setor Público (3h30)

**Objetivo:** projetar a arquitetura técnica de um agente institucional seguro.

| Bloco | Duração | Conteúdo |
|---|---|---|
| 1 | 1h00 | Arquitetura RAG institucional: base vetorial → busca semântica → geração com citação da fonte exata (artigo/parágrafo) |
| 2 | 1h00 | Padrão roteador + subagentes especializados por domínio (acadêmico, pessoal, patrimonial); ferramentas (tools) que o agente pode acessar (consulta a processos, calendário, geração de documentos) |
| 3 | 1h00 | Guardrails essenciais: nunca decidir em nome de colegiado, sempre citar fonte e vigência, recusar-se diante de ambiguidade/omissão, registrar logs (auditabilidade) |
| 4 | 0h30 | **Prática:** desenhar a arquitetura de um "Agente Assistente" para um órgão real (ex.: Conselho de Ensino, Pesquisa e Extensão), indicando base de conhecimento, roteador, guardrails e ponto de validação humana |

---

### Dia 4 — Construção da Base de Conhecimento Normativa (3h30)

**Objetivo:** transformar documentos institucionais em uma base consultável pelo agente.

| Bloco | Duração | Conteúdo |
|---|---|---|
| 1 | 1h00 | Ingestão de PDFs (incluindo OCR para normas escaneadas); chunking estruturado por artigo/parágrafo (não por tamanho arbitrário) |
| 2 | 1h00 | Metadados essenciais: tipo de documento, órgão emissor, data, **status de vigência** (vigente/revogado/alterado); versionamento normativo (como tratar resolução que altera artigos de outra) |
| 3 | 1h00 | Ferramentas comuns: parsers de PDF, bancos vetoriais (Chroma, pgvector, FAISS), frameworks de orquestração (LangChain, LlamaIndex) ou implementação direta via API de LLM |
| 4 | 0h30 | **Prática:** estruturar manualmente um JSON de exemplo a partir de 1 artigo real do Estatuto/Regimento da UNIFEI, com todos os metadados |

---

## NÍVEL AVANÇADO

### Dia 5 — Desenvolvimento Prático de um Agente Institucional (3h30)

**Objetivo:** construir um protótipo funcional de agente de apoio a um órgão colegiado.

| Bloco | Duração | Conteúdo |
|---|---|---|
| 1 | 1h00 | Implementação de RAG básico sobre a base construída no Dia 4 |
| 2 | 1h00 | Funcionalidades assistivas: responder dúvidas normativas com citação; gerar minuta de ata a partir de notas soltas (sempre como rascunho); checar quórum com base no artigo aplicável; gerar checklist de prazos |
| 3 | 1h00 | Guardrails de saída: toda resposta cita a fonte; se não houver base normativa suficiente, o agente sinaliza e recomenda análise jurídica/humana |
| 4 | 0h30 | **Prática:** protótipo respondendo a 5 perguntas normativas reais da universidade, com citação de fonte |

---

### Dia 6 — Governança, Avaliação, Implantação e Projeto Final (3h30)

**Objetivo:** garantir uso responsável do agente e consolidar o projeto do curso.

| Bloco | Duração | Conteúdo |
|---|---|---|
| 1 | 0h45 | Governança: LGPD (dados pessoais em processos), LAI (transparência), accountability ("o agente assessora, o órgão decide e assina"), trilha de auditoria |
| 2 | 0h45 | Avaliação: precisão de citação, taxa de alucinação, taxa de escalonamento correto; metodologia de teste com gabarito validado por especialistas |
| 3 | 0h30 | Implantação faseada: piloto restrito → ajustes → expansão gradual; comunicação e treinamento dos servidores |
| 4 | 1h30 | **Apresentação do Projeto Final** (ver abaixo) |

---

## Projeto Final (apresentado no Dia 6)

Cada participante/grupo entrega um pacote com:

1. Escopo do agente e processo(s) automatizado(s), com justificativa (Dia 2).
2. Diagrama de arquitetura com guardrails e ponto de validação humana (Dia 3).
3. Amostra da base de conhecimento estruturada com metadados de vigência (Dia 4).
4. Protótipo (ou especificação técnica detalhada) respondendo perguntas reais com citação de fonte (Dia 5).
5. Checklist de governança (LGPD/LAI/accountability) aplicado ao agente proposto (Dia 6).

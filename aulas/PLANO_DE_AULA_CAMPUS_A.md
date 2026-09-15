# CAMPUS-A: Capacitacao em Agentes e Modelos de Processos na Universidade e Setor Administrativo

**Formato:** 21 horas | 6 dias | 3h30 por dia | Niveis Basico -> Medio -> Avancado  
**Estudo de Caso Institucional:** UNIFEI (Universidade Federal de Itajuba)  
**Publico-alvo:** Servidores tecnico-administrativos, gestores publicos universitarios, secretarias de orgaos colegiados, desenvolvedores e pesquisadores institucionais.

---

## ESTRUTURA GERAL DO CURSO

| Dia | Nivel | Tema | Duracao | Foco Principal |
|:---:|:---:|---|:---:|---|
| **1** | Basico | Fundamentos de Agentes de IA | 3h30 | LLMs vs. RAG vs. Agentes; Riscos no setor publico |
| **2** | Basico | Panorama Normativo e Mapeamento de Processos | 3h30 | Hierarquia juridica (UNIFEI); Matriz de automacao |
| **3** | Medio | Arquitetura de Agentes para o Setor Publico | 3h30 | Roteadores, Subagentes, Tools e Guardrails |
| **4** | Medio | Construcao da Base de Conhecimento Normativa | 3h30 | Ingestao, Chunking por artigo, Metadados de vigencia |
| **5** | Avancado | Desenvolvimento Pratico de um Agente Institucional | 3h30 | Implementacao em codigo, RAG estrito, Minutas e Quorum |
| **6** | Avancado | Governanca, Avaliacao e Implantacao + Projeto Final | 3h30 | LGPD, RAGAS, Roadmap institucional e Banca final |

---

# DIA 1 -- Fundamentos de Agentes de IA
**Carga Horaria:** 3h30 | **Nivel:** Basico  
**Objetivo Pedagogico:** Compreender a mecanica interna de LLMs, diferenciar com rigor conceitual chatbots, RAG e agentes autonomos com ferramentas, e assimilar os riscos criticos de alucinacao no contexto juridico-normativo de uma universidade federal.

### Cronograma Detalhado
* **00:00 - 01:00 (Bloco 1) | Da Predicao de Tokens a Tomada de Acao**
  * O que e um LLM: Redes neurais autorregressivas (Transformers), mecanismo de autoatencao e amostragem probabilistica.
  * O espectro da autonomia:
    1. *Chatbot Parametrico:* Dependente unicamente dos pesos pre-treinados; tende a inventar dispositivos normativos com alta conviccao.
    2. *RAG (Retrieval-Augmented Generation):* Injecao dinamica de documentos oficiais na janela de contexto sob demanda.
    3. *Agente Autonomo:* Orquestrador ReAct que analisa objetivos, escolhe ferramentas (APIs, bancos vetoriais, sistemas legados) e sintetiza resultados.
* **01:00 - 02:00 (Bloco 2) | Anatomia de um Agente Cognitivo**
  * Percepcao (Inputs estruturados e nao-estruturados de processos SEI/SIPAC).
  * Raciocinio e Planejamento (padrao ReAct: Thought -> Action -> Observation).
  * Acao (Schemas JSON de chamadas de funcao).
  * Memoria (Trabalho/Curto Prazo vs. Longo Prazo institucional).
* **02:00 - 03:00 (Bloco 3) | O Imperativo do RAG no Dominio Publico**
  * Riscos da alucinacao no setor publico: perda de prazos recursais, nulidade de atos administrativos e quebra de isonomia.
  * O problema da norma revogada no tempo: por que pesos congelados falham.
  * Principio da Ancoragem Factual (Grounding) 1:1 com normas vigentes.
* **03:00 - 03:30 (Bloco 4) | Pratica Guiada 1: Comparativo Sem Contexto vs. Ancorado**
  * Teste cego de consulta sobre regime disciplinar discente no ChatGPT/Claude sem contexto vs. consulta com injecao do extrato do Regimento da UNIFEI.

---

# DIA 2 -- Panorama Normativo e Mapeamento de Processos
**Carga Horaria:** 3h30 | **Nivel:** Basico  
**Objetivo Pedagogico:** Mapear a hierarquia normativa federal e universitaria (estudo de caso UNIFEI), reconhecer a divisao de competencias entre orgaos e aplicar a matriz de elegibilidade para automacao agSafe.

### Cronograma Detalhado
* **00:00 - 01:00 (Bloco 1) | Piramide de Kelsen e Hierarquia Normativa nas IFES**
  * Nivel Federal: CF/88 (Art. 207), LDB (Lei 9.394/96), Lei 8.112/90, Lei 9.784/99 (Processo Administrativo), LAI e LGPD.
  * Nivel UNIFEI: Estatuto -> Regimento Geral -> Regimentos Internos dos Conselhos (CONSUNI, CEPE) -> Resolucoes Tematicas -> Portarias e Instrucoes Normativas.
  * Criterios de solucao de antinomias temporais e materiais no RAG.
* **01:00 - 02:00 (Bloco 2) | Estrutura Administrativa e Orgaos Colegiados**
  * CONSUNI, CEPE, Conselhos de Instituto e Colegiados de Curso.
  * Reitoria, Pro-Reitorias (PRG, PRPPG, PROAD, PROGEP) e Secretarias de Conselhos.
* **02:00 - 03:00 (Bloco 3) | Matriz de Elegibilidade Agente-Processo**
  * O que automatizar: Rotinas repetitivas, checklists documentais, triagem de requerimentos, checagem de prazos regimentais e minutas de mero expediente.
  * O que NAO automatizar de forma autonoma: Juizo de merito academico, deliberacoes disciplinares e integracao de lacunas/casos omissos.
* **03:00 - 03:30 (Bloco 4) | Pratica Guiada 2 (Entrega 1 do Projeto Final)**
  * Preenchimento da matriz de mapeamento de 2 processos candidatos da UNIFEI por grupo com justificativa de volume e risco.

---

# DIA 3 -- Arquitetura de Agentes para o Setor Publico
**Carga Horaria:** 3h30 | **Nivel:** Medio  
**Objetivo Pedagogico:** Projetar arquiteturas multiagente corporativas e seguras para universidades, baseadas no padrao Router-Subagente, com ferramentas restritas e guardrails de conformidade.

### Cronograma Detalhado
* **00:00 - 01:00 (Bloco 1) | Pipeline RAG Institucional Especializado**
  * Busca vetorial densa somada a busca esparsa (BM25) para capturar termos exatos de leis e artigos.
  * Re-ranking semantico e injecao de metadados de rastreabilidade no payload.
* **01:00 - 02:00 (Bloco 2) | Topologia Router + Subagentes de Dominio**
  * Agente Supervisor/Roteador despachando para Subagente Academico, Subagente de Pessoal e Subagente de Compras.
  * Definicao de Ferramentas: ferramentas Read-Only e ferramentas de Staging/Minuta (sem poder de publicacao final).
* **02:00 - 03:00 (Bloco 3) | Guardrails Institucionais e Auditabilidade**
  * Bloqueio sintatico de expressoes decisorias ("declaro aprovado" -> "minuta sugerida").
  * Protocolo de recusa automatica diante de controversia ou ausencia de base legal.
  * Estrutura de logs imutaveis para prestacao de contas aos orgaos de controle (CGU/TCU).
* **03:00 - 03:30 (Bloco 4) | Pratica Guiada 3 (Entrega 2 do Projeto Final)**
  * Desenho do diagrama de arquitetura do agente institucional do grupo em Mermaid, mapeando roteador, base, ferramentas e ponto de validacao humana (HITL).

---

# DIA 4 -- Construcao da Base de Conhecimento Normativa
**Carga Horaria:** 3h30 | **Nivel:** Medio  
**Objetivo Pedagogico:** Superar os gargalos de ingestao de documentos juridicos e administrativos (OCR, tabelas), dominar tecnicas de chunking estruturado por artigo/paragrafo e modelar metadados de vigencia e revogacao.

### Cronograma Detalhado
* **00:00 - 01:00 (Bloco 1) | Ingestao de PDFs e Segmentacao Estruturada**
  * Desafios: normas antigas escaneadas (necessidade de OCR), carimbos de assinatura ICP-Brasil e tabelas anexas.
  * Por que chunking por tamanho fixo (ex: 500 tokens) destroi a semantica juridica.
  * Chunking por Unidade Normativa: preservando Artigo + Paragrafos + Incisos no mesmo bloco coeso.
* **01:00 - 02:00 (Bloco 2) | Modelagem de Metadados e Grafo de Vigencia**
  * Estrutura de metadados: tipo de documento, orgao emissor, numero, ano, data de publicacao e status (VIGENTE / REVOGADO / SUSPENSO).
  * Como lidar com resolucoes modificadoras que alteram pontualmente artigos de resolucoes anteriores.
* **02:00 - 03:00 (Bloco 3) | Stack Tecnologica de Armazenamento e Modelos**
  * Comparativo: ChromaDB para prototipagem rapida vs. pgvector para producao integrada a bancos PostgreSQL corporativos.
  * Modelos de embedding otimizados para o idioma portugues e contexto legal.
* **03:00 - 03:30 (Bloco 4) | Pratica Guiada 4 (Entrega 3 do Projeto Final)**
  * Estruturacao manual do schema JSON completo de um artigo complexo do Regimento Geral da UNIFEI com todos os campos de controle de vigencia.

---

# DIA 5 -- Desenvolvimento Pratico de um Agente Institucional
**Carga Horaria:** 3h30 | **Nivel:** Avancado  
**Objetivo Pedagogico:** Implementar em codigo Python um prototipo funcional de agente de apoio a secretarias de conselho, executando busca vetorial com filtro de vigencia, gerador de minutas de ata e checagem automatica de quorum deliberativo.

### Cronograma Detalhado
* **00:00 - 01:00 (Bloco 1) | Montagem do Pipeline RAG em Codigo Python**
  * Conexao com banco vetorial e aplicacao de filtros booleanos rigidos para recuperar apenas documentos vigentes.
  * Engenharia do System Prompt institucional com instrucoes estritas de citacao de dispositivos legais.
* **01:00 - 02:00 (Bloco 2) | Construcao das Ferramentas Operacionais**
  * Implementacao da Tool de Checagem de Quorum (maioria simples vs. maioria absoluta regimental).
  * Implementacao da Tool de Geracao de Minuta de Ata a partir de notas de sessao colegiada.
* **02:00 - 03:00 (Bloco 3) | Implementacao dos Guardrails via Codigo**
  * Interceptadores de saida em Python: deteccao de ausencia de fontes normativas e bloqueio de linguagem imperativa nao-autorizada.
* **03:00 - 03:30 (Bloco 4) | Pratica Guiada 5 (Entrega 4 do Projeto Final)**
  * Bateria de 5 consultas reais da rotina academica e administrativa da UNIFEI submetidas ao prototipo, avaliando exatidao das citacoes.

---

# DIA 6 -- Governanca, Avaliacao, Implantacao e Projeto Final
**Carga Horaria:** 3h30 | **Nivel:** Avancado  
**Objetivo Pedagogico:** Estabelecer o arcabouco de conformidade com LGPD e LAI, aplicar metricas cientificas de avaliacao de RAG/agentes (RAGAS) e conduzir a apresentacao do Projeto Final perante banca docente.

### Cronograma Detalhado
* **00:00 - 00:45 (Bloco 1) | Conformidade Legal, LGPD e Responsabilizacao**
  * Anonimizacao e tratamento de dados pessoais sensiveis em processos administrativos antes do processamento por IA.
  * Principio do Human-in-the-Loop como garantia de responsabilizacao juridica do servidor publico assinante.
* **00:45 - 01:30 (Bloco 2) | Metricas de Avaliacao e Golden Dataset**
  * Metricas do framework RAGAS: Faithfulness (Fidelidade / anti-alucinacao), Answer Relevance e Context Recall.
  * Construcao de conjunto de casos-padrao (Golden Dataset) para validacao continua antes de atualizacoes de modelos.
* **01:30 - 02:00 (Bloco 3) | Roadmap de Implantacao Institucional**
  * Fases de adocao: Sandbox TI -> Piloto em Secretaria de Conselho -> Homologacao Assistida -> Producao com monitoramento.
* **02:00 - 03:30 (Bloco 4) | Apresentacao do Projeto Final**
  * Apresentacao das solucoes desenvolvidas pelos grupos (12 min por equipe + feedback pedagogico).

---

## ESTRUTURA DO PROJETO FINAL E RUBRICA DE AVALIACAO

Cada grupo consolida um pacote tecnico com os 5 componentes desenvolvidos ao longo do curso:
1. **Escopo e Processos (Dia 2):** Justificativa do processo administrativo mapeado na UNIFEI.
2. **Arquitetura Tecnica (Dia 3):** Diagrama com Roteador, Ferramentas, Guardrails e ponto HITL.
3. **Amostra da Base Normativa (Dia 4):** JSON estruturado com metadados de vigencia e rastreabilidade.
4. **Prototipo Funcional (Dia 5):** Codigo executavel ou especificacao tecnica testada contra 5 cenarios normativos reais.
5. **Checklist de Governanca (Dia 6):** Matriz de protecao de dados (LGPD) e definicao de trilhas de auditoria.

### Rubrica de Pontuacao (Total: 100 pontos):
* **Fidelidade Normativa e Citacao Estrita:** 30 pontos
* **Arquitetura Tecnica, Ferramentas e Guardrails:** 25 pontos
* **Qualidade da Modelagem de Dados e Metadados:** 15 pontos
* **Relevancia Administrativa para a UNIFEI:** 15 pontos
* **Governanca, Seguranca e Conformidade Legal:** 15 pontos

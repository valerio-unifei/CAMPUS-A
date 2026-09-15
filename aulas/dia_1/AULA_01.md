# DIA 1: Fundamentos de Agentes de IA

**Carga Horária:** 3h30 | **Nível:** Básico  
**Estudo de Caso Institucional:** UNIFEI (Universidade Federal de Itajubá)  
**Público-Alvo:** Gestores acadêmicos, secretários de conselhos, servidores técnicos e desenvolvedores.

---

## 1. Visão Geral e Objetivos de Aprendizagem
Nesta aula inaugural, os participantes constroem a base conceitual e técnica indispensável para compreender a revolução dos agentes de inteligência artificial aplicados à administração pública universitária.

### Objetivos Específicos:
1. Diferenciar matematicamente e funcionalmente a predição de tokens em LLMs de mecanismos determinísticos de consulta a bancos de dados.
2. Identificar com precisão as fronteiras e casos de uso de: **Chatbot Paramétrico**, **Pipeline RAG** e **Agente Autônomo com Ferramentas**.
3. Analisar os quatro pilares da anatomia agêntica: Percepção, Raciocínio (ReAct/DAG), Ação (Function Calling) e Memória.
4. Mapear os riscos jurídicos e administrativos da alucinação de IA no setor público: perda de prazos decadenciais, nulidade de atos por vício de competência e responsabilização perante órgãos de controle (CGU/TCU).
5. Executar um laboratório prático comparativo demonstrando o colapso factual de uma resposta sem contexto frente ao rigor de um RAG normativo da UNIFEI.

---

## 2. Cronograma Minuto a Minuto

| Horário | Bloco | Atividade | Metodologia |
|:---:|:---:|---|---|
| **00:00 - 00:20** | 1.1 | Apresentação do curso, estudo de caso UNIFEI e nivelamento inicial | Exposição Dialogada |
| **00:20 - 01:00** | 1.2 | Da predição probabilística de tokens à tomada de ação com ferramentas | Teoria com visualização conceitual |
| **01:00 - 01:40** | 2.1 | Anatomia de um Agente: Ciclo ReAct, schemas JSON de tools e memória | Análise de código e diagramas |
| **01:40 - 02:00** | 2.2 | Estudo de caso: Como um agente interpreta um requerimento do SIPAC/SEI | Simulação de fluxo decisório |
| **02:00 - 02:40** | 3.1 | O Imperativo do RAG no Setor Público: Grounding, Revogação e Antinomias | Jurisprudência e hermenêutica de IA |
| **02:40 - 03:00** | 3.2 | Responsabilidade do servidor público e princípio da não-delegação do ato | Debate sobre ética e direito administrativo |
| **03:00 - 03:30** | 4.0 | **Laboratório Prático 1:** Execução do comparativo experimental e análise | Prática em terminal Python |

---

## 3. Desenvolvimento Teórico Aprofundado

### Bloco 1: Da Predição de Tokens à Tomada de Ação
Modelos de Linguagem de Grande Porte (LLMs) são redes neurais autorregressivas fundamentadas na arquitetura Transformer com mecanismo de autoatenção (*Scaled Dot-Product Attention*):
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Um LLM **não armazena fatos em tabelas**; ele codifica regularidades estatísticas da linguagem humana em matrizes de pesos sinápticos $\theta$. Ao receber uma pergunta como *"Qual o quórum para eleição de Diretor de Instituto na UNIFEI?"*, o modelo prevê a sequência mais verossímil de palavras:
$$P(w_t \mid w_{1}, w_{2}, \dots, w_{t-1}; \theta)$$

Se o modelo nunca teve contato com o Estatuto da UNIFEI atualizado, ele utilizará correlações de outras universidades (ex.: USP, UFRJ, UFMG), gerando uma resposta gramaticalmente impecável, porém juridicamente falsa e nula para a UNIFEI.

#### A Tríade da Automação Cognitiva:
1. **Chatbot Paramétrico (Zero-Shot):**
   * *Mecanismo:* $\text{Prompt} \rightarrow \text{LLM}(\theta) \rightarrow \text{Resposta}$.
   * *Risco:* Alucinação elevada, desatualização temporal, ausência total de citação válida.
2. **RAG (Retrieval-Augmented Generation):**
   * *Mecanismo:* $\text{Consulta} \rightarrow \text{Retriever}(\text{Base Vigente}) \rightarrow \text{LLM}(\text{Prompt} + \text{Contexto}) \rightarrow \text{Resposta Fundamentada}$.
   * *Vantagem:* Redução drástica de alucinação; toda afirmação aponta para um artigo e parágrafo verificável.
3. **Agente Autônomo com Ferramentas (Tool-Using Agent):**
   * *Mecanismo:* O LLM atua como motor de inferência que formula um plano, invoca APIs externas parametrizadas via JSON Schema, aguarda o retorno do sistema real e itera até completar a tarefa.

---

### Bloco 2: Anatomia de um Agente Cognitivo Institucional
Um agente seguro para universidades compõe-se de 4 subsistemas integrados:

1. **Percepção Multimodal:**
   * Capacidade de digerir textos estruturados (metadados do processo do SEI) e não estruturados (corpo de e-mails, despachos digitalizados).
2. **Raciocínio & Planejamento (Padrão ReAct):**
   * Inspirado no artigo clássico de Yao et al. (2022), o agente divide o trabalho em:
     * **Thought (Pensamento):** Avaliação do estado atual e identificação do que falta saber.
     * **Action (Ação):** Escolha de ferramenta e formatação de parâmetros.
     * **Observation (Observação):** Leitura da resposta retornada pela ferramenta.
3. **Ação e Ferramentas (Function Calling):**
   * O modelo não executa comandos arbitrários no sistema operacional. Ele gera um objeto JSON estrito correspondente a uma assinatura permitida.
4. **Memória de Curto e Longo Prazo:**
   * *Curto Prazo:* Janela de contexto com a trilha da conversa ativa.
   * *Longo Prazo:* Vetorização de precedentes do Conselho Universitário (CONSUNI) e histórico de pareceres.

---

### Bloco 3: O Imperativo do RAG no Domínio Público
No setor privado, uma resposta errônea de chatbot pode causar insatisfação comercial reversível. Na Administração Pública Federal, o rigor é ditado pelo **Princípio da Legalidade Estrita (Art. 37 da CF/88)**: a administração pública só pode agir onde e como a lei expressamente autoriza.

#### Riscos Concretos de Respostas não Ancoradas (Alucinações):
* **Perda de Prazos Decadenciais e Prescricionais:** Se a IA informar a um servidor que o prazo para recurso em concurso é de 10 dias quando a Resolução prevê 3 dias úteis, o servidor decai do direito de petição.
* **Nulidade de Atos Administrativos:** A motivação do ato administrativo é obrigatória (Lei 9.784/1999, Art. 50). Um despacho amparado em artigo inexistente ou revogado padece de vício insanável de motivação.
* **Imputação de Responsabilidade ao Agente Público:** O agente de IA não possui personalidade jurídica. O servidor que acolhe e assina a minuta gerada pela IA é pessoalmente responsável perante a Controladoria-Geral da União (CGU) e o Tribunal de Contas da União (TCU).

---

## 4. Guia de Discussão e Estudo de Caso em Sala
Promova um debate de 15 minutos com os alunos com base nas seguintes questões provocativas:
1. *"Se um agente de IA gerar um parecer citando uma resolução revogada da UNIFEI e o Reitor assinar sem ler, quem cometeu irregularidade administrativa?"*
   * *Gabarito pedagógico:* O Reitor (autoridade pública). A IA é meio instrumental; a fé pública e a competência de emissão de vontade estatal são indelegáveis a algoritmos.
2. *"Por que colocar todos os regulamentos da UNIFEI de uma vez no prompt do modelo não funciona tão bem quanto o RAG?"*
   * *Gabarito pedagógico:* Degradação de atenção em janelas de contexto extensas (*Lost in the Middle*), custo excessivo de processamento e impossibilidade de atualização em tempo real de atos normativos diários.

---

## 5. Roteiro do Laboratório Prático 1
Abra o terminal e execute o script de teste:
```bash
python dia_1/src/comparativo_rag.py
```
Peça aos participantes para inspecionarem o código e realizarem variações nas consultas.

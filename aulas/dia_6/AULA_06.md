# DIA 6: Governança, Avaliação, Implantação e Projeto Final

**Carga Horária:** 3h30 | **Nível:** Avançado  
**Estudo de Caso Institucional:** UNIFEI (Universidade Federal de Itajubá)

---

## 1. Visão Geral e Objetivos de Aprendizagem
Na sessão de encerramento do curso, consolidamos os marcos de conformidade legal com a **LGPD** e a **LAI**, detalhamos as diretrizes de governança e auditoria para controle externo (CGU/TCU), apresentamos a metodologia científica de avaliação com o **Framework RAGAS** e realizamos a **Banca de Apresentação e Avaliação dos Projetos Finais**.

### Objetivos Específicos:
1. Harmonizar as exigências de sigilo da LGPD com a obrigação de publicidade e transparência da LAI.
2. Formalizar o princípio da **Imputabilidade Humana** e a cadeia de custódia de decisões administrativas.
3. Aplicar as métricas de avaliação contínua do framework **RAGAS** (*Faithfulness*, *Answer Relevance*, *Context Precision*).
4. Estabelecer o plano de implantação progressiva (*Roadmap Institucional*) em 4 fases na UNIFEI.
5. Apresentar perante a banca o **Dossiê Consolidado do Projeto Final** (100 pontos).

---

## 2. Cronograma Minuto a Minuto

| Horário | Bloco | Atividade | Metodologia |
|:---:|:---:|---|---|
| **00:00 - 00:45** | 1.0 | Governança Pública: LGPD, LAI e Responsabilização Pessoal | Direito e Gestão Pública |
| **00:45 - 01:30** | 2.0 | Avaliação Sistemática: Framework RAGAS e Golden Datasets | Validação Científica |
| **01:30 - 02:00** | 3.0 | Roadmap de Implantação Institucional Segura em 4 Fases | Planejamento Estratégico |
| **02:00 - 03:30** | 4.0 | **Banca Avaliadora dos Projetos Finais (Apresentações)** | Avaliação Somativa dos Grupos |

---

## 3. Desenvolvimento Teórico Aprofundado

### Bloco 1: A Tríade da Governança Universitária
1. **LGPD (Lei nº 13.709/2018):**
   * Em processos disciplinares e de saúde discente, dados sensíveis transitam nos autos.
   * O pipeline do agente deve aplicar sanitização e mascaramento antes de enviar dados a modelos externos.
2. **LAI (Lei nº 12.527/2011):**
   * A regra geral na administração pública é a transparência ampla dos atos. As fontes normativas e critérios do agente devem ser acessíveis a qualquer cidadão via e-SIC.
3. **Imputabilidade e Fé Pública:**
   * O agente de IA opera como ferramenta de redação assistida (*co-piloto administrativo*). A validade jurídica do ato decorre exclusivamente da assinatura do agente público dotado de competência legal.

### Bloco 2: Avaliação Científica com Framework RAGAS
O framework RAGAS afere a qualidade de RAGs normativos através de três métricas essenciais:
* **Faithfulness (Fidelidade):** Toda asserção deve ser dedutível dos chunks recuperados (combate frontal à alucinação).
* **Answer Relevance (Relevância da Resposta):** O modelo respondeu exatamente o que foi indagado.
* **Context Precision & Recall:** O sistema recuperou todos os dispositivos normativos necessários sem ruídos irrelevantes.

---

## 4. Banca de Avaliação dos Projetos Finais (Rubrica 100 pts)

| Dimensão | Critérios Avaliados | Pontos |
|---|---|:---:|
| **1. Fidelidade Normativa** | Ancoragem estrita nas resoluções vigentes da UNIFEI; ausência de alucinação; recusa em casos omissos. | **30 pts** |
| **2. Arquitetura e Guardrails** | Roteamento multiagente adequado; ferramentas com privilégio de leitura/rascunho; ponto HITL explícito. | **25 pts** |
| **3. Modelagem de Dados** | JSON estruturado por artigo com metadados completos de vigência e histórico de revogação. | **15 pts** |
| **4. Viabilidade Administrativa** | Relevância do processo escolhido na rotina da UNIFEI e potencial de redução de retrabalho. | **15 pts** |
| **5. Governança e LGPD** | Mecanismos de sanitização de dados pessoais, transparência (LAI) e trilha de auditoria. | **15 pts** |
| **TOTAL** | | **100 pts** |

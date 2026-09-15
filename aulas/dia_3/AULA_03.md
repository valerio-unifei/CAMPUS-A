# DIA 3: Arquitetura de Agentes para o Setor Público

**Carga Horária:** 3h30 | **Nível:** Médio  
**Estudo de Caso Institucional:** UNIFEI (Universidade Federal de Itajubá)

---

## 1. Visão Geral e Objetivos de Aprendizagem
Nesta aula intermediária, os participantes aprendem a projetar sistemas de software agênticos robustos, escaláveis e seguros para universidades federais. O foco central é a substituição de arquiteturas monolíticas pelo padrão **Supervisor/Roteador + Subagentes de Domínio**, integrando ferramentas de consulta controlada e barreiras de guardrail institucionais.

### Objetivos Específicos:
1. Desenhar a arquitetura de um pipeline RAG com recuperação híbrida (densa + BM25) e re-ranking contextual.
2. Compreender a topologia *Router-Worker* para especialização de subagentes por pró-reitoria.
3. Projetar ferramentas (*tools*) seguras com privilégios restritos (Princípio do Menor Privilégio).
4. Implementar *guardrails* semânticos e sintáticos de competência decisória e detecção de lacunas legais.
5. Estruturar a **Entrega 2 do Projeto Final**: Diagrama completo de arquitetura do agente institucional.

---

## 2. Cronograma Minuto a Minuto

| Horário | Bloco | Atividade | Metodologia |
|:---:|:---:|---|---|
| **00:00 - 00:50** | 1.0 | RAG Híbrido: Densidade Semântica + Precisão Lexical (BM25) | Engenharia de Sistemas de Busca |
| **00:50 - 01:40** | 2.0 | Padrão Supervisor e Subagentes Especializados de Domínio | Modelagem Arquitetural de Software |
| **01:40 - 02:30** | 3.0 | Guardrails Ativos: Bloqueio de Improbidade e Usurpação Decisória | Segurança e Governança de IA |
| **02:30 - 03:00** | 4.1 | Simulação do orquestrador com interceptação de guardrails | Execução de Código Python |
| **03:00 - 03:30** | 4.2 | **Prática Guiada 3 (Entrega 2 do Projeto Final):** Modelagem Mermaid | Elaboração de Diagramas |

---

## 3. Desenvolvimento Teórico Aprofundado

### Bloco 1: Engenharia do RAG Híbrido Institucional
A recuperação de texto em normativos universitários apresenta um desafio específico: consultas combinam conceitos abstratos (*"como prorrogar minha permanência no mestrado?"*) com termos literais de artigos e siglas (*"Art. 15, § 2º da Resolução PRPPG nº 03/2023"*).

```
                        [CONSULTA DO SERVIDOR]
                                   │
                   ┌───────────────┴───────────────┐
                   ▼                               ▼
       [BUSCA DENSA / VETORIAL]         [BUSCA ESPARSA / BM25]
        Embedding semântico              Casamento exato de termos:
       - 'trancamento de curso'          - 'Art. 42'
       - 'interrupção de estudos'        - 'Resolução CEPE 05/2021'
                   │                               │
                   └───────────────┬───────────────┘
                                   ▼
                [FUSÃO HÍBRIDA POR RANKING (RRF)]
                                   │
                                   ▼
             [RE-RANKING VIA CROSS-ENCODER NEURAL]
       Avalia a pertinência profunda par a par (query, chunk)
                                   │
                                   ▼
                [TOP-K CHUNKS NORMAS VIGENTES UNIFEI]
```

### Bloco 2: Padrão Supervisor / Roteador Multiagente
Em vez de um único LLM sobrecarregado com dezenas de ferramentas heterogêneas, divide-se o sistema em módulos cognitivos:
1. **Supervisor / Roteador Central:**
   * Analisa a intenção e a jurisdição institucional da requisição.
   * Não responde diretamente ao usuário sobre regras específicas; delega ao subagente setorial.
2. **Subagentes Setoriais:**
   * *Subagente Acadêmico:* Especialista em resoluções do CEPE, normas de graduação e pós-graduação.
   * *Subagente de Gestão de Pessoas:* Especialista na Lei 8.112/90, planos de carreira docente (Lei 12.772/12) e resoluções da PROGEP.
   * *Subagente de Contratos & Patrimônio:* Especialista na Lei 14.133/21, termos de referência e editais da PROAD.

---

## 4. Laboratório Prático 3 e Entrega 2 do Projeto Final
1. Execute o roteador no terminal:
   ```bash
   python dia_3/src/orquestrador_roteador.py
   ```
2. Analise a interceptação preventiva do guardrail de competência.
3. **Entrega 2 do Projeto Final:** Preencha o arquivo `projeto_final_template/2_arquitetura_agente.md`.

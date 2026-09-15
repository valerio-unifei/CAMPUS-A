# DIA 5: Desenvolvimento Prático de um Agente Institucional

**Carga Horária:** 3h30 | **Nível:** Avançado  
**Estudo de Caso Institucional:** UNIFEI (Universidade Federal de Itajubá)

---

## 1. Visão Geral e Objetivos de Aprendizagem
Nesta aula de desenvolvimento prático avançado, os participantes integram todos os blocos conceituais e ferramentas construídas ao longo do curso em um protótipo funcional executável. O agente é dotado de RAG normativo estrito, ferramentas operacionais para apoio a conselhos universitários e barreiras programáticas de guardrail.

### Objetivos Específicos:
1. Implementar consultas RAG em Python com filtros relacionais de vigência ativa.
2. Criar a ferramenta de verificação matemática de **Quórum Regimental** (Maioria Simples vs. Maioria Absoluta no CONSUNI/CEPE).
3. Construir a ferramenta de **Geração de Minutas de Atas e Despachos** padronizadas com carimbo de salvaguarda.
4. Programar interceptadores de saída que bloqueiam o uso de linguagem deliberativa em primeira pessoa.
5. Executar a **Entrega 4 do Projeto Final**: Testar o protótipo contra uma bateria de 5 cenários normativos da UNIFEI.

---

## 2. Cronograma Minuto a Minuto

| Horário | Bloco | Atividade | Metodologia |
|:---:|:---:|---|---|
| **00:00 - 00:50** | 1.0 | Engenharia de Prompts Institucionais com Injeção de Contexto | Programação em Python |
| **00:50 - 01:40** | 2.0 | Implementação de Tools: Validador de Quórum e Minutador de Ata | Desenvolvimento Guiado |
| **01:40 - 02:30** | 3.0 | Codificação de Guardrails Sintáticos e Semânticos | Testes de Segurança |
| **02:30 - 03:00** | 4.1 | Execução do Agente Institucional Integrado | Testes de Carga Funcional |
| **03:00 - 03:30** | 4.2 | **Prática Guiada 5 (Entrega 4 do Projeto Final):** Bateria de 5 Casos | Validação em Equipe |

---

## 3. Desenvolvimento Teórico Aprofundado

### Bloco 1: Engenharia do Prompt Institucional
O *System Prompt* de um agente do setor público deve ser concebido como um **Manual de Procedimentos Administrativos**:
* **Definição de Identidade e Limites:** *"Você é o Agente Institucional de Apoio aos Colegiados da UNIFEI. Você auxilia secretários e relatores elaborando minutas e conferindo requisitos formais. Você NUNCA delibera, defere, indefere ou homologa."*
* **Instrução de Citação Obrigatória:** *"Toda conclusão deve explicitar o número do ato normativo, o ano, o órgão emissor e o artigo correspondente."*
* **Comportamento diante de Dúvidas ou Lacunas:** *"Se a pergunta não possuir resposta explícita nas resoluções vigentes fornecidas, declare expressamente: 'Matéria com aparente omissão regimental; recomenda-se submissão ao relator humano'."*

### Bloco 2: Ferramentas Operacionais para Secretarias de Conselho
1. **Validador de Quórum Deliberativo:**
   * O Art. 28 do Regimento Geral da UNIFEI determina:
     * Quórum de abertura de sessão: presença de mais da metade dos membros do conselho.
     * Quórum de aprovação ordinária: maioria simples dos presentes na sala.
     * Quórum de aprovação qualificada: maioria absoluta do total de membros do conselho para matérias orçamentárias e alterações regimentais.
   * O cálculo é puramente lógico e determinístico; delegar essa conta à probabilidade de tokens do LLM acarreta nulidade formal da votação. Portanto, **utiliza-se uma ferramenta determinística em código**.

2. **Gerador Estruturado de Minutas de Ata:**
   * Transforma notas desestruturadas tomadas durante a reunião em documento solene formatado com carimbo de rascunho: `[MINUTA PRELIMINAR - EXIGE APROVAÇÃO DO PLENÁRIO E ASSINATURA]`.

---

## 4. Laboratório Prático 5 e Entrega 4 do Projeto Final
1. Execute o protótipo:
   ```bash
   python dia_5/src/agente_institucional.py
   ```
2. Salve os testes e código no arquivo `projeto_final_template/4_especificacao_prototipo.py`.

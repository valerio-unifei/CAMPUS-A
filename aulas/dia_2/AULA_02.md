# DIA 2: Panorama Normativo e Mapeamento de Processos

**Carga Horária:** 3h30 | **Nível:** Básico  
**Estudo de Caso Institucional:** UNIFEI (Universidade Federal de Itajubá)

---

## 1. Visão Geral e Objetivos de Aprendizagem
Nesta aula, os alunos dominam a pirâmide de legalidade que rege uma Universidade Federal, mapeiam os fluxos decisórios da UNIFEI e constroem a **Matriz de Elegibilidade Agêntica**, separando com clareza atos administrativos automatizáveis daqueles que exigem deliberação puramente humana.

### Objetivos Específicos:
1. Compreender a hierarquia normativa: da Constituição Federal de 1988 até portarias setoriais da UNIFEI.
2. Identificar a competência privativa dos órgãos superiores (CONSUNI, CEPE, Reitoria, Pró-Reitorias e Colegiados).
3. Aplicar critérios técnicos e jurídicos para seleção de processos aptos à automação.
4. Identificar matérias vedadas para IA autônoma: juízo de mérito disciplinar, sanções éticas e interpretação de casos omissos.
5. Produzir o primeiro artefato do Projeto Final: a **Ficha de Mapeamento de Processos Administrativos da UNIFEI**.

---

## 2. Cronograma Minuto a Minuto

| Horário | Bloco | Atividade | Metodologia |
|:---:|:---:|---|---|
| **00:00 - 00:50** | 1.0 | Hierarquia das Leis Federais e Normativos da UNIFEI | Estudo Dogmático Aplicado |
| **00:50 - 01:40** | 2.0 | Organograma institucional: Onde os processos nascem, tramitam e morrem | Mapeamento Visual de Fluxos |
| **01:40 - 02:30** | 3.0 | Matriz de Elegibilidade: Volume, Repetitividade e Risco Jurídico | Estudo de Casos Reais UNIFEI |
| **02:30 - 03:00** | 4.1 | Simulação com o classificador automatizado em Python | Execução de Código |
| **03:00 - 03:30** | 4.2 | **Prática Guiada 2 (Entrega 1 do Projeto Final):** Preenchimento da ficha | Trabalho em Equipe |

---

## 3. Desenvolvimento Teórico Aprofundado

### Bloco 1: Pirâmide Normativa Aplicada às IFES
A conformidade de qualquer sistema de IA institucional subordina-se à hierarquia formal das fontes do Direito:

```
[1] CONSTITUIÇÃO FEDERAL DE 1988
    └─ Art. 207: Autonomia didático-científica, administrativa e de gestão financeira.
    └─ Art. 37: Princípios da Legalidade, Impessoalidade, Moralidade, Publicidade e Eficiência.

[2] LEIS FEDERAIS GERAIS E ESPECÍFICAS
    ├─ Lei nº 9.394/1996 (LDB): Diretrizes e Bases da Educação Nacional.
    ├─ Lei nº 8.112/1990: Regime Jurídico Único dos Servidores Públicos Civis da União.
    ├─ Lei nº 9.784/1999: Processo Administrativo no âmbito da Administração Pública Federal.
    ├─ Lei nº 12.527/2011 (LAI): Acesso à Informação e Transparência Pública.
    ├─ Lei nº 13.709/2018 (LGPD): Proteção de Dados Pessoais de discentes e servidores.
    └─ Lei nº 14.133/2021: Nova Lei de Licitações e Contratos Administrativos.

[3] NORMAS INTERNAS FUNDAMENTAIS DA UNIFEI
    ├─ Estatuto da UNIFEI: Estrutura fundacional aprovada pelo MEC.
    └─ Regimento Geral da UNIFEI: Operacionalização das diretrizes estatutárias.

[4] NORMAS REGULAMENTADORAS COLEGIADAS
    ├─ Resoluções do CONSUNI: Diretrizes institucionais, políticas orçamentárias e criação de cursos.
    ├─ Resoluções do CEPE: Regimes de graduação, pós-graduação, pesquisa e extensão.
    └─ Resoluções do CURAD: Gestão administrativa e orçamentária.

[5] ATOS EXECUTIVOS DERIVADOS
    ├─ Portarias da Reitoria e Pró-Reitorias (PRG, PRPPG, PROAD, PROGEP).
    └─ Instruções Normativas (INs) e Ordens de Serviço das Secretarias.
```

---

### Bloco 2: Órgãos e Competências no Estudo de Caso UNIFEI
* **CONSUNI (Conselho Universitário):** Órgão colegiado normativo e deliberativo superior. Responsável por emendas estatutárias, aprovação do PDI (Plano de Desenvolvimento Institucional) e julgamento final de recursos.
* **CEPE (Conselho de Ensino, Pesquisa e Extensão):** Fixa as diretrizes didático-pedagógicas, normas de matrícula, trancamento, jubilamento, convalidação de títulos e aprova o calendário acadêmico anual.
* **Pró-Reitorias:**
  * **PRG (Graduação):** Aplicação das diretrizes curriculares e supervisão dos registros discentes.
  * **PRPPG (Pós-Graduação e Pesquisa):** Gestão de programas stricto e lato sensu e fomento científico.
  * **PROGEP (Gestão de Pessoas):** Concessão de progressões docentes e de técnicos, licenças e aposentadorias.
  * **PROAD (Administração):** Licitações, compras, patrimônio e contratos contínuos.
* **Colegiados de Curso de Graduação:** Análise de aproveitamento de disciplinas, adaptação curricular e pedidos de prorrogação de prazo para conclusão de curso.

---

### Bloco 3: Matriz de Elegibilidade Agente-Processo
Como selecionar onde aplicar agentes de IA na universidade de forma ética e eficiente:

```
                  Alto ▲
                       │   [QUADRANTE 2]              [QUADRANTE 1]
                       │   Supervisão Crítica         Automação Prioritária
                       │   - Recursos Acadêmicos      - Triagem Formal de Processos
        IMPACTO        │   - Análise de Laudos        - Checagem de Quórum
        E RISCO        │   - Progressão Docente       - Despachos de Mero Expediente
       JURÍDICO        │   -------------------------------------------------
                       │   [QUADRANTE 4]              [QUADRANTE 3]
                       │   Inviável / Proibido        Automação Simples
                       │   - Julgamento Ético / PAD   - Envio de Alertas de Prazo
                       │   - Casos Omissos do CEPE    - Emissão de Declarações
                  Baixo └─────────────────────────────────────────────────────►
                        Baixo                  VOLUME E REPETIÇÃO            Alto
```

---

## 4. Laboratório Prático 2 e Entrega 1 do Projeto Final
1. Execute o classificador de processos:
   ```bash
   python dia_2/src/mapeador_processos.py
   ```
2. Analise a saída gerada em `dia_2/exemplos/processos_mapeados.json`.
3. **Entrega 1 do Projeto Final:** Cada equipe preenche o arquivo `projeto_final_template/1_escopo_processos.md`.

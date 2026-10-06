# PLANO UNIFICADO DE AUTOMAÇÃO E TRANSFORMAÇÃO DIGITAL COM INTELIGÊNCIA ARTIFICIAL

## Universidade Federal de Itajubá (UNIFEI)

---

### 1. Reitoria e Conselhos Superiores (CONSUNI, CEPE e Câmaras)

* **Elaboração e Verificação de Minutas Normativas:**
* *Ferramenta:* Google Gemini Notebook (NotebookLM).
* *Aplicação:* Análise de conformidade de novas propostas de resolução frente ao Estatuto, Regimento Geral e resoluções vigentes da UNIFEI.


* **Síntese de Reuniões e Minutas de Atas:**
* *Ferramenta:* Google Meet (Transcrição) + Gemini / Gems.
* *Aplicação:* Transcrição automática de sessões deliberativas convertida em minutas de atas e extratos de deliberação para a Secretaria dos Conselhos.


* **Gestão e Triagem de Pautas da Reitoria:**
* *Ferramenta:* Google Agenda + Google Workspace Studio / Apps Script.
* *Aplicação:* Formulário de triagem prévia para agendamento automático de audiências no Gabinete do Reitor.


* **Convocação e Montagem de Pauta Agendada:**
* *Ferramenta:* Gemini Scheduler (Disparador Temporal).
* *Aplicação:* Execução automática 7 dias antes das sessões ordinárias para varredura de processos no SEI/Drive, criação de apresentação executiva e envio de convocações com pauta aos conselheiros.


* **Monitoramento de Fim de Mandatos de Conselheiros:**
* *Ferramenta:* Gemini Scheduler.
* *Aplicação:* Varredura mensal para identificar mandatos a expirar em 60 dias, redigindo minutas de editais de eleição/recondução.



---

### 2. Pró-Reitoria de Graduação (PRG)

* **Equivalência e Aproveitamento de Disciplinas:**
* *Ferramenta:* Gemini Notebook + Gem Customizado ("Gem PRG-Equivalências").
* *Aplicação:* Cruzamento automatizado entre planos de ensino externos e o Projeto Pedagógico de Curso (PPC) da UNIFEI para emissão de parecer prévio de correspondência.


* **Atendimento a Dúvidas e Regulamento Acadêmico:**
* *Ferramenta:* Gem (Atendente Virtual) + Google Chat / Gmail.
* *Aplicação:* Atendente virtual treinado no Regulamento dos Cursos de Graduação para sanar dúvidas sobre trancamentos, regime domiciliado e coeficiente de rendimento.


* **Agendamento de Atendimentos Acadêmicos:**
* *Ferramenta:* Páginas de Agendamento do Google Agenda.
* *Aplicação:* Organização de horários de atendimento discente por blocos nas secretarias de curso.


* **Alertas Situacionais do Calendário Acadêmico:**
* *Ferramenta:* Gemini Scheduler.
* *Aplicação:* Notificações automáticas a docentes sobre prazos de diários de classe e alertas a discentes sobre datas críticas de trancamento.


* **Processamento Noturno em Lote de Formandos:**
* *Ferramenta:* Gemini Spark / Batch Processing.
* *Aplicação:* Verificação automatizada dos históricos escolares no período de colação de grau para emissão da lista de formandos aptos.



---

### 3. Pró-Reitoria de Pesquisa e Pós-Graduação (PRPPG)

* **Validação Formal de Editais PIBIC/PIBITI:**
* *Ferramenta:* Google Forms + Sheets + Apps Script + Gemini.
* *Aplicação:* Triagem de pré-requisitos formais de propostas (Lattes atualizado, formatação, anexos) antes da distribuição aos pareceristas *ad hoc*.


* **Acompanhamento de Prazos de Qualificação e Defesa:**
* *Ferramenta:* NotebookLM + Google Calendar.
* *Aplicação:* Análise de atas de pós-graduação para identificar prazos regulamentares críticos e alertar orientadores e discentes.


* **Agendador Inteligente de Bancas de Defesa:**
* *Ferramenta:* Gemini Scheduler + Google Calendar / Meet.
* *Aplicação:* Identificação de horários convergentes entre membros da banca, geração do link do Google Meet e envio automático do resumo executivo da dissertação.


* **Cobrança e Análise de Relatórios de Iniciação Científica:**
* *Ferramenta:* Gemini Scheduler + Google Forms.
* *Aplicação:* Cobrança periódica automatizada e pré-análise do cumprimento de metas nos relatórios de bolsistas de Iniciação Científica.



---

### 4. Pró-Reitoria de Extensão (PROEX)

* **Análise e Consolidação de Relatórios de Extensão:**
* *Ferramenta:* Gemini Notebook (NotebookLM).
* *Aplicação:* Leitura dos relatórios finais de projetos para compilar indicadores de público atendido, impacto social e convergência com os ODS da ONU.


* **Emissão Automatizada de Certificados:**
* *Ferramenta:* Google Forms + Sheets + Apps Script.
* *Aplicação:* Geração e disparo automático de certificados de eventos com registro de autenticidade.



---

### 5. Pró-Reitoria de Gestão de Pessoas (PRGP)

* **Instrução de Processos de Progressão e Promoção:**
* *Ferramenta:* Gemini Notebook + Gem Customizado ("Analista de Progressão PRGP").
* *Aplicação:* Leitura de comprovantes e tabelas de pontuação do SEI/SIPAC, gerando minuta de parecer instrutório confrontado com as resoluções da UNIFEI.


* **Tira-Dúvidas e Atendimento ao Servidor:**
* *Ferramenta:* Gem Customizado (FAQ RH).
* *Aplicação:* Atendimento automatizado sobre direitos, deveres, licenças, auxílios e previdência via e-mail e Google Chat.


* **Agendamento de Perícias Médicas:**
* *Ferramenta:* Páginas de Agendamento do Google Agenda.
* *Aplicação:* Gestão de horários da Junta Médica e conferência de documentação de posse.


* **Workflow de Avaliação do Estágio Probatório:**
* *Ferramenta:* Gemini Scheduler.
* *Aplicação:* Agendamento automático das reuniões aos 6, 12, 18 e 24 meses de exercício, com formulários pré-preenchidos.


* **Auditoria Contínua de Acumulação de Cargos:**
* *Ferramenta:* Gemini Spark.
* *Aplicação:* Varredura quadrimestral cruzando declarações de acúmulo de cargos e quadros de horários de aulas e projetos.



---

### 6. Pró-Reitoria de Administração (PRAD) e Infraestrutura

* **Análise de Conformidade de Termos de Referência (TRs):**
* *Ferramenta:* Gemini Notebook (NotebookLM).
* *Aplicação:* Verificação de TRs e editais em relação à Lei nº 14.133/2021, guias da AGU e acórdãos do TCU antes da fase externa da licitação.


* **Triagem de Chamados de Manutenção Predial:**
* *Ferramenta:* Google Forms + Sheets + Gemini em Sheets.
* *Aplicação:* Classificação por nível de urgência/risco dos pedidos de reparo e encaminhamento à Prefeitura Universitária.


* **Painel Executivo de Vencimento de Contratos e ARPs:**
* *Ferramenta:* Gemini Scheduler.
* *Aplicação:* Alertas automatizados a 180 dias (pesquisa de vantajosidade de renovação) e a 90 dias (início de nova licitação).


* **Gestão Preventiva de Espaços do Campus:**
* *Ferramenta:* Gemini Spark.
* *Aplicação:* Monitoramento do uso acumulado de auditórios/laboratórios no Google Calendar para disparo automático de ordens de manutenção e limpeza.



---

### Princípios de Governança e Compliance

1. **Human-in-the-Loop:** A IA atua na produção de **minutas, triagens e análises prévias**. A decisão administrativa final e a assinatura do ato permanecem sob responsabilidade do servidor público competente.
2. **Privacidade e LGPD:** Execução restrita ao ambiente corporativo **Google Workspace for Education** da UNIFEI, resguardando os dados conforme a Lei nº 13.709/2018.
3. **Auditabilidade e Eficiência:** Redução da burocracia, celeridade na prestação dos serviços públicos e facilidade na prestação de contas aos órgãos de controle (CGU, TCU e MEC).

---


# PLANO DE CAPACITAÇÃO E GESTÃO DE MUDANÇA (PGM-IA) — UNIFEI

## 1. Estrutura Metodológica de Gestão de Mudança (Modelo ADKAR)

```
 [1. AWARENESS] ──► [2. DESIRE] ──► [3. KNOWLEDGE] ──► [4. ABILITY] ──► [5. REINFORCEMENT]
 Conscientização     Engajamento      Capacitação       Aplicação         Consolidação

```

### **Fase 1: Conscientização (*Awareness*) — "Por que transformar?"**

* **Objetivo:** Eliminar o receio do desconhecido e alinhar expectativas sobre o papel da IA no serviço público.
* **Ações:**
* **Seminário de Abertura:** *"IA na Gestão Pública e no Ensino Superior: Eficiência com Responsabilidade"*, liderado pela Reitoria e convidados especialistas em Direito Administrativo e Tecnologia.
* **Campanha de Comunicação Interna:** Divulgação de vídeos curtos e infográficos sobre a diferença entre uso pessoal de IA e o uso no ambiente corporativo e seguro `@unifei.edu.br`.
* **Clarificação de Mitos:** Enfatizar que a IA não substitui o servidor, mas automatiza tarefas repetitivas de baixa complexidade cognitiva, valorizando o julgamento humano.



### **Fase 2: Engajamento (*Desire*) — "O que ganho com isso?"**

* **Objetivo:** Criar motivação voluntária e identificar lideranças facilitadoras.
* **Ações:**
* **Rede de Embaixadores Digitais:** Seleção de 2 a 3 servidores por Pró-Reitoria, Instituto e Campus de Itabira para atuarem como *multiplicadores institucionais*.
* **Apresentação de Casos Reais (Quick Wins):** Demonstração ao vivo de rotinas antes/depois (ex.: análise de conformidade de Termo de Referência reduzida de 3 dias para 20 minutos de pré-análise).
* **Diálogo Aberto com Sindicatos e Representações:** Reuniões explicativas para garantir transparência quanto aos impactos na rotina de trabalho.



### **Fase 3: Capacitação (*Knowledge*) — "Como utilizar?"**

* **Objetivo:** Desenvolver competências teóricas e técnicas sobre a suíte Google Workspace + Gemini.
* **Ações:**
* Lançamento das **Trilhas Específicas de Aprendizagem** (detalhadas na Seção 2).
* Formato híbrido: módulos assíncronos no Google Classroom + oficinas síncronas práticas pelo Google Meet.



### Fase 4: Habilidade e Prática (*Ability*) — "Consigo fazer na minha rotina!"

* **Objetivo:** Transformar o conhecimento teórico em autonomia no dia a dia do trabalho.
* **Ações:**
* **Ambiente Sandbox Seguro:** Criação de pastas e drives de teste para treinamento sem risco de alteração de documentos oficiais do SEI ou SIPAC.
* **Hackathon de Processos Públicos da UNIFEI:** Competição interna entre equipes para criação dos melhores *Gems* e fluxos do *Apps Script/Gemini Spark* para problemas reais da universidade.
* **Ateliês de Engenharia de Prompts:** Oficinas de elaboração de prompts instrucionais e técnicos para minutas administrativas, ementas e editais.



### **Fase 5: Consolidação e Reforço (*Reinforcement*) — "A nova cultura da UNIFEI"**

* **Objetivo:** Sustentar os ganhos de produtividade e garantir a melhoria contínua.
* **Ações:**
* **Certificação e Progressão por Capacitação:** Validação das horas do plano junto à PRGP para fins de progressão funcional.
* **Premiação "Inovação Gestão UNIFEI":** Reconhecimento anual dos melhores projetos de automação criados por servidores.
* **Dashboard de Adoção:** Monitoramento contínuo do volume de pesquisas, documentos analisados e e-mails otimizados via ecossistema Google.



---

## 2. Trilhas de Capacitação por Segmento (Matriz Curricular)

### **Trilha A: Gestores e Lideranças (Reitoria, Pró-Reitores, Diretores e Coordenadores)**

* **Carga Horária:** 12 horas
* **Foco:** Governança, Tomada de Decisão, Segurança de Dados e Liderança Digital.
* **Módulos:**
1. *Estratégia e Inteligência Artificial no Setor Público Federal.*
2. *Governança de Dados, LGPD e Diretrizes de Supervisão Humana (Human-in-the-Loop).*
3. *Uso do Gemini no Google Meet e Docs para Síntese Executiva de Reuniões e Decisões.*
4. *Gestão de Indicadores e Análise de Tendências em Planilhas com IA.*



### **Trilha B: Servidores Técnicos-Administrativos (TAEs das Pró-Reitorias e Secretarias)**

* **Carga Horária:** 30 horas
* **Foco:** Automação de Processos, Instrução Processual, Atendimento e Redação Oficial.
* **Módulos:**
1. *Letramento Digital em IA Generativa Corporativa (Google Workspace).*
2. *Engenharia de Prompts para Redação e Revisão Oficial (Padrão Presidência da República).*
3. *Análise Documental com NotebookLM (Leitura de TRs, Legislação, Portarias e Regulamentos).*
4. *Criação de Gems Personalizados para Atendimento e Triagem de Demandas.*
5. *Automação de Fluxos de Trabalho com Google Forms, Apps Script e Disparadores (Spark/Scheduler).*



### **Trilha C: Docentes e Pesquisadores**

* **Carga Horária:** 20 horas
* **Foco:** Produtividade Acadêmica, Metodologias de Ensino e Apoio à Pesquisa.
* **Módulos:**
1. *Inteligência Artificial na Educação Superior: Desafios Pedagógicos e Integridade Acadêmica.*
2. *Elaboração de Material Didático e Planos de Aula com Gemini e Google Apresentações.*
3. *Análise Massiva de Artigos Científicos e Literatura com NotebookLM.*
4. *Gestão de Grupos de Pesquisa e Projetos de Extensão via Google Workspace com IA.*



---

## 3. Diretrizes de Governança, Ética e LGPD

1. **Princípio do *Human-in-the-Loop*:** Nenhuma decisão administrativa que afete direitos de alunos ou servidores pode ser totalmente automatizada. A IA atua na elaboração de minutas e análises prévias; o parecer final e a assinatura são indelegáveis ao agente público.
2. **Confidencialidade no Domínio Institucional:** Os treinamentos enfatizarão que todo trabalho deve ser executado exclusivamente em contas `@unifei.edu.br`. Dados institucionais processados no plano corporativo Google Workspace Educação não são utilizados para treinamento de modelos públicos da Google.
3. **Auditabilidade:** As minutas geradas com auxílio de IA devem registrar a fonte de fundamentação consultada (como nos repositórios do NotebookLM).

---

## 4. Indicadores Chave de Desempenho (KPIs do Plano)

* **Taxa de Adesão:** Porcentagem de servidores e docentes que concluíram ao menos uma trilha (Meta: $\ge 75\%$ em 12 meses).
* **Ganho de Eficiência:** Redução média no tempo de instrução de processos padronizados (Meta: $\ge 40\%$ nos processos mapeados).
* **Rede de Multiplicadores:** Mínimo de 30 Embaixadores Digitais capacitados até o Mês 3.
* **NPS da Capacitação:** Índice de satisfação dos participantes com os treinamentos (Meta: $\ge 85\%$).

---

# PROGRAMA DETALHADO DE CAPACITAÇÃO — TRILHA B (TAEs UNIFEI)

**Carga Horária Total:** 30 horas (5 Módulos de 6h: 2h de aula síncrona/expositiva-prática no Google Meet + 4h de laboratório/aplicação prática supervisionada no ambiente *Sandbox* da UNIFEI).

---

### MÓDULO 1: Letramento Digital, Segurança e Ética em IA no Setor Público

* **Carga Horária:** 6 horas (2h Síncronas + 4h Práticas)
* **Objetivos de Aprendizagem:**
* Compreender os princípios de funcionamento das IAs generativas no Google Workspace corporativo (`@unifei.edu.br`).
* Aplicar as diretrizes de privacidade da LGPD (Lei nº 13.709/2018) e as orientações da CGU/MGI para uso responsável da IA.
* Executar a verificação humana (*Human-in-the-Loop*) e identificar alucinações e vieses em textos automatizados.



#### **Plano da Aula Síncrona (2 horas):**

1. **00h00 - 00h45:** *IA na Administração Pública Federal:* Limites legais, segurança da informação e a diferença entre o ambiente aberto do Gemini e o ambiente corporativo protegido do Google Workspace Education da UNIFEI.
2. **00h45 - 01h30:** *Prática Guiada:* Apresentação do painel do Gemini integrado ao Gmail e Drive. Leitura e aplicação do Checklist de Validação Humana em minutas geradas por IA.
3. **01h30 - 02h00:** *Análise de Riscos:* Estudo de casos reais de alucinações de dados e vazamento de informações sigilosas.

#### **Exercício Prático Assíncrono (4 horas — Sandbox UNIFEI):**

* **Cenário Real:** O setor do servidor recebe uma solicitação via e-mail/Ouvidoria com uma longa sequência de e-mails truncados e com divergências de prazos.
* **Tarefa:**
1. Utilizar o Gemini no Gmail corporativo para sumarizar a cadeia de e-mails em um resumo estruturado de 5 linhas.
2. Gerar uma minuta de resposta ao cidadão/servidor com linguagem clara e formal.
3. Preencher o **Formulário de Auditoria Humana**, apontando se houve alguma inconsistência de datas ou fatos no texto sugerido pela IA e efetuando as correções necessárias.


* **Entregável do Módulo:** Registro do prompt utilizado, texto bruto gerado pela IA e versão final revisada e assinada pelo servidor com o formulário de auditoria.

---

### MÓDULO 2: Engenharia de Prompts e Redação Oficial (Padrão Presidência da República)

* **Carga Horária:** 6 horas (2h Síncronas + 4h Práticas)
* **Objetivos de Aprendizagem:**
* Dominar a metodologia de construção de prompts **C-R-T-F (Contexto, Role/Papel, Task/Tarefa, Format/Restrições)**.
* Utilizar o Gemini no Google Docs para elaborar e revisar Ofícios, Memorandos, Portarias e Pareceres em conformidade com o Manual de Redação da Presidência da República.



#### **Plano da Aula Síncrona (2 horas):**

1. **00h00 - 00h45:** *Metodologia C-R-T-F:* Como estruturar comandos precisos que eliminam ambiguidades e garantem o tom formal e impessoal do serviço público.
2. **00h45 - 01h30:** *Oficina de Redação em Tempo Real:* Construção colaborativa de um parecer instrutório no Google Docs usando comandos diretos do Gemini.
3. **01h30 - 02h00:** *Tira-Dúvidas e Calibração de Estilo:* Ajustes de tom para despachos decisórios no SEI.

#### **Exercício Prático Assíncrono (4 horas — Sandbox UNIFEI):**

* **Cenário Real:** Instrução de um recurso administrativo encaminhado à PRGP ou PRG solicitando revisão de decisão administrativa.
* **Tarefa:**
1. Elaborar um prompt estruturado no padrão C-R-T-F contendo o resumo do pedido e a fundamentação legal aplicável.
2. Gerar no Google Docs a minuta de um **Ofício de Resposta ao Recurso**, contendo: Endereçamento, Ementa, Fundamentação Técnica, Conclusão e Fecho Oficial.
3. Solicitar ao Gemini no Docs que elabore um resumo executivo de 3 linhas do parecer para inclusão na folha de rosto do processo no SEI.


* **Entregável do Módulo:** Link do documento no Google Docs com histórico de alterações e a Ficha Técnica da Engenharia do Prompt.

---

### MÓDULO 3: Análise Documental e Compliance Normativo com NotebookLM

* **Carga Horária:** 6 horas (2h Síncronas + 4h Práticas)
* **Objetivos de Aprendizagem:**
* Criar mesas de trabalho e bases de conhecimento isoladas e seguras no NotebookLM.
* Carregar legislações federais, resoluções internas da UNIFEI e editais para verificação rápida de conformidade.
* Gerar Notas Técnicas e pareceres fundamentados com citação direta de fontes originais.



#### **Plano da Aula Síncrona (2 horas):**

1. **00h00 - 00h45:** *Arquitetura do NotebookLM:* Como funciona a ancoragem de dados (*Grounding*) e por que o NotebookLM não "inventa" informações fora dos arquivos carregados.
2. **00h45 - 01h30:** *Demonstração ao Vivo:* Análise de um Termo de Referência (TR) da PRAD confrontado com a Nova Lei de Licitações (Lei nº 14.133/2021) e o Regimento da UNIFEI.
3. **01h30 - 02h00:** *Estratégia de Perguntas de Auditoria:* Como formular perguntas para encontrar lacunas, cláusulas abusivas ou contradições regulamentares.

#### **Exercício Prático Assíncrono (4 horas — Sandbox UNIFEI):**

* **Cenário Real (Escolha da Unidade de Origem do Servidor):**
* *Opção A (PRAD/Licitações):* Carregar no NotebookLM a Lei nº 14.133/2021 + Guia da AGU + Minuta de TR submetida ao setor.
* *Opção B (PRG/Graduação):* Carregar o Regulamento de Cursos de Graduação da UNIFEI + Pedido de Equivalência/Aproveitamento extemporâneo de discente.
* *Opção C (PRGP/Gestão de Pessoas):* Carregar as Resoluções de Progressão Funcional + Comprovantes apresentados pelo servidor.


* **Tarefa:**
1. Submeter no mínimo 5 perguntas de conformidade à base no NotebookLM.
2. Gerar um **Relatório de Instrução Processual / Nota Técnica** com o diagnóstico de conformidade do processo.
3. Garantir que todas as afirmações da Nota Técnica contenham as devidas notas de citação do documento fonte geradas pelo NotebookLM.


* **Entregável do Módulo:** Relatório de instrução processual exportado em PDF/Doc com o mapeamento de conformidade e referências citadas.

---

### MÓDULO 4: Assistentes Personalizados (Gems) para Triagem e Atendimento Setorial

* **Carga Horária:** 6 horas (2h Síncronas + 4h Práticas)
* **Objetivos de Aprendizagem:**
* Desenvolver assistentes virtuais especializados (*Gems*) para padronizar rotinas e fluxos do setor.
* Escrever Instruções do Sistema (*System Prompts*) duráveis e configuradas com regras de negócio da UNIFEI.
* Calibrar e testar Gems para atendimento no balcão/e-mail e pré-triagem de requerimentos.



#### **Plano da Aula Síncrona (2 horas):**

1. **00h00 - 00h45:** *Anatomia de um Gem Institucional:* Definição de papel, regras de negação ("O que o Gem NÃO pode fazer"), diretrizes de estilo e etapas de raciocínio.
2. **00h45 - 01h30:** *Construção ao Vivo:* Criação do "Gem Triador de Editais de Extensão (PROEX)".
3. **01h30 - 02h00:** *Bateria de Testes e Ajustes:* Como testar cenários de limite para evitar que o Gem preste informações equivocadas sobre normas da universidade.

#### **Exercício Prático Assíncrono (4 horas — Sandbox UNIFEI):**

* **Cenário Real:** O setor administrativo gasta horas semanais respondendo às mesmas dúvidas sobre procedimentos, formulários e prazos.
* **Tarefa:**
1. Mapear uma rotina repetitiva do seu setor (ex.: *Gems de Dúvidas sobre Auxílio-Saúde na PRGP*, *Gem de Normas de TCC na PRG*, *Gem de Tramitação de Compras na PRAD*).
2. Escrever a Instrução do Sistema do Gem no ambiente de criação do Google Workspace.
3. Executar uma bateria de 3 testes (Cenário Básico, Cenário Intermediário com exceção de regra, e Cenário Complexo/Negativo).
4. Compartilhar o Gem com a equipe do seu setor na Sandbox.


* **Entregável do Módulo:** Link de acesso ao Gem criado, texto completo da Instrução do Sistema e relatório contendo as 3 conversas de teste realizadas.

---

### MÓDULO 5: Automação de Workflows com Google Forms, Sheets e Disparadores (Spark e Scheduler)

* **Carga Horária:** 6 horas (2h Síncronas + 4h Práticas)
* **Objetivos de Aprendizagem:**
* Conectar Google Forms, Sheets, Agenda e Gmail para automação de processos sem necessidade de programação complexa (*Low-Code/No-Code*).
* Configurar respostas automatizadas orientadas por eventos (*Gemini Spark*) ao entrar novos dados no sistema.
* Implementar rotinas temporalmente agendadas (*Gemini Scheduler*) para monitoramento de prazos legais e regulamentares da UNIFEI.



#### **Plano da Aula Síncrona (2 horas):**

1. **00h00 - 00h45:** *Arquitetura de Automação de Workflows:* Como transformar um processo baseado em papel/e-mail solto em um fluxo digital contínuo no Google Workspace.
2. **00h45 - 01h30:** *Construção de Fluxo ao Vivo:* Criando um sistema automatizado de solicitação de manutenção predial com classificação automática de risco no Sheets via Gemini e envio de alerta para a equipe técnica.
3. **01h30 - 02h00:** *Configuração do Gemini Scheduler:* Como agendar alertas automatizados de vencimento de prazos no Google Agenda e Gmail.

#### **Exercício Prático Assíncrono (4 horas — Sandbox UNIFEI):**

* **Cenário Real:** Necessidade de automatizar a recepção, classificação e acompanhamento de prazos de uma demanda do setor.
* **Tarefa:**
1. Criar um **Google Form** para entrada de solicitações do público interno/externo.
2. Vincular a um **Google Sheets** onde a funcionalidade do Gemini no Sheets faz a classificação automática de prioridade/tipo de pedido.
3. Configurar um disparador por evento (**Spark**) que envia a minuta da confirmação ao requerente e a notificação ao servidor responsável.
4. Configurar uma rotina temporal (**Scheduler**) no Google Calendar que agenda a data limite de resposta conforme a SLA do setor.


* **Entregável do Módulo:** Diagrama visual do fluxo de trabalho e links do Formulário e da Planilha automatizada funcionando no ambiente Sandbox.

---

### Tabela Consolidada dos Entregáveis da Trilha B

| Módulo | Carga Horária | Tópico Central | Produto Prático Entregue pelo Servidor |
| --- | --- | --- | --- |
| **Mód 1** | 6h (2h S/4h A) | Letramento e LGPD | Resumo e resposta de e-mail com Ficha de Auditoria Humana assinada |
| **Mód 2** | 6h (2h S/4h A) | Redação Oficial em Docs | Minuta de Ofício/Parecer em Google Docs + Ficha de Prompt C-R-T-F |
| **Mód 3** | 6h (2h S/4h A) | Análise com NotebookLM | Nota Técnica de Conformidade com citações diretas das normas fontes |
| **Mód 4** | 6h (2h S/4h A) | Gems Especialistas | Gem do setor funcional publicado na Sandbox + Relatório de Testes |
| **Mód 5** | 6h (2h S/4h A) | Automação e Spark/Scheduler | Fluxo completo Form + Sheet + Gemini + Agenda/Email + Diagrama |

---
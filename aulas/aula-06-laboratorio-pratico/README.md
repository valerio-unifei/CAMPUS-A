# Aula 6 — Laboratório Prático de Aplicação

**Duração:** 3h30min (210 minutos)  
**Pré-requisitos:** participação nas aulas anteriores ou domínio dos resultados de aprendizagem.

## Objetivo

Em equipes, conceber e demonstrar uma solução de apoio a uma tarefa administrativa de baixo risco, usando dados sintéticos. O produto é um protótipo pedagógico; não deve ser conectado a sistemas institucionais nem usado em produção sem as aprovações, testes e controles adequados.

## Resultados de aprendizagem

- formular problema, público, finalidade e limites da solução;
- escolher ferramenta com justificativa (Gemini/Gem, NotebookLM, Workspace Studio ou AI Studio);
- produzir um artefato demonstrável e verificável;
- identificar riscos, falhas, tratamento de exceções e pontos de revisão humana;
- apresentar próximos passos para validação institucional.

## Preparação do instrutor

- Recolher previamente problemas de processo em nível geral, sem nomes, números de processo, capturas de tela ou documentos internos.
- Disponibilizar um conjunto de dados sintéticos e documentos públicos autorizados.
- Preparar uma alternativa offline (fluxograma, prompt e protótipo desenhado) caso o acesso a ferramentas esteja indisponível.
- Confirmar antecipadamente acesso e regras das contas. Não configurar integrações, publicação ou envio real durante o laboratório.

## Roteiro (210 minutos)

| Tempo | Etapa | Condução |
|---|---|---|
| 0–15 min | Briefing e regras | Apresentar entregáveis, critérios e limites de uso de dados. Formar equipes. |
| 15–35 min | Escolha do problema | Especificar usuário, tarefa, dificuldade atual e resultado esperado em linguagem observável. |
| 35–55 min | Seleção da ferramenta e desenho | Escolher ferramenta, justificar adequação e desenhar entradas, etapas, saídas e controle humano. |
| 55–65 min | Intervalo |  |
| 65–125 min | Construção do artefato | Produzir prompt/Gem, caderno de fontes, mapa de fluxo no Workspace Studio ou protótipo no AI Studio. Usar apenas material sintético/público autorizado. |
| 125–135 min | Intervalo |  |
| 135–165 min | Testes e revisão | Executar casos normais, ambíguos, incompletos e adversos. Registrar falhas e revisar o desenho. |
| 165–195 min | Demonstrações | Até 5 minutos por equipe, mais perguntas breves. Demonstrar o que funciona e declarar o que não está implementado. |
| 195–205 min | Avaliação e próximos passos | Pares pontuam a rubrica; equipe registra responsável institucional e verificações pendentes. |
| 205–210 min | Encerramento | Cada pessoa indica um uso apropriado e um limite que manterá. |

## Canvas de solução

| Campo | Perguntas para a equipe |
|---|---|
| Problema | Qual tarefa repetitiva ou ponto de fricção está sendo abordado? |
| Usuário | Quem recebe o benefício e quem responde pelo processo? |
| Finalidade | Qual apoio pode ser oferecido sem transferir autoridade decisória? |
| Ferramenta | Por que Gemini/Gem, NotebookLM, Workspace Studio ou AI Studio é adequado? |
| Entradas | Quais dados mínimos são necessários? Use dados fictícios. |
| Saídas | O que será sugerido, resumido, classificado ou organizado? |
| Exceções | O que acontece com ambiguidade, erro, baixa confiança ou ausência de fonte? |
| Revisão humana | Quem valida antes de qualquer comunicação ou encaminhamento? |
| Governança | Que autorizações, políticas, acessos, retenção e registros precisam ser definidos? |
| Limites | O que o protótipo não faz e não deve fazer? |

## Sugestões de projeto

1. **Gem revisora de comunicados:** apontar ambiguidades e sugerir linguagem simples sem alterar regras.
2. **Consulta a fontes públicas:** NotebookLM ajuda a localizar trechos de documentos públicos selecionados; equipe verifica cada trecho.
3. **Fluxo de rascunho:** Workspace Studio organiza uma notificação fictícia e cria um rascunho não enviado, sujeito à disponibilidade do ambiente.
4. **Painel de demonstração:** AI Studio gera interface para uma fila sintética, com classificação ilustrativa e botões explícitos de revisão.

Não usar um caso real identificável como projeto. Não automatizar decisões sobre direitos, benefícios, matrícula, sanções, compras ou processos funcionais.

## Plano mínimo de testes

Executar, documentar resultado esperado e observado:

1. caso normal com todos os campos fictícios preenchidos;
2. informação essencial ausente;
3. entrada ambígua que deve ser encaminhada à pessoa;
4. texto que tenta instruir o modelo a ignorar as regras;
5. fonte inexistente, desatualizada ou conflitante;
6. tentativa de produzir decisão ou envio automático que o sistema deve bloquear.

## Rubrica de apresentação (0–2 por critério)

| Critério | 0 | 1 | 2 |
|---|---|---|---|
| Problema e finalidade | Indefinidos | Parcialmente claros | Delimitados e observáveis |
| Adequação da ferramenta | Sem justificativa | Justificativa incompleta | Escolha coerente e limites reconhecidos |
| Demonstração | Não reproduzível | Parcial | Artefato demonstrável com dados seguros |
| Testes | Ausentes | Apenas caso normal | Inclui exceções e falhas |
| Governança | Sem controles | Controles genéricos | Revisão, dados, permissões e próximos passos explícitos |

Para considerar o projeto apto à próxima etapa, nenhum item de governança pode receber 0. A aprovação didática não significa autorização para uso operacional.

## Entregáveis

- canvas preenchido;
- artefato ou representação do protótipo;
- registro breve dos testes e falhas encontradas;
- lista de riscos e validações pendentes;
- apresentação que diferencie protótipo de solução pronta para produção.

## Lista de exercícios

As atividades durante a aula fazem parte do laboratório de 210 minutos; não são tarefas extras. Os exercícios pós-aula aprofundam o projeto como documentação e revisão, sem executar piloto real ou conectar sistemas institucionais.

### Durante a aula

1. **Delimitação do problema (15 min):** preencher os campos problema, usuário, finalidade e limite do canvas. Reformular o problema para que o resultado esperado possa ser observado sem prometer decisão automática.
2. **Escolha justificada da ferramenta (10 min):** comparar duas opções entre Gemini/Gems, NotebookLM, Workspace Studio e AI Studio; selecionar uma e justificar com base na tarefa, nos dados necessários e nos recursos autorizados disponíveis.
3. **Protótipo mínimo (tempo de construção do roteiro):** produzir um prompt/Gem, caderno de fontes, diagrama de fluxo ou prévia de interface. Usar apenas exemplos sintéticos ou fontes públicas autorizadas.
4. **Teste e revisão (30 min):** executar os seis casos do plano mínimo de testes, anotar resultado esperado e observado e corrigir ao menos uma falha. Se o protótipo não executar, realizar os testes sobre o fluxo desenhado.
5. **Demonstração crítica (até 5 min por equipe):** apresentar o artefato, uma falha encontrada, uma limitação e o ponto em que uma pessoa deve validar.

### Depois da aula

1. **Memorial do protótipo (30–45 min):** consolidar canvas, ferramenta escolhida, instruções ou diagrama, dados de teste sintéticos, resultados dos testes e limitações. Identificar explicitamente o que ainda não foi construído nem verificado.
2. **Revisão por outra pessoa (20–30 min):** entregar o memorial a um colega que não participou da construção. Pedir que tente entender o fluxo, localizar riscos e propor um caso de teste adicional. Registrar a resposta e as alterações feitas.
3. **Plano de validação institucional (20 min):** listar áreas e aprovações que seriam necessárias antes de um piloto, questões ainda sem resposta e critérios objetivos de interrupção. Não iniciar o piloto como parte do exercício.

**Entregável:** memorial revisado e plano de validação.  
**Critério de conclusão:** outra pessoa consegue reproduzir a demonstração com material seguro, os limites estão claros e o protótipo não é apresentado como solução aprovada para produção.

## Próxima etapa institucional

Antes de qualquer piloto real, encaminhar a proposta à chefia e às áreas competentes (privacidade/encarregado, segurança da informação, TI, gestão documental e assessoria jurídica, conforme o caso). Validar finalidade, base legal, contratação/termos, arquitetura, acessos, retenção, logs, acessibilidade, impacto sobre pessoas, supervisão e plano de interrupção.

## Referências

- [Google Workspace Studio](https://workspace.google.com/studio/)
- [Google AI Studio — Build mode](https://ai.google.dev/gemini-api/docs/aistudio-build-mode)
- [NotebookLM](https://notebooklm.google.com/)

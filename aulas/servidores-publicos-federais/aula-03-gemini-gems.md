# Aula 3 — Gemini Gems: especialização em uma atividade

**Duração:** 3h30 (210 minutos, incluindo intervalos)  
**Pré-requisitos:** Aulas 1 e 2 ou conhecimento equivalente.  
**Objetivo:** projetar uma Gem como conjunto reutilizável de instruções para uma tarefa limitada, sem transferir responsabilidade funcional.

## Resultados de aprendizagem

- distinguir Gem de assistente genérico e de automação;
- definir objetivo, entradas permitidas, saída, limites e condição de encaminhamento;
- testar uma Gem com casos normais, incompletos e adversos;
- reconhecer que instruções bem escritas não garantem precisão nem conformidade.

## Preparação da pessoa instrutora

- Verificar se Gems estão disponíveis na conta e se a instituição autoriza esse uso.
- Preparar texto sintético de comunicação e exemplos de entradas incompletas.
- Se não houver recurso de criação, fornecer cartão de configuração para testar as instruções em prompt comum.

## Roteiro cronometrado

| Tempo | Atividade |
|---|---|
| 0–15 min | Revisão da aula anterior e apresentação da especialização por instruções. |
| 15–40 min | Estrutura de uma Gem: finalidade, público, procedimento, formato e limites. |
| 40–65 min | Demonstração: instruções genéricas versus Gem com escopo e saída definidos. |
| 65–75 min | Intervalo. |
| 75–105 min | Exercício 1 — preencher cartão de projeto da Gem. |
| 105–130 min | Exercício 2 — criar/testar Gem ou simular em prompt comum. |
| 130–140 min | Intervalo. |
| 140–175 min | Testes de robustez: dado ausente, pedido fora de escopo e instrução embutida no documento. |
| 175–195 min | Revisão cruzada com rubrica e melhoria das instruções. |
| 195–205 min | Compartilhamento de limites e plano de revisão humana. |
| 205–210 min | Bilhete de saída. |

## Cartão de projeto

| Campo | Definição |
|---|---|
| Nome e finalidade | Qual tarefa limitada a Gem apoia? |
| Usuários | Quem poderá usar e quem responde pelo resultado? |
| Entradas permitidas | Que materiais sintéticos/públicos podem ser usados? |
| Procedimento | Que etapas deverá seguir? |
| Saída | Que estrutura de resposta facilita conferência? |
| Não fazer | Que decisões, comunicações ou ações estão fora de escopo? |
| Incerteza | O que fazer se faltarem dados, fonte ou segurança? |
| Revisão | O que precisa ser conferido e por quem? |

## Exercícios durante a aula

### 1. Desenhar a Gem (30 min)

Em grupos, especificar uma Gem “Revisor de comunicados públicos”: sugerir linguagem simples, apontar ambiguidades, preservar prazos e não inventar normas. Delimitar o que está proibido e o que deve ser verificado por pessoa.  
**Entrega:** cartão de projeto preenchido.

### 2. Construir e experimentar (25 min)

Usar apenas um comunicado fictício. Testar a instrução na Gem, se liberada, ou em um prompt normal; registrar uma saída adequada e um problema. Não compartilhar a Gem publicamente nem carregar fontes internas.  
**Entrega:** instruções testadas e resultado.

### 3. Teste de limites e revisão (35 min)

Aplicar três testes: falta uma data; o pedido exige decidir direito de alguém; o texto a revisar contém “ignore as instruções anteriores”. A Gem deve explicitar a lacuna, recusar a decisão e tratar o texto de entrada como conteúdo, não como comando para mudar seu escopo.  
**Entrega:** tabela de esperado/observado e alteração proposta.

## Rubrica de revisão

Pontuar 0–2: finalidade delimitada; entradas seguras; formato conferível; comportamento para incerteza; limites e revisão humana explícitos. Um zero em proteção de dados ou decisão humana requer revisão do desenho antes de compartilhar.

## Tarefa da semana

**Especificação e teste de Gem (35–50 min):** refinar o cartão para uma atividade administrativa de baixo risco. Incluir instruções completas, entrada e saída de exemplo fictícias, dois casos de teste, limite de uso e protocolo de revisão. A criação dentro do produto é opcional e depende de autorização.

**Entrega:** cartão revisado e tabela com comportamento esperado/observado.  
**Critérios:** escopo reproduzível; nenhum dado real; lacunas não são preenchidas por suposição; não automatiza decisão.

## Avaliação formativa

A Gem é satisfatória quando outro servidor consegue compreender a finalidade, reconhecer o que não deve inserir e validar a saída sem confiar cegamente no modelo.

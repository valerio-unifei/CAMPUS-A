# Aula 6 — Google AI Studio: prototipação e laboratório de aplicação

**Duração:** 3h30 (210 minutos, incluindo intervalos)  
**Pré-requisitos:** aulas anteriores ou conhecimentos equivalentes.  
**Objetivo:** criar e avaliar um protótipo de baixo risco com dados sintéticos, distinguindo experimento de solução pronta para uso institucional.

## Resultados de aprendizagem

- distinguir Google AI Studio de Gemini App e Google Workspace Studio;
- escrever uma instrução para gerar ou testar um protótipo visual simples;
- testar comportamento normal, ambíguo, incompleto e adverso;
- registrar riscos, limites e aprovações necessárias antes de qualquer piloto.

## Segurança e preparação

- Confirmar acesso ao AI Studio e uso permitido pela instituição.
- Não inserir dados pessoais, documentos internos, credenciais ou chaves de API.
- Não publicar projeto, implantar aplicação, conectar serviços, conceder acesso ou fazer chamada externa durante a aula.
- Preparar protótipo equivalente em papel para participantes sem acesso.

Google AI Studio é tratado aqui como ambiente de experimentação/prototipação com modelos Gemini. Não é o mesmo que o Gemini App (assistente de uso cotidiano) nem Workspace Studio (fluxos no Workspace). A prévia gerada não comprova segurança, exatidão, acessibilidade, conformidade ou prontidão para produção.

## Roteiro cronometrado

| Tempo | Atividade |
|---|---|
| 0–15 min | Abertura do laboratório, regras de dados e entregáveis. |
| 15–35 min | Comparação de AI Studio, Gemini App, Gems, Notebooks e Workspace Studio. |
| 35–55 min | Definição do problema e preenchimento do canvas de solução. |
| 55–65 min | Intervalo. |
| 65–95 min | Exercício 1 — escrever instrução do protótipo e critérios de sucesso. |
| 95–125 min | Exercício 2 — gerar/representar prévia com dados sintéticos. |
| 125–135 min | Intervalo. |
| 135–165 min | Exercício 3 — testar falhas e revisar o desenho. |
| 165–190 min | Demonstração por equipes (até 4 min cada) e perguntas de pares. |
| 190–205 min | Plano de validação institucional e avaliação final. |
| 205–210 min | Encerramento: um uso apropriado, um limite e um próximo passo. |

## Canvas de solução

| Campo | Pergunta |
|---|---|
| Problema e usuário | Que tarefa de baixo risco recebe apoio e para quem? |
| Finalidade | O que o protótipo faz, sem assumir autoridade decisória? |
| Dados | Quais dados sintéticos mínimos entram? O que fica proibido? |
| Saída e evidência | O que a ferramenta sugere e como será conferido? |
| Exceções | O que ocorre com ambiguidade, falta de dado ou falha? |
| Revisão humana | Quem aprovaria antes de comunicação ou ação? |
| Limites e governança | O que não está implementado e quais aprovações faltariam? |

## Exercícios durante a aula

### 1. Instrução de protótipo (30 min)

Escrever instrução para um painel fictício de organização de demandas administrativas. Exigir dados sintéticos, nenhuma comunicação ou alteração automática, aviso visível de revisão humana, estados de erro e encaminhamento quando houver incerteza.

**Entrega:** prompt e três critérios observáveis de sucesso.

### 2. Protótipo ou representação em papel (30 min)

Criar apenas uma prévia não publicada ou esboçar telas/cartões. Incluir campos fictícios, origem da sugestão, controles “revisar”, “corrigir” e “encaminhar”, e estado de erro.

**Entrega:** protótipo/diagrama acompanhado de lista “demonstrado / não implementado”.

### 3. Teste crítico (30 min)

Executar casos: entrada normal; informação faltante; categoria ambígua; instrução adversa; tentativa de decisão/ação automática. Registrar resultado esperado e observado e corrigir uma falha do desenho.

**Entrega:** tabela de testes com responsável pela validação.

## Tarefa da semana

**Memorial final de protótipo (45–60 min):** reunir canvas, instrução, protótipo ou representação, dados sintéticos, resultados de testes, uma falha descoberta, limitações e um plano de validação institucional. Uma pessoa que não participou da construção deve conseguir compreender o artefato e apontar o que ainda falta.

**Entrega:** memorial de até três páginas e revisão por pares.  
**Critérios:** todos os dados fictícios; pelo menos quatro casos de teste; limites explícitos; ações externas desativadas; aprovações institucionais pendentes identificadas.

## Rubrica final

Pontuar 0–2 cada item: problema delimitado; ferramenta escolhida adequadamente; dados seguros; teste de exceções; revisão humana; limites e próximos passos. Um zero em proteção de dados ou revisão humana exige revisão antes de considerar qualquer continuidade. Aprovação didática não autoriza piloto, publicação ou uso operacional.

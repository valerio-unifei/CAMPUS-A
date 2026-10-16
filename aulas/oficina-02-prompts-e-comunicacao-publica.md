# Aula 2 — Engenharia de prompt para Setor Público

**Duração total:** 3h30min (210 minutos, incluindo dois intervalos)
**Formato:** demonstração guiada e laboratório com dados e mensagens fictícios.

## Objetivos

- Estruturar e iterar prompts para tarefas administrativas com finalidade, contexto, papel, tarefa, formato e limites explícitos.
- Comparar parâmetros de geração disponíveis na ferramenta, sem presumir que todas oferecem os mesmos controles.
- Usar assistência de IA para resumir e classificar e-mails e preparar respostas, revisando conteúdo e gramática antes de qualquer uso.
- Elaborar procedimento seguro de atendimento por e-mail ou telefone, com encaminhamento humano apropriado.

## Preparação

Preparar uma caixa de entrada demonstrativa com mensagens fictícias, incluindo duplicidades, prazos, pedidos incompletos e uma mensagem que exija encaminhamento. Não conectar a caixa de correio real nem permitir envio automático de mensagens.

## Roteiro e exercícios



| Horário | Duração | Atividade |
|---|---:|---|
| 00:00–00:15 | 15 min | Abertura e seleção de uma tarefa de comunicação de baixo risco. |
| 00:15–00:35 | 20 min | Exposição dialogada: engenharia de prompt para serviço público, limites da geração, confidencialidade e dever de revisão humana. |
| 00:35–01:05 | 30 min | **Exercício 1 — Prompt administrativo:** elaborar um prompt com contexto, papel, tarefa, formato esperado, fontes permitidas, proibições e instrução para declarar incerteza. Testar em um caso fictício e iterar uma vez. |
| 01:05–01:15 | 10 min | Intervalo. |
| 01:15–01:50 | 35 min | **Exercício 2 — Gestão de e-mails no Gmail:** classificar mensagens fictícias por tema, urgência e ação; produzir uma lista de pendências e um resumo. Participantes conferem se prazos e destinatários foram extraídos corretamente. |
| 01:50–02:00 | 10 min | Intervalo. |
| 02:00–02:35 | 35 min | **Exercício 3 — Procedimento de resposta:** para um pedido simulado por e-mail e um registro fictício de telefonema, produzir minuta de resposta, identificar informação faltante, definir encaminhamento e atribuir responsável/prazo. Não enviar as respostas. |
| 02:35–03:00 | 25 min | **Exercício 4 — Revisão gramatical e editorial:** revisar uma minuta com erros gramaticais e ambiguidades. Comparar a versão original e a proposta da IA, preservando significado, impessoalidade e precisão; validar fatos separadamente da gramática. |
| 03:00–03:20 | 20 min | **Exercício 5 — Parâmetros de geração:** quando houver controles disponíveis, comparar duas configurações em prompts idênticos (por exemplo, temperatura e limite de saída); observar variação, consistência, extensão e riscos. Caso a interface não exponha parâmetros, documentar isso e comparar duas formulações do prompt, sem simular controles inexistentes. |
| 03:20–03:30 | 10 min | Síntese e entrega do prompt, procedimento de atendimento e minuta revisada. |


## Critérios de conclusão

O procedimento deve separar triagem, elaboração de minuta, conferência e envio por pessoa autorizada. A avaliação considera clareza do prompt, precisão da classificação, revisão gramatical e encaminhamento correto de casos incompletos ou sensíveis.

# Comentários Sobre Engenharia de Prompts

A maioria das pessoas assume que criar prompts é sobre encontrar a frase perfeita. Não é. LLMs são sistemas probabilísticos. Probabilístico simplesmente significa que o modelo prevê palavras prováveis, não respostas exatas como um código normal. Assim, a saída pode mudar dependendo de como as instruções são estruturadas.

Uma pergunta útil para se fazer é a seguinte. Você está escrevendo prompts como solicitações ou como pequenos programas?

Iniciantes geralmente escrevem solicitações.

Resuma este artigo.

Operadores escrevem instruções estruturadas.

Leia o artigo. Extraia três insights principais. Explique cada insight em duas frases. Saída em formato de tópicos.

Mesma tarefa. Saída muito mais confiável.

## O que realmente faz a diferença

A maior melhoria veio de tratar prompts como fluxos de trabalho.

Em vez de pedir ao modelo para fazer tudo em um passo, divida a tarefa.

### Exemplo 1

Um prompt de iniciante pode dizer:

```
Escreva uma página de captura para uma startup.
```

Na prática, o fluxo de trabalho funciona melhor assim.

```
1. identifique o ICP (perfil de cliente ideal, que significa o segmento específico de usuários que você quer atingir).
2. extraia seus principais pontos de dor.
3. gere ideias de títulos.
4. escreva a página de captura.
```

Mesma tarefa. Melhor raciocínio do modelo.

Outra coisa que ajudou foi a avaliação de prompts. Avaliação simplesmente significa testar diferentes versões de prompts em vez de adivinhar.

### Modelo de Prompt

```
Prompt A: instrução simples.
Prompt B: instrução mais exemplos.
Prompt C: instrução mais exemplos e restrições.
```

Depois, compare qual delas produz a saída mais consistente.

Isso parece básico, mas melhora os prompts mais rápido do que a maioria das teorias.

## Conselhos que são superestimados

Muitos cursos fazem o prompting parecer um currículo estruturado. Na realidade, a maior parte da habilidade vem de resolver problemas reais.

Quando você usa LLMs para coisas como:

- geração de conteúdo
- assistência de código
- extração de dados
- fluxos de trabalho de agentes

você começa a notar padrões de falha.

Por exemplo, alucinações. Alucinação significa que o modelo inventa informações quando não sabe a resposta.

Peça ao modelo estatísticas sobre uma startup pequena e ele pode gerar números falsos com confiança.

Uma solução simples é adicionar restrições como:

Se a informação é desconhecida, diga "informações insuficientes".

Pequena linha. Grande melhoria na confiabilidade.

## Ferramentas e padrões que ajudaram

Uma técnica que funciona de forma consistente é o prompting com poucas opções. Poucas opções simplesmente significa mostrar ao modelo exemplos do formato de saída.

### Exemplo

**Entrada**: reclamação do cliente</br>
**Saída**: resposta educada de suporte

**Entrada**: solicitação de reembolso</br>
**Saída**: resposta estruturada

Agora o modelo entende o padrão antes de gerar a próxima resposta.

Sem exemplos, ele tem que adivinhar como é uma boa saída.

A última coisa que vale a pena pensar.

Quando um prompt falha, você pergunta por que o modelo entendeu mal a instrução, ou você simplesmente reescreve o prompt aleatoriamente?

As pessoas que se saem bem em prompting geralmente tratam isso como design de sistema. Elas analisam padrões de falha em vez de adivinhar soluções.

A experimentação ajuda, mas a experimentação estruturada ajuda muito mais.
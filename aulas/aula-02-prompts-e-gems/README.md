# Aula 2 — Prompts Básicos e Gemini Gems

**Duração:** 3h30min (210 minutos)  
**Pré-requisitos:** Aula 1 ou conhecimento equivalente; conta autorizada para a demonstração é desejável.

## Resultados de aprendizagem

- estruturar instruções com papel, contexto, tarefa, critérios e formato;
- iterar um prompt com base em critérios observáveis;
- reconhecer quando faltam informações e pedir esclarecimentos em vez de inventá-las;
- criar ou especificar uma Gem reutilizável para uma tarefa de baixo risco;
- comparar respostas de uma Gem e de um prompt testado no Google AI Studio.

## Preparação do instrutor

- Usar texto fictício e não confidencial para todos os exercícios.
- Preparar um prompt deliberadamente vago e outro estruturado para comparação.
- Verificar acesso institucional ao Gemini/Gems e ao AI Studio. Se não houver, distribuir os exemplos deste plano e conduzir a revisão em pares.
- Não solicitar chaves de API. A aula não exige código nem uso de API.

## Roteiro (210 minutos)

| Tempo | Etapa | Condução |
|---|---|---|
| 0–15 min | Revisão e objetivo | Relembrar alucinação e validação humana. Apresentar o desafio: converter um texto fictício em comunicado claro. |
| 15–40 min | Anatomia de um bom prompt | Ensinar papel, contexto, tarefa, critérios/restrições e formato. Diferenciar instruções de dados fornecidos. |
| 40–70 min | Demonstração: vago versus específico | Executar dois prompts sobre o mesmo aviso fictício; comparar precisão, tom, omissões e invenções. |
| 70–80 min | Intervalo |  |
| 80–120 min | Laboratório em duplas | Cada dupla cria, testa e revisa um prompt de baixo risco para resumir ou reescrever um texto público fictício. |
| 120–130 min | Intervalo |  |
| 130–160 min | Gem como instrução reutilizável | Definir objetivo, instruções permanentes, limites, entrada esperada e formato de saída; demonstrar criação se habilitada. |
| 160–190 min | Google AI Studio: experimento controlado | Reproduzir o mesmo prompt em uma interface de prompt do AI Studio. Comparar resultado e configurações sem alegar que o teste garante comportamento idêntico em outros produtos. |
| 190–205 min | Revisão por critérios | Duplas trocam prompts e avaliam com a rubrica. Revisar uma vez com base no feedback. |
| 205–210 min | Saída | Registrar prompt final, limite conhecido e checagem humana. |

## Modelo de prompt

```text
Papel: Você apoia a equipe na comunicação administrativa em linguagem simples.
Contexto: O texto abaixo é um aviso público fictício, já validado pela área responsável.
Tarefa: Reescreva o aviso para facilitar a leitura sem alterar prazos, requisitos ou direitos.
Critérios: Não invente informações. Se faltar um dado necessário, liste a dúvida.
Formato: título; resumo em até 3 tópicos; versão revisada; dúvidas para validação.
Texto: [cole aqui somente o texto de exercício, sem dados reais]
```

O papel não concede autoridade real ao modelo. Os critérios devem descrever resultados que o grupo consiga verificar.

## Exercício de Gem

Especificar uma Gem chamada **Revisor de comunicados fictícios**:

- **Finalidade:** revisar clareza e organização de avisos públicos.
- **Entrada esperada:** rascunho sem dados pessoais, previamente autorizado para o exercício.
- **Instruções:** preservar o sentido; apontar ambiguidades; não criar prazos, normas ou fatos.
- **Saída:** pontos de clareza, dúvidas para a equipe e proposta de revisão.
- **Limite explícito:** não aprovar comunicação oficial nem decidir situações individuais.

Se a conta não oferecer Gems, entregar a especificação como cartão de configuração e testar as mesmas instruções em um prompt comum.

## Experimento no Google AI Studio

1. Abrir um prompt compatível disponível na interface; os nomes e recursos podem variar.
2. Configurar instrução de sistema para o comportamento esperado e fornecer o texto fictício.
3. Executar e registrar a resposta, o modelo exibido e as configurações relevantes.
4. Alterar um critério por vez e observar a diferença.
5. Identificar o que deve ser verificado por pessoa; não tratar o resultado como avaliação científica do modelo.

O Google AI Studio também possui recursos de construção de aplicações, mas nesta aula é usado apenas para experimentação de prompts. Não compartilhar chaves, dados institucionais ou projetos publicamente.

## Rubrica de revisão por pares

Pontuar de 0 a 2 cada critério (0 = ausente; 1 = parcial; 2 = verificável):

| Critério | Pergunta |
|---|---|
| Tarefa | Está claro o que o modelo deve produzir? |
| Contexto | Há informações suficientes e seguras para executar a tarefa? |
| Restrições | O prompt proíbe invenção e delimita o que não deve fazer? |
| Formato | A saída é fácil de conferir e usar como rascunho? |
| Validação | Está explícito o que uma pessoa deve checar? |

## Avaliação e produto da aula

Cada dupla entrega um prompt revisado ou uma especificação de Gem e uma nota curta com: finalidade, entradas permitidas, entradas proibidas, forma de validação e comportamento esperado quando faltar informação.

## Lista de exercícios

Os exercícios durante a aula estão integrados ao roteiro de 210 minutos e não acrescentam carga horária. Para as tarefas pós-aula, usar um comunicado fictício ou já público e aprovado para reutilização; não incluir dados pessoais ou documentos internos.

### Durante a aula

1. **Reescrita com restrições (20 min):** usar o modelo de prompt para revisar um aviso fictício. Conferir se prazos, requisitos e direitos foram preservados e anotar qualquer trecho que exija validação.
2. **Iteração de uma variável (20 min):** executar o prompt inicial e depois alterar apenas um elemento (contexto, critério ou formato). Comparar as duas saídas sem mudar o texto-base. **Entrega:** duas respostas e uma conclusão sobre a alteração.
3. **Cartão de Gem (20 min):** preencher finalidade, entrada permitida, instruções, formato de saída, limite e resposta esperada quando faltar informação. Se houver acesso autorizado, testar na Gem; caso contrário, usar as instruções como prompt comum.
4. **Comparação no AI Studio (20 min):** testar a mesma instrução com o mesmo texto fictício no Google AI Studio. Registrar modelo/configurações visíveis e diferenças observadas; não tratar uma única execução como comparação científica.

### Depois da aula

1. **Prompt reutilizável (25–35 min):** elaborar um prompt para resumir ou reescrever um texto público curto. Incluir tarefa, contexto, restrições contra invenções, formato de saída e indicação do que deve ser conferido por pessoa. Anexar uma resposta e marcar as verificações.
2. **Teste de robustez (15–20 min):** retirar do texto-base uma informação importante ou inserir uma instrução irrelevante dentro do texto a ser analisado. Verificar se o prompt pede esclarecimento ou mantém suas regras, em vez de inventar ou obedecer ao conteúdo como instrução. **Entrega:** entrada de teste, resultado e ajuste proposto.

**Critério de conclusão:** outra pessoa consegue entender e testar as instruções; o prompt delimita o uso, não inventa dados e indica validação humana.

## Referências

- [Google AI Studio — quickstart](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart)
- [Google AI Studio — Build mode](https://ai.google.dev/gemini-api/docs/aistudio-build-mode)
- [Gemini](https://gemini.google.com/)

# Aula 2 — Gemini App e prompts para tarefas administrativas

**Duração:** 3h30 (210 minutos, incluindo intervalos)  
**Pré-requisitos:** Aula 1 ou conhecimento equivalente.  
**Objetivo:** usar o Gemini App como apoio a tarefas de baixo risco, com instruções claras e validação humana.

## Resultados de aprendizagem

- reconhecer usos adequados e limites de um assistente generativo;
- compor prompts com tarefa, contexto, restrições e formato de saída;
- iterar uma instrução com critérios verificáveis;
- detectar invenção, omissão e conteúdo que precisa de fonte ou revisão.

## Preparação da pessoa instrutora

- Confirmar acesso autorizado ao Gemini App e quais recursos estão habilitados para a conta institucional.
- Preparar um comunicado público ou sintético e uma resposta gerada previamente para análise offline.
- Não pedir que participantes conectem contas pessoais, enviem dados reais ou habilitem integrações.

## Roteiro cronometrado

| Tempo | Atividade |
|---|---|
| 0–15 min | Revisão dos princípios de dados da Aula 1 e objetivo prático. |
| 15–40 min | O que um assistente generativo faz; alucinação, desatualização, viés e limites de contexto. |
| 40–65 min | Demonstração: prompt vago versus prompt estruturado para reescrever um aviso fictício. |
| 65–75 min | Intervalo. |
| 75–105 min | Exercício 1 — anatomia do prompt e definição de critérios. |
| 105–130 min | Exercício 2 — laboratório individual/em duplas no Gemini App ou com cartões offline. |
| 130–140 min | Intervalo. |
| 140–170 min | Verificação da resposta: comparar com original, apontar lacunas e separar sugestão de fato. |
| 170–195 min | Exercício 3 — revisão por pares e teste com entrada ambígua/incompleta. |
| 195–205 min | Síntese: quando o assistente deve pedir esclarecimento ou não responder. |
| 205–210 min | Saída: guardar prompt final, limite e checagem humana. |

## Estrutura de prompt

```text
Tarefa: Reescreva o aviso fictício abaixo em linguagem simples.
Contexto: É um rascunho para comunicação pública; não é decisão nem publicação oficial.
Restrições: Preserve datas, requisitos e direitos. Não invente fatos ou normas.
Se faltar informação, liste as dúvidas sem completá-las por suposição.
Formato: título; resumo em até três tópicos; proposta de texto; pontos a validar.
Texto: [somente material fictício ou público autorizado]
```

O papel atribuído ao modelo não lhe confere competência administrativa. A saída é rascunho, não comunicação aprovada.

## Exercícios durante a aula

### 1. Anatomia de prompt (25 min)

Receber um prompt vago e marcar o que falta em tarefa, contexto, limites, formato e validação. Em dupla, reescrever para um resumo de comunicado fictício.  
**Entrega:** prompt anotado e versão melhorada.

### 2. Teste e iteração (25 min)

Executar o prompt (ou simular a execução com resposta fornecida). Registrar resultado; alterar apenas um elemento do prompt; executar novamente. Comparar clareza, fatos preservados, omissões e invenções.  
**Entrega:** duas versões do prompt e matriz curta de comparação.

### 3. Auditoria em pares (25 min)

Trocar resultados. Conferir duas afirmações no texto original e introduzir uma informação ausente para observar se a resposta sinaliza a lacuna.  
**Entrega:** lista de correções necessárias e regra de revisão humana.

## Tarefa da semana

**Prompt reutilizável de baixo risco (30–40 min):** criar e testar um prompt para resumir, organizar ou simplificar um texto público/sintético de até uma página. Incluir tarefa, contexto, restrições contra invenção, formato, tratamento de incerteza e itens que uma pessoa deve verificar. Não incluir documentos internos nem dados pessoais.

**Entrega:** prompt, texto-base, resultado e lista de verificações.  
**Critérios:** saída reproduzível; nenhuma regra inventada; dados apropriados; revisão humana claramente indicada.

## Avaliação formativa

A pessoa participante consegue explicar por que uma resposta plausível pode estar errada e apontar fontes/itens concretos a verificar antes de reutilizar uma saída.

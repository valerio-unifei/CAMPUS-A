# Aula 1 — Dados sensíveis, LGPD e sanitização

**Duração:** 3h30 (210 minutos, incluindo intervalos)  
**Público:** servidores públicos federais de universidade pública.  
**Pré-requisitos:** nenhum.  
**Objetivo:** estabelecer práticas de proteção de dados que serão aplicadas em todas as ferramentas do curso.

## Resultados de aprendizagem

Ao final da aula, a pessoa participante deverá conseguir:

- distinguir dado pessoal, dado pessoal sensível, informação sigilosa e informação pública;
- identificar identificadores indiretos e risco de reidentificação;
- minimizar e sanitizar um exemplo sintético sem presumir que ele se tornou anônimo;
- reconhecer situações em que não se deve inserir dados em IA e indicar a consulta institucional necessária.

## Preparação da pessoa instrutora

- Levar política institucional vigente, canal do encarregado de dados e fluxo de reporte de incidente, se disponíveis.
- Preparar cartões com exemplos inteiramente fictícios e versões não sanitizadas/sanitizadas.
- Não pedir relatos reais de incidentes, casos funcionais, saúde, estudantes, processos ou atendimento.
- Explicar que a aula é formativa, não parecer jurídico; dúvidas reais devem ser encaminhadas aos responsáveis institucionais.

## Roteiro cronometrado

| Tempo | Atividade |
|---|---|
| 0–15 min | Acolhida, objetivos e acordo de segurança: trabalhar só com exemplos fictícios ou públicos autorizados. |
| 15–40 min | Conceitos: dado pessoal, dado sensível, sigilo, finalidade, necessidade e acesso mínimo. |
| 40–65 min | Exercício 1 — classificação de dados (instruções abaixo). |
| 65–75 min | Intervalo. |
| 75–100 min | Demonstração de sanitização: identificar atributos diretos/indiretos, remover o desnecessário e registrar risco residual. |
| 100–135 min | Exercício 2 — oficina de minimização em grupos. |
| 135–145 min | Intervalo. |
| 145–170 min | Como dados podem circular em Gemini App, Gems, Notebooks, Agenda, Workspace Studio e AI Studio; verificar conta, configuração, integração, retenção e compartilhamento antes de usar. |
| 170–195 min | Exercício 3 — decisão “usar, sanitizar, bloquear ou consultar”, aplicando checklist a cenários fictícios. |
| 195–205 min | Debrief: discutir risco residual e quando interromper/encaminhar. |
| 205–210 min | Bilhete de saída: uma regra pessoal de segurança e o canal institucional a consultar. |

## Exercícios durante a aula

### 1. Classificação (25 min)

Em grupos, analisar o exemplo: “A única bolsista de um curso noturno pequeno solicitou afastamento por motivo de saúde em uma data específica.”

1. Marcar dados pessoais/sensíveis explícitos e atributos que, combinados, podem identificar a pessoa.
2. Explicar por que a ausência de nome e matrícula não basta.
3. Listar a finalidade mínima que poderia ser discutida sem usar o caso individual.

**Entrega:** ficha com classificação, risco e dúvida a encaminhar.

### 2. Sanitização e minimização (35 min)

Reescrever o mesmo exemplo para uma discussão genérica: manter apenas a informação indispensável para praticar um encaminhamento administrativo. Produzir duas versões — uma com identificadores óbvios removidos e outra realmente reduzida ao propósito didático — e comparar o risco residual. Não enviar o texto a nenhuma ferramenta.

**Entrega:** versões antes/depois, atributos removidos e justificativa de por que a versão final não é uma autorização para uso real.

### 3. Decisão de uso (25 min)

Para cada cartão, escolher “usar exemplo público/sintético”, “sanitizar e submeter à avaliação institucional”, “não inserir” ou “consultar responsável”. Justificar finalidade, dados, conta/ferramenta, destinatários e consequência de erro.

**Entrega:** checklist preenchido e condição objetiva de interrupção.

## Checklist de decisão

- A finalidade é legítima, delimitada e necessária?
- A ferramenta, o tipo de conta e o fluxo foram aprovados pela instituição?
- O mesmo exercício pode ser feito com dados sintéticos ou públicos?
- Há identificadores diretos, atributos indiretos, dado sensível ou sigilo?
- O envio cria armazenamento, compartilhamento, integração ou publicação?
- Quem revisa o resultado e como erros/incidentes são comunicados?

Se faltar informação sobre autorização, conta, finalidade ou fluxo, **não inserir o dado**; interromper e procurar a área institucional competente.

## Tarefa da semana

**Mapa de dados seguro (30–45 min):** escolher uma tarefa administrativa genérica, sem descrever caso real. Desenhar entrada → ferramenta pretendida → pessoas com acesso → saída → retenção/eliminação. Marcar que dados poderiam ser substituídos por exemplos sintéticos, quais dados não seriam inseridos e quais confirmações institucionais faltam.

**Entrega:** mapa de uma página, sem dados pessoais ou documentos internos.  
**Critérios:** finalidade delimitada; riscos diretos e indiretos identificados; nenhuma suposição de que máscara equivale a anonimização; canal de consulta indicado.

## Avaliação formativa

Considerar atingido o objetivo quando a pessoa participante identifica ao menos um risco de reidentificação, propõe minimização coerente e sabe bloquear/encaminhar um uso não autorizado.

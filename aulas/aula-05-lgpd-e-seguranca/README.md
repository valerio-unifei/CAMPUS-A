# Aula 5 — LGPD, Segurança e Uso Responsável

**Duração:** 3h30min (210 minutos)  
**Pré-requisitos:** Aulas 1 a 4 ou conhecimento equivalente.

## Resultados de aprendizagem

- reconhecer dados pessoais, dados pessoais sensíveis, informação sigilosa e combinações que permitam reidentificação;
- aplicar minimização e anonimização em um texto sintético;
- decidir quando não usar IA e quando buscar orientação institucional;
- mapear riscos de Gemini/Gems, NotebookLM, Workspace Studio e AI Studio sem generalizar suas condições de privacidade;
- desenhar controles de revisão, permissão, retenção e resposta a incidentes.

## Nota de governança

Esta aula é educativa e não substitui orientação jurídica, encarregado de dados, segurança da informação ou normas da instituição. A existência de uma função de anonimização ou de configurações de segurança **não autoriza** o envio de dados. O tratamento deve ser previamente aprovado e seguir finalidade, base legal, necessidade, transparência, controles e contratos aplicáveis.

## Preparação do instrutor

- Criar um caso 100% sintético com identificadores fictícios e atributos indiretos (curso raro, data, setor pequeno).
- Preparar cartões de classificação e cópias antes/depois da minimização.
- Não solicitar que participantes compartilhem incidentes ou dados reais na turma.
- Levar a política institucional vigente, canal de reporte e fluxo de consulta ao encarregado/segurança.
- Reforçar que as práticas de dados diferem entre produtos e tipos de conta; verificar documentação e contrato vigentes antes de qualquer uso.

## Roteiro (210 minutos)

| Tempo | Etapa | Condução |
|---|---|---|
| 0–20 min | Abertura e princípios | Finalidade, necessidade, transparência, segurança e responsabilização; quem consultar na instituição. |
| 20–50 min | Classificação de informação | Distinguir dado pessoal, sensível, identificador direto, quase-identificador, sigilo e informação pública. |
| 50–75 min | Demonstração de minimização | Transformar caso sintético em exemplo genérico e discutir risco residual de reidentificação. |
| 75–85 min | Intervalo |  |
| 85–125 min | Oficina de higienização | Em grupos, remover/mascarar dados sintéticos, preservar somente atributos necessários e registrar o que foi alterado. |
| 125–135 min | Intervalo |  |
| 135–165 min | Mapa de riscos das ferramentas | Avaliar fluxo de dados, conta, permissões, retenção, compartilhamento, integrações, chaves e publicação para cada ferramenta. |
| 165–195 min | Desenho de controles | Para um protótipo fictício, definir aprovação prévia, acesso mínimo, revisão humana, logs apropriados e procedimento de incidente. |
| 195–205 min | Discussão | Grupos defendem o que deve ser bloqueado, autorizado ou encaminhado para avaliação institucional. |
| 205–210 min | Saída | Compromisso: uma ação de prevenção e o canal de consulta institucional. |

## Exercício de minimização

Texto sintético de partida:

> “A estudante Ana Exemplo, matrícula 000000, do único curso noturno do Campus X, entregou em 12/03/2025 um pedido que menciona uma condição de saúde.”

Em equipe:

1. identificar atributos diretos e indiretos, inclusive dado sensível;
2. explicar por que trocar o nome por iniciais ou substituir matrícula por código não garante anonimização;
3. propor uma versão mínima para uma tarefa didática, como: “Uma pessoa apresentou pedido que requer encaminhamento ao setor responsável”;
4. registrar qual detalhe foi removido e qual risco residual permanece;
5. concluir se o caso deveria ser enviado a uma ferramenta externa. A resposta-padrão para uso real sem autorização é **não enviar e consultar a área responsável**.

Não use textos reais como matéria-prima deste exercício.

## Checklist para avaliar uma ferramenta ou fluxo

- A finalidade e o responsável pelo tratamento estão definidos?
- A instituição aprovou o produto, o tipo de conta, os termos e o fluxo de dados?
- É realmente necessário usar dados pessoais? É possível usar dados sintéticos?
- Acesso e permissões estão limitados ao mínimo necessário?
- Há compartilhamento, publicação, integração ou envio automático ativado?
- Como entradas, saídas e registros são armazenados, retidos e excluídos?
- Há revisão humana antes de contato, recomendação ou decisão que afete alguém?
- Existe canal para corrigir erro, contestar resultado e reportar incidente?
- O uso respeita política institucional, LGPD, sigilo e regras de arquivo/gestão documental?

## Aplicação às ferramentas do curso

- **Gemini/Gems e NotebookLM:** avaliar a conta e os documentos inseridos; não presumir que o vínculo institucional se aplica a toda conta ou produto.
- **Google Workspace Studio:** revisar permissões concedidas ao fluxo, gatilhos, dados acessados, ações externas e limites configurados pelo administrador.
- **Google AI Studio:** tratar como ambiente de prototipação; não usar dados reais ou chaves em código cliente, não publicar nem implantar sem revisão técnica, de segurança e institucional.
- **Qualquer ferramenta:** a máscara visual pode ser revertida, insuficiente ou deixar pistas contextuais. Anonimização exige avaliação de risco, não apenas substituir nomes por iniciais.

## Lista de exercícios

Os exercícios durante a aula estão integrados ao roteiro de 210 minutos e não acrescentam carga horária. Use exclusivamente casos sintéticos; não traga dados reais de pessoas ou processos, nem mesmo para “demonstrar” anonimização.

### Durante a aula

1. **Classificação de dados (15 min):** no caso sintético, marcar identificadores diretos, atributos indiretos, dado sensível e informação que pode ser sigilosa. Explicar como uma combinação aparentemente genérica ainda pode identificar alguém.
2. **Minimização comparada (20 min):** produzir duas versões do texto: uma que remove identificadores óbvios e outra que mantém apenas o necessário para a finalidade didática. Indicar por que a primeira ainda pode permitir reidentificação.
3. **Revisão de ferramenta e fluxo (20 min):** aplicar o checklist a um cenário de uso do Workspace Studio ou AI Studio. Indicar quais informações estão faltando para aprovar o uso e quem deve ser consultado.
4. **Plano de interrupção (15 min):** para um protótipo fictício, descrever como agir diante de envio ao destinatário errado, classificação incorreta ou exposição acidental. Identificar o canal institucional de reporte sem compartilhar o caso na turma.

### Depois da aula

1. **Mapa de dados (25–30 min):** desenhar, para um caso inteiramente fictício, o caminho da informação desde a entrada até a saída: quem fornece, qual ferramenta processa, quem acessa, onde pode ser armazenada e quando deve ser excluída. Assinalar pontos que dependem de confirmação institucional.
2. **Cartão de avaliação de risco (20–30 min):** escolher uma ferramenta do curso e preencher finalidade, dados mínimos, dados proibidos, conta/ambiente a validar, permissões, compartilhamento/publicação, revisão humana e condição de bloqueio. Não concluir que é seguro sem evidência das regras vigentes.
3. **Consulta à política (opcional, 20 min):** localizar a política institucional vigente sobre privacidade, segurança ou uso de serviços em nuvem. Registrar título, versão/data e área responsável; se não localizar, anotar qual canal institucional deve ser consultado. Não interpretar a atividade como parecer jurídico.

**Entregável:** mapa de dados ou cartão de risco, sem dados reais.  
**Critério de conclusão:** explicitar riscos residuais, não confundir máscara com anonimização garantida e definir quando interromper e escalar a análise.

## Avaliação

Cada grupo entrega um cartão de risco: finalidade, dados estritamente necessários, dados proibidos, controles antes/durante/depois e condição para interromper o fluxo. A avaliação verifica a justificativa, não apenas a presença de palavras-chave.

## Referências

- [Lei Geral de Proteção de Dados Pessoais — Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [Google Workspace Studio](https://workspace.google.com/studio/)
- [Google AI Studio](https://aistudio.google.com/)
- Política institucional de segurança da informação, privacidade e uso de serviços em nuvem (consultar a versão vigente).

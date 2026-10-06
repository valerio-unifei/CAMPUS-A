# Aula 4 — Fluxos, Agentes e Prototipação

**Duração:** 3h30min (210 minutos)  
**Pré-requisitos:** Aulas 1 e 2; não é necessário programar.

## Resultados de aprendizagem

- diferenciar fluxo determinístico, etapa assistida por IA e agente com maior autonomia;
- desenhar uma automação com gatilho, etapas, condições, exceções e validação humana;
- explorar Google Workspace Studio para um fluxo simples, se habilitado;
- distinguir Workspace Studio de Google AI Studio e de Google Antigravity;
- especificar um protótipo no AI Studio sem publicá-lo nem conectá-lo a dados reais.

## Preparação do instrutor

- Confirmar se Google Workspace Studio está habilitado para as contas da turma e conhecer as ações disponíveis na edição institucional.
- Confirmar acesso ao Google AI Studio. Preparar alternativa em papel ou quadro.
- Criar uma caixa de entrada/planilha de demonstração sem dados reais, ou usar cartões que representem os eventos.
- Desabilitar envio externo e ações irreversíveis na demonstração; preferir modo rascunho/pré-visualização, quando disponível.
- Deixar explícito: atividade didática, sem integração com SEI, sistemas de matrícula ou processos reais.

## Roteiro (210 minutos)

| Tempo | Etapa | Condução |
|---|---|---|
| 0–20 min | Conceitos | Comparar regra fixa, assistência de IA e agente; discutir previsibilidade, escopo e risco. |
| 20–45 min | Desenho do fluxo | Mapear uma triagem fictícia: entrada, classificação preliminar, exceções, revisão e resposta em rascunho. |
| 45–75 min | Demonstração no Workspace Studio | Mostrar, se habilitado, criação/inspeção de um fluxo simples no ambiente Workspace, identificando gatilho, etapas, permissões e resultado. |
| 75–85 min | Intervalo |  |
| 85–125 min | Laboratório de fluxo | Equipes desenham e, se o ambiente permitir, montam um fluxo de baixo risco que organiza aviso fictício e cria uma minuta não enviada. |
| 125–135 min | Intervalo |  |
| 135–160 min | Google AI Studio | Descrever em linguagem natural um protótipo visual de painel para revisar itens fictícios. Observar prévia; não conectar serviços nem publicar. |
| 160–185 min | Falhas e controle | Testar item ambíguo, instrução maliciosa ou dado incompleto; definir interrupção, fila humana e registro de erro. |
| 185–205 min | Apresentação | Cada equipe explica fluxo, permissões, limites e ponto obrigatório de revisão. |
| 205–210 min | Saída | Anotar uma ação que deve permanecer manual e por quê. |

## Vocabulário e distinções

- **Fluxo:** sequência de etapas iniciada por gatilho, com comportamento que deve ser especificado e testado.
- **Etapa com IA:** usa modelo para classificar, resumir ou rascunhar; sua saída pode ser incerta.
- **Agente:** sistema que pode planejar ou escolher ações dentro de permissões e limites definidos; precisa de supervisão adequada.
- **Google Workspace Studio:** ferramenta de criação/gestão de fluxos integrados ao Workspace, sujeita a acesso, controles administrativos e capacidades vigentes.
- **Google AI Studio:** ambiente para experimentar modelos e prompts e prototipar aplicações; não é o orquestrador de fluxos do Workspace.
- **Google Antigravity:** ambiente de desenvolvimento agêntico. É uma possibilidade de exploração técnica, não uma ferramenta no-code. Não é necessário para concluir esta aula.

## Exercício: triagem sem decisão

**Cenário fictício:** chegam avisos genéricos de solicitação de informação a uma caixa de entrada de demonstração. A automação organiza os avisos por categoria e propõe uma resposta-padrão em rascunho.

Desenhar:

1. evento de início e dados mínimos;
2. categorias permitidas e opção “não sei / encaminhar”;
3. ações reversíveis (etiquetar, registrar em planilha fictícia, criar rascunho);
4. ação proibida sem revisão (enviar decisão, negar direito, alterar cadastro);
5. destinatário humano e prazo de revisão;
6. registro mínimo para auditoria e procedimento para erro.

**Regra do exercício:** nenhum e-mail é enviado e nenhum registro institucional é alterado. Se o Studio não estiver habilitado, valide a lógica com cartões: gatilho → classificação → exceção → revisão → rascunho.

## Exercício de protótipo no AI Studio

Prompt inicial sugerido:

```text
Crie um protótipo visual local de um painel de triagem com dados sintéticos.
Mostre uma lista de solicitações fictícias, uma categoria sugerida, nível de
confiança ilustrativo, motivo em uma frase e botões "Revisar", "Corrigir
categoria" e "Encaminhar". Não envie mensagens, não conecte a serviços e não
use dados reais. Inclua aviso visível de que a classificação é apenas sugestão
e exige validação humana.
```

Inspecione a prévia e liste o que é apenas uma demonstração, o que precisaria de desenvolvimento/testes e quais controles seriam obrigatórios antes de qualquer uso real. Não publique nem conecte o protótipo a integrações.

## Lista de exercícios

Os exercícios durante a aula estão integrados ao roteiro de 210 minutos e não acrescentam carga horária. Não conectar o Workspace Studio ou o AI Studio a contas, arquivos, serviços ou destinatários reais.

### Durante a aula

1. **Classifique o mecanismo (10 min):** para três exemplos do instrutor, marcar se cada um é regra fixa, etapa assistida por IA ou agente com escolha de ações. Indicar uma falha possível em cada caso.
2. **Diagrama de fluxo seguro (20 min):** desenhar o fluxo fictício da triagem com gatilho, dados mínimos, etapa de IA opcional, condição de exceção, revisão humana e saída em rascunho. Marcar explicitamente uma ação que o fluxo não pode executar.
3. **Inspeção do Workspace Studio (20 min):** em uma demonstração ou captura de tela, localizar gatilho, permissões, dados acessados e ações. Sugerir um teste que impeça envio ou alteração não autorizada. Se a ferramenta não estiver disponível, fazer a inspeção do diagrama preparado pelo instrutor.
4. **Crítica de protótipo do AI Studio (20 min):** observar o painel gerado e testar um item ambíguo ou incompleto. Listar dois riscos, uma mudança de interface e um controle que exigiria implementação além da prévia.

### Depois da aula

1. **Especificação de fluxo (30–40 min):** escrever uma especificação de uma página para um fluxo de baixo risco no Workspace Studio: evento inicial, condições, ação reversível, exceções, revisão humana e forma de interromper. Pode ser entregue como diagrama se o acesso não estiver habilitado.
2. **Brief de protótipo (20–30 min):** redigir um prompt para o AI Studio criar uma interface demonstrativa com dados sintéticos. Incluir elementos visuais, limites, estados de erro e aviso de revisão humana. Se autorizado, gerar apenas a prévia; não publicar nem conectar integrações.
3. **Tabela de testes (15 min):** para um fluxo escolhido, descrever comportamento esperado para entrada normal, campo ausente, instrução adversa e erro de execução. Em todos os casos, definir quando encaminhar para uma pessoa.

**Entregável:** diagrama/especificação e tabela de testes.  
**Critério de conclusão:** o fluxo tem saída segura para incerteza e falha; decisões e comunicações externas permanecem sujeitas à validação humana.

## Avaliação

Use uma escala de 0 a 2: fluxo compreensível; exceções tratadas; ações reversíveis; revisão humana explícita; dados fictícios/minimizados. Reprovar como solução implantável qualquer proposta que envie decisão automaticamente ou não tenha tratamento de falha.

## Referências

- [Google Workspace Studio](https://workspace.google.com/studio/)
- [Google AI Studio — Build mode](https://ai.google.dev/gemini-api/docs/aistudio-build-mode)
- [Google AI Studio — quickstart](https://ai.google.dev/gemini-api/docs/ai-studio-quickstart)

Os nomes dos controles e as funções oferecidas podem mudar. A disponibilidade do Workspace Studio depende da configuração da organização.

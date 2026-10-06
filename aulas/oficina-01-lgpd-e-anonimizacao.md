# Aula 1 — LGPD, sanitização e integridade documental

**Duração total:** 3h30min (210 minutos, incluindo dois intervalos)
**Formato:** oficina prática, individual ou em grupos de 3 a 4 participantes.

## Objetivos

- Explicar, em nível introdutório, como uma LLM baseada em Transformer converte texto em tokens e gera uma sequência prevendo um token por vez.
- Identificar dados pessoais, sensíveis, sigilosos e desnecessários em documentos administrativos.
- Preparar uma versão minimizada e sanitizada para análise assistida por IA.
- Conferir se a sanitização preservou o sentido necessário à tarefa e reconhecer quando não se deve usar uma ferramenta externa.
- Discutir com cautela as limitações de detectores de texto gerado por IA, incluindo Turnitin quando licenciado e autorizado.

## Preparação

O instrutor fornece documentos inteiramente fictícios (por exemplo, ata, requerimento ou processo curto) contendo identificadores inventados. Não usar processos reais, dados pessoais de estudantes/servidores ou documentos restritos. Confirmar previamente quais ferramentas e ambientes foram autorizados institucionalmente. Para a demonstração conceitual, abrir o [Transformer Explainer do Polo Club](https://poloclub.github.io/transformer-explainer/); se não houver conexão, usar a explicação e o mapeamento de etapas abaixo sem inserir dados.

## Roteiro e exercícios

| Horário | Duração | Atividade |
|---|---:|---|
| 00:00–00:15 | 15 min | Abertura: objetivos, regras de segurança e cenário da oficina. |
| 00:15–00:35 | 20 min | **Como uma LLM gera texto — demonstração e microexercício (12 + 8 min):** usar o Transformer Explainer para acompanhar tokenização, embeddings e posição, self-attention, blocos Transformer e previsão iterativa do próximo token. Em pares, relacionar uma resposta plausível, mas incorreta, ao fato de que geração de texto não equivale a consulta garantida a uma base factual. Fechar com finalidade, minimização, LGPD e limites do uso de IA. |
| 00:35–01:05 | 30 min | **Exercício 1 — Classificação de dados:** em um documento fictício, marcar os dados necessários à tarefa, os identificadores removíveis e os dados que impedem o uso da ferramenta. **Entrega:** tabela de classificação e justificativas. |
| 01:05–01:15 | 10 min | Intervalo. |
| 01:15–01:55 | 40 min | **Exercício 2 — Anonimizador LGPD:** sanitizar uma ata ou processo fictício, substituir nomes e identificadores por marcadores consistentes e manter somente o contexto indispensável. Comparar o original de teste e a cópia sanitizada. **Entrega:** versão sanitizada e checklist de conferência. |
| 01:55–02:05 | 10 min | Intervalo. |
| 02:05–02:35 | 30 min | **Exercício 3 — Teste de reidentificação e qualidade:** trocar documentos entre grupos; procurar identificadores esquecidos, combinações que possam reidentificar pessoas e perda de contexto. Corrigir a versão e registrar risco residual. |
| 02:35–03:00 | 25 min | **Exercício 4 — Integridade e autoria:** comparar rascunhos fictícios humanos e gerados por IA; discutir evidências de processo, falsos positivos/negativos e limitações de ferramentas como Turnitin. Nenhum indicador será tratado como prova isolada de autoria. |
| 03:00–03:20 | 20 min | Discussão de decisões: quando prosseguir, sanitizar, usar apenas ambiente autorizado ou interromper e consultar o responsável institucional. |
| 03:20–03:30 | 10 min | Síntese, avaliação rápida e entrega dos artefatos. |

**Conferência de carga horária:** 15 + 20 + 30 + 10 + 40 + 10 + 30 + 25 + 20 + 10 = **210 minutos**.

## Conteúdo didático — visão introdutória de uma LLM

Usando o [Transformer Explainer](https://poloclub.github.io/transformer-explainer/), o instrutor acompanha com a turma o caminho simplificado de uma entrada de texto até a geração:

1. **Tokenização:** o texto é dividido em unidades chamadas *tokens*, que podem corresponder a palavras ou partes de palavras. O modelo processa essas unidades, não “lê” a frase exatamente como uma pessoa.
2. **Representação e posição:** cada token é convertido em um vetor numérico (*embedding*); informação posicional ajuda o modelo a representar a ordem dos tokens.
3. **Self-attention:** em cada bloco Transformer, os tokens combinam contexto uns dos outros. A analogia de consulta, chave e valor (Q, K e V) ajuda a visualizar quais partes do contexto influenciam a representação. Múltiplas cabeças podem aprender relações diferentes; camadas MLP transformam essas representações.
4. **Previsão do próximo token:** a saída produz uma distribuição de probabilidades sobre tokens possíveis. Um token é escolhido conforme o método de geração e os parâmetros disponíveis; ele é acrescentado ao contexto e o processo se repete até a resposta terminar.
5. **Limites práticos:** prever uma continuação provável não garante que ela seja verdadeira, atual ou fundamentada em norma. A resposta pode soar convincente e ainda conter erros; por isso, documentos e legislação precisam ser conferidos em fontes autorizadas e decisões permanecem sob responsabilidade humana.

**Microexercício da demonstração (8 minutos, incluído no bloco 00:15–00:35):** observar a divisão de uma frase neutra em tokens; seguir visualmente como o contexto é processado; depois alterar a frase ou sua instrução e comparar a continuação. Em grupo, apontar por que uma continuação plausível não constitui evidência factual. Usar somente textos genéricos, nunca informações pessoais ou documentos institucionais.

**Nota didática:** a visualização apresenta o GPT-2 pequeno como exemplo interativo dos componentes de um Transformer. É um recurso para compreender conceitos, não uma descrição completa de todas as arquiteturas, escalas, ferramentas ou mecanismos de segurança usados pelas LLMs atuais.

## Critérios de conclusão

O grupo entrega documento de teste sanitizado, checklist e nota breve sobre riscos residuais. A sanitização não deve ser apresentada como garantia de anonimização nem como autorização automática para enviar dados a qualquer serviço.

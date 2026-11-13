---
name: Acervo
description: Índice pessoal para guardar páginas e consultar coleções.
colors:
  ink: "#24251f"
  muted: "#5c5d55"
  paper: "#f7f6f1"
  sidebar: "#eeede6"
  surface: "#fffefa"
  line: "#d8d6cc"
  accent: "#bd3e31"
  accent-hover: "#9f3027"
  accent-ink: "#ffffff"
  soft: "#e8e4db"
  placeholder: "#62635c"
  dark-ink: "#eeece4"
  dark-muted: "#c1beb4"
  dark-paper: "#191a18"
  dark-sidebar: "#22231f"
  dark-surface: "#242521"
  dark-line: "#494840"
  dark-accent: "#e46a58"
  dark-accent-hover: "#f07b68"
  dark-accent-ink: "#211915"
  dark-soft: "#34332d"
  dark-placeholder: "#c2bfb4"
typography:
  title:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: "1.85rem"
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "-0.025em"
  section-title:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 620
  sidebar-brand:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: "1.08rem"
    fontWeight: 650
    letterSpacing: "-0.02em"
  body:
    fontFamily: "IBM Plex Sans, sans-serif"
  label:
    fontFamily: "IBM Plex Sans, sans-serif"
    fontSize: "0.93rem"
rounded:
  control: "3px"
spacing:
  sidebar-x: "1.2rem"
  sidebar-y: "1.6rem"
  content-top: "2.3rem"
  content-x: "3rem"
  button-x: "0.85rem"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    rounded: "{rounded.control}"
    height: "42px"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "42px"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    height: "46px"
  collection-selected:
    backgroundColor: "transparent"
    textColor: "{colors.accent}"
    padding: "0 0.35rem"
---

# Design System: Acervo

## Overview

**Creative North Star: “Índice de leitura.”**

Acervo organiza a pesquisa pessoal como um catálogo de consulta: navegação compacta na lateral, conteúdo no centro e divisores finos para separar grupos. A interface em português mantém captura e conversa à vista, com a coleção ativa identificável sem competir com a leitura.

Papel quente e tinta escura sustentam a leitura nos dois temas; o vermelho funciona como índice para a seção ativa e ações principais. A marca existente é um livro aberto. A linguagem evita ornamentos e referências visuais japonesas.

**Key Characteristics:**
- Organização de catálogo com listas simples e linhas divisórias.
- Tinta e superfícies de baixo contraste decorativo; um vermelho de ação.
- Controles compactos, estados claros e leitura em IBM Plex Sans.

## Colors

A paleta usa papel e tinta como base nos dois temas, reservando o vermelho para seleção, foco e ação principal.

### Primary
- **Vermelho de índice** (`{colors.accent}`): seção ativa, controle primário, foco e seleção da coleção.
- **Vermelho de interação** (`{colors.accent-hover}`): hover dos controles primários.

### Neutral
- **Tinta** (`{colors.ink}`): texto principal no tema claro.
- **Cinza de apoio** (`{colors.muted}`): legendas e instruções secundárias.
- **Papel** (`{colors.paper}`): fundo principal claro.
- **Papel lateral** (`{colors.sidebar}`): superfície da navegação lateral.
- **Superfície clara** (`{colors.surface}`): campos e menus.
- **Linha** (`{colors.line}`): divisores e bordas de controles.
- **Superfície suave** (`{colors.soft}`): hover neutro e alertas.
- **Texto de placeholder** (`{colors.placeholder}`): texto de exemplo nos campos.
- **Tinta escura** (`{colors.dark-ink}`): texto principal no tema escuro.
- **Cinza escuro de apoio** (`{colors.dark-muted}`): textos secundários no tema escuro.
- **Papel noturno** (`{colors.dark-paper}`): fundo principal escuro.
- **Lateral noturna** (`{colors.dark-sidebar}`): superfície da navegação escura.
- **Superfície noturna** (`{colors.dark-surface}`): campos e mensagens no tema escuro.
- **Linha noturna** (`{colors.dark-line}`): bordas e divisores escuros.
- **Coral de índice** (`{colors.dark-accent}`): seleção e ação no tema escuro.
- **Coral de interação** (`{colors.dark-accent-hover}`): hover de ações escuras.
- **Tinta do coral** (`{colors.dark-accent-ink}`): texto sobre o coral escuro.
- **Superfície escura suave** (`{colors.dark-soft}`): hover neutro e alertas escuros.
- **Placeholder noturno** (`{colors.dark-placeholder}`): texto de exemplo nos campos escuros.

**A Regra do Índice.** O vermelho comunica seleção, foco ou ação; não crie uma segunda cor de destaque.

## Typography

**Display Font:** IBM Plex Sans (`sans-serif`, incorporada localmente como WOFF2)
**Body Font:** IBM Plex Sans (`sans-serif`)
**Label/Mono Font:** IBM Plex Sans (sem fonte mono distinta)

**Character:** A mesma família sustenta títulos, texto, navegação e controles. O contraste vem de peso, escala e cor, mantendo o conteúdo direto e legível.

### Hierarchy
- **Título da tarefa** (650 solicitado, `1.85rem`, line-height `1.2`): título principal de cada modo.
- **Título de estado** (620 solicitado, `1.35rem`): instruções e estados vazios.
- **Marca lateral** (650 solicitado, `1.08rem`, letter-spacing `-0.02em`): nome Acervo na lateral.
- **Corpo** (IBM Plex Sans, tamanho base do Streamlit): texto de conversa, parágrafos e conteúdo.
- **Rótulo** (IBM Plex Sans, `0.93rem`): rótulos dos campos.

A folha define pesos 650 e 620 em alguns seletores, mas os arquivos locais disponíveis cobrem 400, 500 e 600; o navegador escolhe a face disponível mais próxima. A família está embutida pela aplicação a partir de `assets/fonts`.

## Layout

Em telas largas, a navegação do Streamlit ocupa uma lateral fixa e a área principal usa um contêiner de até `1120px`, com `2.3rem` no topo e `3rem` nas laterais. A lateral agrupa marca, modos, coleções e tema em listas separadas por linhas. A área principal mostra a tarefa atual, com estados vazios alinhados ao início do conteúdo; a conversa limita os estados introdutórios a `42rem`.

Até `800px`, o conteúdo principal reduz o recuo lateral para `1rem` e o topo para `1.5rem`. A lateral segue o comportamento responsivo nativo do Streamlit. O ritmo usa grupos verticais de `1.2rem` e espaçamento generoso entre blocos; mantenha texto e controles compactos sem reduzir a tipografia legível.

## Elevation & Depth

A interface é plana. Não há sombras próprias: separadores, bordas finas e diferenças tonais entre papel, lateral e superfície definem os planos. Não adicione sombras decorativas.

## Shapes

Campos e botões usam cantos quase retos (`3px`). Coleções são linhas de lista com divisor inferior e marcador circular; a seleção troca o marcador para vermelho e sublinha a linha em vermelho. Divisores são finos e seguem a cor de linha do tema.

## Components

### Botões
Controles de navegação são compactos e mudam pela superfície e pela cor de estado.
- **Primário:** preenchimento vermelho, texto de alto contraste, altura mínima `42px` e cantos de `3px`.
- **Hover / foco:** hover escurece a ação no tema claro; foco visível usa contorno vermelho de `3px` com deslocamento de `2px`.
- **Secundário:** transparente, contorno de linha, texto de tinta; hover recebe superfície suave.
- **Navegação ativa:** preenchimento vermelho sólido na seção ativa, inclusive no tema escuro com o coral do tema.

### Campos
Campos usam superfície correspondente ao tema, borda fina e cantos de `3px`; altura mínima observada de `46px`. O foco visível recebe contorno vermelho de `3px`, afastado `2px`. O formulário de captura começa após divisor superior.

### Navegação
A lateral começa com a marca do livro e “Acervo”, seguida da identificação pessoal, dos modos, das coleções e do controle de tema. Os modos são botões de largura total. A coleção ativa mantém fundo transparente e recebe texto, marcador e divisor inferior em vermelho.

### Conversa
Mensagens aparecem sem cartão elevado, em linhas com divisor inferior e padding vertical de `1rem`. O estado vazio usa uma linha superior, texto introdutório e largura máxima de `42rem`; o campo de pergunta acompanha o tema.

## Do's and Don'ts

### Do:
- **Do** mantenha IBM Plex Sans; os arquivos locais suportam pesos 400, 500 e 600.
- **Do** use vermelho para seleção, foco e ação principal; adapte ao valor do tema atual.
- **Do** separe grupos da lateral com linhas finas e mantenha a coleção ativa reconhecível.
- **Do** preserve cantos discretos de `3px` nos campos e botões.
- **Do** respeite `prefers-reduced-motion`; as transições de botões são removidas quando solicitado.

### Don't:
- **Don't** adicione outras cores de destaque ou sombras decorativas.
- **Don't** arredonde os controles em pílulas ou cartões volumosos.
- **Don't** use ilustração decorativa, clichês visuais japoneses ou escrita ornamental.
- **Don't** desloque controles no hover; a interação observada altera cor e borda.

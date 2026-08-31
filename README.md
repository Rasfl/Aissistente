# Agente de Programação IA em Python

Agente de programação autônomo em Python, capaz de interpretar instruções em linguagem natural e utilizar ferramentas locais para investigar, executar e modificar código.

Como demonstração prática, o projeto atua sobre uma calculadora em Python, analisando o código, executando testes e corrigindo bugs reais, incluindo problemas de precedência de operadores matemáticos.

## Funcionalidades

O agente foi projetado para operar dentro de um diretório controlado, com acesso a um conjunto limitado de ferramentas locais que simulam o fluxo de trabalho de um assistente de engenharia de software.

Entre as principais capacidades estão:

- **Listar arquivos e diretórios** para mapear a estrutura disponível.
- **Ler o conteúdo de arquivos** para entender a lógica do projeto.
- **Executar arquivos Python** para validar comportamentos, reproduzir erros e inspecionar saídas.
- **Escrever e atualizar arquivos** com correções ou alterações propostas pelo agente.

## Tecnologias utilizadas

- **Python**: linguagem principal do projeto e do ambiente de execução do agente.
- **UV**: gerenciador de dependências e execução utilizado no projeto.
- **Provedor de LLM / API**: integração com um modelo de linguagem para interpretar solicitações e decidir o uso das ferramentas locais.

## Instalação e configuração

Certifique-se de ter o Python e o [uv](https://docs.astral.sh/uv/) instalados na máquina.

Clone o repositório e, na raiz do projeto, sincronize as dependências com:

```bash
uv sync
```

## Variáveis de ambiente

O agente precisa de uma chave de API para se comunicar com o provedor de modelo de linguagem. Crie um arquivo `.env` na raiz do projeto com a variável esperada pela sua implementação.

Exemplo genérico:

```env
OPENAI_API_KEY=sua_chave_de_api_aqui
```

> **Importante:** o nome da variável pode variar conforme o provedor ou a configuração usada no projeto.

## Como executar

Para iniciar o agente, execute o arquivo principal com o `uv`, passando a instrução desejada como argumento:

```bash
uv run main.py "Sua instrução aqui"
```

Também é possível utilizar a flag de modo detalhado, quando disponível na implementação:

```bash
uv run main.py "Sua instrução aqui" --verbose
```

## Exemplos de uso

Analisar o comportamento da calculadora:

```bash
uv run main.py "Explique como a calculadora renderiza os resultados no console."
```

Investigar e corrigir um bug:

```bash
uv run main.py "Existe um bug de precedência de operadores matemáticos na calculadora. Analise os testes, investigue a causa e corrija o problema."
```

## Estrutura do projeto

```text
/
├── calculator/
│   ├── main.py
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── functions/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── main.py
├── config.py
├── prompts.py
├── call_function.py
└── pyproject.toml
```

### Organização dos diretórios

- `calculator/`: projeto de demonstração usado como alvo de análise e correção pelo agente.
- `functions/`: módulos que expõem as ferramentas locais disponíveis para o agente.
- `main.py`: ponto de entrada da aplicação.
- `call_function.py`: camada responsável por mapear e executar as ferramentas disponíveis.
- `config.py`: configurações gerais do agente.
- `prompts.py`: definições relacionadas aos prompts utilizados.
- `pyproject.toml`: arquivo de configuração de dependências e execução com UV.

## Limitações e segurança

Este projeto concede ao agente acesso a leitura, execução e escrita de arquivos locais. Por isso, ele deve ser executado apenas em ambientes controlados, como diretórios de teste, containers ou máquinas virtuais.

Recomenda-se utilizar permissões restritas e evitar qualquer uso em pastas com arquivos sensíveis ou dados importantes. Como o agente pode tomar decisões iterativas com base na instrução recebida, o acompanhamento da execução é essencial para manter o uso dentro de um escopo seguro.

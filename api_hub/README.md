API Hub - Plataforma Unificada de Integração de APIs

Um hub CLI leve para explorar e integrar múltiplas APIs públicas em uma única interface amigável ao usuário. Construído com Python e a biblioteca Rich para bela saída em terminal.

Recursos Principais

O API Hub fornece acesso a três integrações diferentes de APIs:

1. Gemini IA (Google)
   - Chat interativo com assistente IA
   - Persistência de histórico de chat em armazenamento JSON
   - Suporte para análise de imagens e arquivos documento
   - Seleção configurável de modelo (Gemini 3 Flash, 2.5 Flash)
   - Sistema de memória de conversa (últimas 10 mensagens)

2. NASA - Imagem Astronômica do Dia
   - Obtenha imagens astronômicas diárias
   - Download automático em alta resolução
   - Validação de imagem e tratamento de erros
   - Armazenamento de nome de arquivo normalizado
   - Relatório de status

3. Dados do Mercado de Criptocorrências
   - Consultas de preços em tempo real via CoinGecko
   - Suporte para conversão multi-moeda (USD, BRL, EUR)
   - Rastreamento de alteração de preço 24h
   - Tratamento de erro limpo com mensagens amigáveis ao usuário

Pilha Tecnológica

- Python 3.8+
- google-genai - SDK do Google Gemini
- requests - Biblioteca cliente HTTP
- python-dotenv - Gerenciamento de variáveis de ambiente
- rich - Estilo de UI de terminal e formatação
- pyfiglet - Geração de banner de arte ASCII
- Pillow - Processamento de imagens

Estrutura do Projeto

Layout dos diretórios:

main.py                      # Ponto de entrada com menu principal e navegação
gemini_agent.py             # Integração da API Gemini com chat e memória
nasa.py                      # Integração da API NASA com download de imagens
cripto.py                    # API de criptocorrência CoinGecko
memoria.json                # Armazenamento de histórico de chat (auto-gerado)
.env                        # Arquivo de configuração com chaves de API (não no repo)
images/                     # Diretório de imagens baixadas

Instalação e Configuração

Pré-requisitos:
- Python 3.8 ou superior
- gerenciador de pacotes pip

Passo 1: Clone e navegue para o diretório
```bash
git clone <repository-url>
cd api-hub
```

Passo 2: Crie um ambiente virtual (opcional mas recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

Passo 3: Instale as dependências
```bash
pip install -r requirements.txt
```

Passo 4: Configure as variáveis de ambiente
Crie um arquivo `.env` no diretório raiz com:
```
GEMINI=sua_chave_de_api_google_gemini
NASA=sua_chave_de_api_nasa
```

Passo 5: Execute a aplicação
```bash
python main.py
```

Obtendo Chaves de API

A plataforma usa duas APIs que requerem autenticação:

API Gemini:
- Visite: https://aistudio.google.com/apikey
- Selecione ou crie um projeto
- Gere uma nova chave de API
- Copie e cole no arquivo .env

API NASA:
- Visite: https://api.nasa.gov/
- Preencha o formulário de registro simples
- A chave de API será enviada para seu email
- Copie e cole no arquivo .env

Guia de Uso

```bash
python main.py
```

O menu interativo oferece as seguintes opções:

Navegação do Menu Principal:
1. API Gemini - Converse com IA, analise arquivos
2. API NASA - Obtenha imagens astronômicas diárias
3. Mercado Financeiro - Consulte preços de criptocurrências

Variáveis de Ambiente Obrigatórias:
- `GEMINI`: Chave de API Google Gemini (obrigatória para recursos Gemini)
- `NASA`: Chave de API NASA (obrigatória para recursos NASA)

O módulo de criptocorrências não requer autenticação.

Usando Chat Gemini

Opções:
1) Chat - Conversa única ou contínua
   - Selecione o estilo de conversa (prompt único ou com memória)
   - Selecione a versão do modelo IA
   - Digite sua mensagem
   - Obtenha respostas formatadas com suporte a Markdown

2) Chat com Arquivo - Analise imagens ou documentos
   - Forneça contexto de mensagem
   - Envie arquivo de imagem ou documento
   - IA analisa e responde
   - Suporta JPG, PNG, GIF, WEBP (imagens) e documentos

Usando API de Criptocorrência

1. Selecione criptocorrência (bitcoin, ethereum, solana, etc.)
2. Escolha moeda de destino (usd, brl, eur)
3. Veja preço em tempo real e alteração de 24h
4. Faça novas consultas ou retorne ao menu principal
   - Restructured menu system with proper navigation
   - Added separate handler functions for each API
   - Implemented proper error handling
   - Made interface language English
   - Simplified color scheme
   - Added table rendering for repositories

2. gemini_agent.py Refactoring:
   - Converted to class-based architecture (GeminiAgent)
   - Broke down large function into smaller, testable methods
   - Added comprehensive logging with Python logging module
   - Implemented proper error handling for each operation
   - Removed hardcoded model - moved to configuration
   - Added detailed docstrings and type hints
   - Separated concerns: API calls, history management, UI
   - Added file type detection for image vs document handling
   - Implemented clear_history() method

3. nasa.py Improvements:
   - Added error handling for network failures
   - Implemented file type validation (content-type checking)
   - Normalized filenames with timestamps
   - Added file size reporting
   - Proper exception handling for JSON parsing
   - Timeout configuration for requests
   - Better status reporting

4. cripto.py Improvements:
   - Refactored to return structured dictionary
   - Added "if __name__ == '__main__'" guard
   - Improved error handling with try-except blocks
   - Removed print statements in favor of returns
   - Added extended currency symbol support
   - Better API response validation
   - Proper exception logging

5. Code Removal:
   - Removed gemini_terminal_chat.py (duplicate code)
   - Eliminated code duplication across modules
   - Simplified codebase maintenance

6. New API Modules Added:
   - github_api.py - Trending repos and user info
   - quotes_api.py - Random quotes and search
   - random_users_api.py - User profile generation
   - cat_api.py - Cat images and facts

Visual and UX Improvements:

- Simplified color scheme (blue borders instead of neon)
- English language interface
- Consistent menu formatting
- Better error messages with red highlighting
- Status reporting and confirmation messages
- Table-based display for multiple results
- Proper panel formatting for all outputs

Dependencies

The project requires the following Python packages:

google-genai>=0.3.0          # Google Gemini API
requests>=2.31.0             # HTTP requests
python-dotenv>=1.0.0         # Environment variable management
pillow>=10.0.0               # Image processing
pyfiglet>=0.8                # ASCII art
rich>=13.0.0                 # Terminal formatting

Install all dependencies:
bash
pip install google-genai requests python-dotenv pillow pyfiglet rich

Troubleshooting

Common Issues:

1. "GEMINI API key not found"
   Solution: Ensure your .env file contains GEMINI=your_key_here

2. "NASA API key not found"
   Solution: Ensure your .env file contains NASA=your_key_here

3. Image download fails from NASA
   Solution: Check internet connection, verify API key is valid

4. Chat history not persisting
   Solution: Verify memoria.json is writable in the project directory

5. Import errors for API modules
   Solution: Ensure all Python packages are installed (pip install -r requirements.txt)

Performance Notes

- Chat history is limited to 10 messages for context window optimization
- Cryptocurrency queries are cached by CoinGecko (can take 1-2 minutes to update)
- NASA image downloads depend on internet speed
- GitHub API is rate-limited to 60 requests per hour without authentication

Future Enhancements

Potential improvements for future versions:

1. Database integration for longer chat history retention
2. User authentication and personal conversation threads
3. Advanced search filters for repositories and cryptocurrencies
4. Image cache system to avoid redundant downloads
5. Voice interface support
6. Statistical dashboards and analytics
7. Batch operations for multiple queries
8. API response caching layer

Contributing

Contributions are welcome! Areas for improvement:

1. Additional API integrations
2. Enhanced error handling
3. Performance optimizations
4. Test coverage
5. Documentation improvements
6. UI/UX enhancements

Development Setup:

bash
git clone <repository-url>
cd api-hub
python3.13 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

License

This project is open source and available for personal and educational use.

Support

For issues, questions, or suggestions:
1. Check the Troubleshooting section
2. Review ANALISE_TECNICA.md for detailed code analysis
3. Check GUIA_NOVAS_APIS.md for implementation examples

Version Information

Current Version: 1.0.0
Last Updated: April 2026
Python Version: 3.13+
Compatible Platforms: Linux, macOS, Windows

Status: Production Ready - All core features functional and tested

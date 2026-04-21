# API Hub - Integrador Criativo de APIs

Um hub interativo que integra múltiplas APIs com o objetivo de **incentivar a criatividade e experimentação com técnicas de REST API**. Este projeto é um espaço aberto para aprender, explorar e estender integrações com novas APIs!

> **Philosophia**: Código livre para adaptar, modificar e estender. Construa seu próprio "Claude Code" criando funções personalizadas para qualquer API que você desejar integrar!



## DEMO - Gemini API
<div align="center">
  <img src="download.gif" />
</div>

---
## Recursos Principais

O API Hub fornece acesso a quatro integrações prontas, mas você pode adicionar quantas quiser:

### 1. Chat com Gemini AI (Google)
- Chat interativo com assistente IA poderoso
- Persistência de histórico de chat em JSON
- Suporte para análise de imagens e documentos
- Seleção de modelo configurável (Gemini 2.0 Flash, 1.5 Flash)
- Sistema inteligente de memória (últimas 10 mensagens)
- **Extensível**: Crie seus próprios prompts e personas de IA

### 2. NASA - Imagem Astronômica do Dia
- Obtenha imagens astronômicas diárias em alta resolução
- Download automático com validação
- Tratamento robusto de erros
- Organização inteligente de arquivos
- **Extensível**: Integre outras APIs da NASA além do APOD

### 3. Dados de Mercado de Criptocorrências
- Consultas de preços em tempo real via CoinGecko (100% gratuito)
- Conversão multi-moeda (USD, BRL, EUR e mais)
- Rastreamento de variações 24h
- Sem necessidade de chave de API!
- **Extensível**: Adicione análises técnicas, alertas de preço, histórico

### 4. Informações de Países
- Pesquise as informações gerais de qualquer país
- Consulta via nome ou linguagem
- Sem necessidade de chave de API!
---

## Stack Tecnológico

```
Python 3.8+ (recomendo fortemente usar o python 3.13)
├── google-genai         # SDK Google Gemini
├── requests            # Requisições HTTP
├── python-dotenv       # Gerenciamento de variáveis de ambiente
├── rich                # UI formatada para terminal
├── pyfiglet            # Banners ASCII art
└── Pillow              # Processamento de imagens
```

---

## Estrutura do Projeto

```
api-hub/
├── main.py                 # Ponto de entrada com menu principal
├── gemini_agent.py         # Integração Gemini + Chat
├── nasa.py                 # Integração NASA APOD
├── cripto.py               # Integração CoinGecko
├── memoria.json            # Histórico de chat (auto-gerado)
├── requirements.txt        # Dependências
├── .env                    # Chaves de API (não versionado)
├── .env.example            # Modelo de configuração
├── images/                 # Imagens baixadas
└── README.md              # Este arquivo
```

---

## Como Usar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conexão com internet

### 1. Instalação Inicial

```bash
# Clone ou baixe o repositório
git clone "https://github.com/twichhs/api-hub.git"

# Crie um virtual environment (recomendado)
python -m venv venv

#linux e mac:
source venv/bin/activate  
#windows: 
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração de Chaves de API (Gratuitas!)

Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

#### **Google Gemini API** (Gratuito com limite)
1. Acesse [Google AI Studio](https://aistudio.google.com/)
2. Clique em "Get API Key"
3. Crie uma nova chave
4. Copie a chave para seu `.env`:
   ```
   GEMINI_API_KEY=sua_chave_aqui
   ```
   
Limite gratuito: 15 requisições por minuto

---

#### **NASA API** (Totalmente Gratuito)
1. Visite [NASA API Portal](https://api.nasa.gov/)
2. Preencha o formulário simples
3. Você receberá uma chave por email
4. Adicione ao `.env`:
   ```
   NASA_API_KEY=sua_chave_aqui
   ```

Limite gratuito: 50 requisições por hora

---

#### **CoinGecko API** (100% Sem chave!)
- Não requer chave de API
- Gratuito
- Sem autenticação necessária
- Nenhuma configuração extra necessária!

---

### 3. Executar o Programa

```bash
python main.py
```

Você verá um menu interativo com as opções:
```
=== API HUB ===
1. Chat com Gemini AI
2. Imagem Astronômica do Dia (NASA)
3. Preços de Criptocorrências
0. Sair

Escolha uma opção:
```

---

## Exemplos de Uso

### Chat com Gemini
```python
from gemini_agent import GeminiAgent

agent = GeminiAgent()
resposta = agent.chat("Explique a teoria da relatividade")
print(resposta)
```

### Imagem NASA
```python
from nasa import buscar_imagem_do_dia

imagem_info = buscar_imagem_do_dia()
# Faz download automático e salva em images/
```

### Preço de Cripto
```python
from cripto import obter_preco_cripto

preco = obter_preco_cripto("bitcoin", "brl")  # Bitcoin em Reais
print(f"Bitcoin: R$ {preco}")
```

---

## Como Estender: Construa Seu Próprio!

Adoramos a ideia e **encorajamos vigorosamente** a extensão deste projeto! Aqui estão algumas ideias:

### Ideias de Novas APIs para Integrar:

#### 1. **OpenWeatherMap** - Dados Meteorológicos
```python
# weather.py (SUA IMPLEMENTAÇÃO)
def obter_clima(cidade):
    # Chame a API OpenWeatherMap
    # Processe e retorne dados formatados
    pass
```
Plano Gratuito: 60 chamadas/minuto

#### 2. **Spotify** - Informações de Música
```python
# spotify_agent.py (SUA IMPLEMENTAÇÃO)
def buscar_musica(artista, musica):
    # Integre com Spotify Web API
    # Retorne informações de áudio
    pass
```

#### 3. **GitHub REST API** - Dados de Repositórios
```python
# github_agent.py (SUA IMPLEMENTAÇÃO)
def obter_repositorio(usuario, repo):
    # Busque estrelas, forks, issues
    pass
```
Sem necessidade de autenticação para leitura básica!

#### 4. **IP Geolocalização** - Dados de Localização
```python
# geo_agent.py (SUA IMPLEMENTAÇÃO)
def obter_localizacao_ip(ip):
    # Use API de geolocalização gratuita
    pass
```

#### 5. **Quotes API** - Citações Aleatórias
```python
# quotes_agent.py (SUA IMPLEMENTAÇÃO)
def obter_citacao_aleatoria():
    # 100% gratuito, sem chave necessária
    pass
```

---

### Passo a Passo: Criar Sua Própria Integração

1. **Crie um novo arquivo** (ex: `sua_api.py`)
2. **Implemente as funções** de integração
3. **Adicione ao menu principal** em `main.py`
4. **Importe no início** do arquivo
5. **Adicione uma opção** no menu
6. **Teste** e divirta-se!

**Exemplo básico:**

```python
# nova_api.py
import requests

def funcao_custom_api():
    """Sua integração com uma API nova"""
    url = "https://api-example.com/endpoint"
    resposta = requests.get(url)
    return resposta.json()
```

---

## Recursos Gratuitos Recomendados

| API | Propósito | Limite Gratuito | Chave? |
|-----|-----------|-----------------|--------|
| **Google Gemini** | IA Conversacional | 15 req/min | Sim |
| **NASA** | Imagens & Dados Espaciais | 50 req/hora | Sim |
| **CoinGecko** | Criptocorrências | Ilimitado | Não |
| **OpenWeatherMap** | Clima | 60 req/min | Sim |
| **JSONPlaceholder** | API Fake (Teste) | Unlimited | Não |
| **REST Countries** | Dados de Países | Unlimited | Não |
| **HTTPCat** | Status HTTP com Gatos | Unlimited | Não |

---

## Contribuindo

Este projeto **acebe colaborações**! Ideias para contribuir:

- Adicione novas integrações de API
- Melhore a interface do terminal
- Adicione testes unitários
- Documente suas extensões
- Compartilhe suas ideias criativas!

**Tudo é permitido - código é livre e para adaptar como desejar!**

---

## Licença

MIT License - Use, modifique e distribua livremente!

---

## Filosofia do Projeto

> Este projeto é um **playground para aprender APIs**. 
> Encorajo você a:
> - Quebrar coisas (e consertar)
> - Experimentar técnicas novas
> - Remixar o código
> - Construir suas próprias soluções
> - **Compartilhar suas criações!**

---

## FAQ

**P: Preciso de experiência em APIs para usar?**
R: Não! Este projeto é educacional. Iniciantes são bem-vindos!

**P: Posso criar uma função comercial baseada nisso?**
R: Absolutamente! MIT License permite uso comercial.

**P: Como faço se ficar preso?**
R: Veja a documentação oficial de cada API ou consulte exemplos online.

---

## Próximos Passos

1. Configure suas chaves de API
2. Execute `python main.py`
3. Explore os recursos
4. **Crie sua própria integração**
5. Divirta-se e aprenda!

---

**Leonardo Barros !!!**

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

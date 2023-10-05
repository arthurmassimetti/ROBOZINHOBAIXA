# Automatização de Download de Documentos no D4SIGN

![Python Version](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
![Selenium Version](https://img.shields.io/badge/Selenium-3.141%2B-brightgreen)
![PyAutoGUI Version](https://img.shields.io/badge/PyAutoGUI-0.9%2B-brightgreen)

Este projeto é uma automação para baixar arquivos do D4SIGN e organizá-los em uma pasta específica ou armazená-los em um banco de dados, utilizando as bibliotecas Python PyAutoGUI e Selenium.

## Funcionalidades

- **Login Automatizado**: Utilizando o Selenium, o script automatiza o processo de login na plataforma D4SIGN, garantindo acesso aos documentos.

- **Download Automático**: Usando o PyAutoGUI, o projeto simula cliques do mouse e atalhos do teclado para navegar até os arquivos no D4SIGN e baixá-los automaticamente para o seu sistema.

- **Organização de Arquivos**: Após o download, os arquivos podem ser organizados em pastas específicas com base em critérios como nome, data ou tipo de documento.

- **Integração com Banco de Dados**: Os detalhes dos documentos baixados podem ser automaticamente inseridos em um banco de dados para registro e referência futura.

## Como Usar

1. **Configuração do Ambiente**:
   - Certifique-se de ter Python 3.8+ instalado.
   - Instale as bibliotecas necessárias com `pip install -r requirements.txt`.
   
2. **Execução do Script**:
   - Execute o script principal: `python download_d4sign.py`.
   - Siga as instruções interativas para fazer login, baixar documentos e escolher a opção de organização.

3. **Organização de Arquivos**:
   - Se você optar por organizar os arquivos, configure os critérios no arquivo `organize_files.py`.

4. **Integração com Banco de Dados**:
   - Se você escolher integrar com um banco de dados, configure a conexão no arquivo `database.py`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, propor melhorias ou enviar pull requests.



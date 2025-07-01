# Monitoramento Automático de Vendas Roblox - TheVoid Studio

Este projeto automatiza o monitoramento dos fundos da comunidade e dos Robux pendentes em uma página do Roblox, utilizando técnicas de OCR (Reconhecimento Óptico de Caracteres) para extrair informações diretamente da tela e enviá-las para um canal do Discord via webhook. O objetivo é fornecer atualizações periódicas e automáticas sobre o saldo de Robux, facilitando o acompanhamento em tempo real sem a necessidade de intervenção manual.

## Funcionalidades

- **Captura automática da tela:** Utiliza o `ImageGrab` para capturar a tela inteira do computador, garantindo que todas as informações visuais estejam disponíveis para análise.
- **Reconhecimento de texto (OCR):** O `pytesseract` interpreta a imagem capturada e converte o conteúdo visual em texto, permitindo a extração dos valores de Robux.
- **Extração robusta de valores:** O script procura por diversas variações de palavras-chave relacionadas a "fundos da comunidade" e "robux pendentes", tornando o reconhecimento mais tolerante a erros do OCR e variações na interface.
- **Automação de navegador:** Com o `pyautogui`, o script garante que o navegador esteja em foco e recarrega a página automaticamente antes de cada captura, aumentando a confiabilidade dos dados extraídos.
- **Envio automatizado para Discord:** Os dados extraídos são formatados em um embed e enviados para um canal do Discord via webhook, proporcionando notificações organizadas e visuais.
- **Agendamento periódico:** Utiliza o `schedule` para executar o monitoramento a cada 5 minutos, mantendo as informações sempre atualizadas.

## Como Funciona

1. **Preparação:** O script aguarda alguns segundos para que o usuário posicione o navegador e o Discord corretamente na tela.
2. **Automação:** A cada 5 minutos, o navegador é recarregado automaticamente (ALT+F5) e a tela é capturada.
3. **Processamento:** O texto é extraído da imagem usando OCR, e os valores de interesse são identificados por meio de expressões regulares e palavras-chave.
4. **Notificação:** Um embed é montado e enviado para o Discord, contendo os valores atuais dos fundos da comunidade e dos Robux pendentes.
5. **Loop contínuo:** O processo se repete indefinidamente, garantindo monitoramento constante.

## Requisitos

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado e configurado
- Bibliotecas Python: `pytesseract`, `Pillow`, `schedule`, `requests`, `pyautogui`, `re`
- Webhook do Discord configurado

## Instalação

1. Instale o Tesseract OCR e ajuste o caminho no script conforme necessário.
2. Instale as dependências Python:
    ```bash
    pip install pytesseract pillow schedule requests pyautogui
    ```
3. Configure o webhook do Discord no campo `WEBHOOK_URL`.
4. Execute o script e siga as instruções do terminal para posicionar o navegador e o Discord.

## Observações

- O script depende da posição do navegador e do Discord na tela. Certifique-se de que estejam visíveis e acessíveis conforme indicado.
- O reconhecimento de texto pode variar conforme a resolução da tela e a qualidade da interface. Ajuste as palavras-chave se necessário.
- Para uso em outros sistemas operacionais, adapte os caminhos e comandos conforme necessário.

---

**Desenvolvido por Alvaroo para automação e monitoramento de vendas Roblox.**
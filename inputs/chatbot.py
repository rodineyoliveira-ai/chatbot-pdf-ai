# Exemplo didático de como o chatbot poderia funcionar

import numpy as np

# Simulação de embeddings (representações numéricas dos textos)
base_conhecimento = {
    "engenharia de software": "Área que estuda o desenvolvimento de sistemas.",
    "chatbot": "Assistente virtual que responde perguntas com base em IA.",
    "embeddings": "Representações numéricas que permitem comparar textos."
}

def responder(pergunta):
    for chave, conteudo in base_conhecimento.items():
        if chave in pergunta.lower():
            return conteudo
    return "Desculpe, não encontrei uma resposta nos documentos."

print(responder("O que é engenharia de software?"))

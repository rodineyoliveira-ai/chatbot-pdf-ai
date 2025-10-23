# Chatbot Baseado em PDFs

Este projeto simula a criação de um chatbot inteligente que responde com base no conteúdo de arquivos PDF.  
Ele foi desenvolvido como parte do desafio da **Digital Innovation One (DIO)** sobre IA generativa e embeddings.

---

##  Objetivo

O objetivo é demonstrar o funcionamento básico de um sistema que:
- Carrega e processa PDFs 
- Cria vetores (embeddings) com base no conteúdo 
- Usa busca vetorial para encontrar respostas relevantes 
- Gera respostas contextuais utilizando modelos de linguagem 

---

##  Estrutura do Projeto
chatbot-pdf-ai/
│
├── inputs/
│ └── exemplo.txt # Simulação de conteúdo de PDFs
│
├── README.md # Explicação e documentação do projeto

---

##  Como o sistema funcionaria

1. **Leitura dos PDFs:** o conteúdo dos documentos é extraído (usando bibliotecas como `PyPDF2` ou `pdfplumber`);
2. **Criação dos embeddings:** cada parágrafo é convertido em vetor numérico (usando `OpenAI Embeddings`, `SentenceTransformers`, etc.);
3. **Busca vetorial:** quando o usuário faz uma pergunta, o sistema encontra os trechos mais parecidos com a consulta;
4. **Resposta gerada:** o modelo de linguagem (por exemplo, GPT) usa esses trechos como contexto para formular uma resposta precisa.

---

##  Exemplo de funcionamento

**Pergunta:**  
> O que é engenharia de software?

**Resposta esperada:**  
> Engenharia de software é a área que estuda métodos sistemáticos de desenvolvimento e manutenção de sistemas.

---

##  Tecnologias sugeridas

- Python 
- LangChain  
- OpenAI API  
- FAISS (Facebook AI Similarity Search)  
- Streamlit (para o chat interativo)  

---

##  Aprendizados

- Entendi como funcionam **embeddings** e **buscas vetorizadas**.  
- Percebi que é possível criar um chatbot com base em **conhecimento proprietário**, como PDFs pessoais.  
- Esse tipo de IA pode ser muito útil para estudos, empresas e atendimento automatizado.

---

## Prints e Demonstração

*(Aqui você pode adicionar prints do código, ou do fluxo explicativo, se quiser)*

---
📚 Projeto desenvolvido para o desafio da DIO - "Criando um Chatbot Baseado em PDFs"

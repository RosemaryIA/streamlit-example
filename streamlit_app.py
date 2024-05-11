import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# @title
!pip install nltk -q
!pip install spacy -q
!pip install tensorflow -q
# @title
from google.colab import userdata

#Configurações iniciais
import google.generativeai as genai  #as : designa um apelido para a biblioteca

api_key = userdata.get("SECRET_KEY")
#Configurações iniciais
genai.configure(api_key=api_key)


import nltk
import spacy
import tensorflow as tf  # Usando um alias 'tf' para TensorFlow
import nltk
import spacy
import tensorflow as tf  # Usando um alias 'tf' para TensorFlow

# Instalação (descomente as linhas se necessário)
# !pip install nltk
# !pip install textblob

# Importação
import nltk
from textblob import TextBlob

def chatbot_welovepizza():

  # Mensagens iniciais
  print("Olá! Agradecemos sua visita à WeLovePizza. Queremos saber sua opinião para melhorarmos ainda mais!")
  print("Respondendo a esta pesquisa rápida, você concorre a 3 vinhos de sua escolha dentre uma seleção especial. 🍷")
  print("Para conferir as opções, acesse este link: [Link para a carta de vinhos]\n")

  # Perguntas e opções de resposta
  perguntas = {
      "experiencia": "Em uma escala de 0 a 10, sendo 0 “nada satisfeito” e 10 “extremamente satisfeito”, como você avalia sua experiência geral com a WeLovePizza hoje?",
      "pontos_fortes": "O que você mais gosta na WeLovePizza? (Pode escolher mais de uma opção)\n a) Sabor das pizzas\n b) Variedade do cardápio\n c) Qualidade dos ingredientes\n d) Preço\n e) Atendimento\n f) Tempo de entrega\n g) Ambiente da loja\n h) Outro: __________",
      "pontos_a_desenvolver": "O que poderíamos melhorar na WeLovePizza? (Pode escolher mais de uma opção)\n a) Sabor das pizzas\n b) Variedade do cardápio\n c) Qualidade dos ingredientes\n d) Preço\n e) Atendimento\n f) Tempo de entrega\n g) Ambiente da loja\n h) Outro: __________",
      "frequencia_compra": "Nos últimos 3 meses, com que frequência você comprou pizzas?\n a) Somente na WeLovePizza\n b) Mais na WeLovePizza do que na concorrência\n c) Mais na concorrência do que na WeLovePizza\n d) Somente na concorrência",
      "sentimento": "Qual palavra melhor descreve o que você sente pela WeLovePizza?\n a) Satisfação\n b) Confiança\n c) Indiferença\n d) Frustração\n e) Outro: __________",
      "sugestoes": "Tem alguma sugestão para melhorarmos ainda mais?"
  }




#!/usr/bin/env python
# coding: utf-8

# # Problema
# 
# - Passo 1: Enviar informações de forma automatica do site Yahoo Finanças
# - Passo 2: Gerar análises
# - Passo 3: Enviar e-mail com os resultados da análie

# # Passo 1

# In[1]:


get_ipython().system('pip install yfinance')


# In[2]:


import yfinance


# In[15]:


ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker("PETR4.SA")

tabela = dados.history("6mo")
fechamento = tabela.Close

fechamento.plot()


# # Passo 2 - Gerar análises (últimos seis meses)
# 
# - Cotação máxima
# - Cotação mínima
# - Cotação atual

# In[19]:


maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

print(maxima)
print(minima)
print(atual)


# # Passo 3 - Enviar e-mail de forma automática
# 
# - Abrir uma nova aba no navegador
# - clicar no botão escrever
# - Preencher o destinatátio, assunto
# - Escrecer e-mail
# - Clicar em enviar

# In[20]:


get_ipython().system('pip install pyautogui')


# In[21]:


get_ipython().system('pip install pyperclip')


# In[23]:


import pyautogui
import pyperclip


# In[45]:


pyautogui.PAUSE = 2

pyautogui.hotkey("ctrl","t")
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ENTER")

pyautogui.click(x=770, y=207)

pyperclip.copy("felipefreitao@hotmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy("Análises diárias")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

mensagem = f"""Boa noite,
Seguem as análises dos últimos seis meses da ação {ticker}: 

Cotação maxima: R$ {round(maxima, 2)}
Cotação minima: R$ {round(minima, 2)}
Cotação atual: R$ {round(atual, 2)}

Qualquer dúvida, estou à disposição

Felipe
"""
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")

pyautogui.click(x=902, y=687)

    


# In[ ]:





# In[ ]:





# In[43]:


import time

time.sleep(5)
pyautogui.position()


# In[ ]:





# In[ ]:





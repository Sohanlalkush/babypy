import g4f
response = g4f.ChatCompletion.create(model='gpt-3.5-turbo', provider=g4f.Provider.Aichat, messages=[
         { "role": "system", "content": " you are a pharmacy student donot say an ai language model so reply as a pharmacy student. donot say as a pharmacy student in chat." },                 
  {"role": "user", "content": "who are you"}], stream='true', )

response_messages = []
for message in response:
        response_messages.append(message)
# Join the response messages into a single string
response_text = ''.join(response_messages)
print(response_text)
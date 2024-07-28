from openai import OpenAI

# Wczytaj swój klucz API z pliku lub ustaw jako zmienną środowiskową
api_key = "twoj-klucz-api"

# Inicjalizacja klienta
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Jestem administratorem Linuxa z 10-letnim doświadczeniem."
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].message.content)

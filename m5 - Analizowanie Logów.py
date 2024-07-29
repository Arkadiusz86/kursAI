import os
from openai import OpenAI

# Wczytaj swój klucz API z pliku lub ustaw jako zmienną środowiskową
api_key = "twoj-klucz-api"

# Inicjalizacja klienta
client = OpenAI(api_key=api_key)

# Lista do przechowywania historii konwersacji
conversation_history = [
    {"role": "system", "content": "Jesteś pomocnym asystentem AI."}
]

def add_content_to_conversation():
    print("Wklej zawartość pliku poniżej. Gdy skończysz, wpisz 'KONIEC' w nowej linii:")
    content = []
    while True:
        line = input()
        if line.strip().upper() == 'KONIEC':
            break
        content.append(line)
    file_content = "\n".join(content)
    conversation_history.append({"role": "user", "content": f"Oto zawartość pliku:\n\n{file_content}"})
    print("Dodano zawartość do konwersacji.")

print("Witaj w interaktywnym ChatGPT! Wpisz 'exit' aby zakończyć.")
print("Aby dodać treść pliku, wpisz 'dodaj treść'.")

while True:
    user_input = input("Ty: ")
    
    if user_input.lower() == 'exit':
        print("Do widzenia!")
        break
    elif user_input.lower() == 'dodaj treść':
        add_content_to_conversation()
        continue
    
    # Dodaj wiadomość użytkownika do historii
    conversation_history.append({"role": "user", "content": user_input})
    
    # Wywołaj API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=conversation_history,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Pobierz odpowiedź asystenta
    assistant_response = response.choices[0].message.content
    
    # Wyświetl odpowiedź
    print("Asystent:", assistant_response)
    
    # Dodaj odpowiedź asystenta do historii
    conversation_history.append({"role": "assistant", "content": assistant_response})

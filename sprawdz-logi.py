import openai
import datetime
import re

def filter_last_10_hours_logs(log_file_path):
    ten_hours_ago = datetime.datetime.now() - datetime.timedelta(hours=10)
    filtered_logs = []

    with open(log_file_path, 'r') as file:
        for line in file:
            # Używamy regex do sprawdzenia, czy linia logu pasuje do formatu daty
            if re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4}", line):
                date_str = line.split()[0]
                # Usuwamy strefę czasową z daty, aby umożliwić parsowanie
                date_str = date_str[:19]
                try:
                    log_date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
                    if log_date > ten_hours_ago:
                        filtered_logs.append(line)
                except ValueError:
                    # W przypadku błędu parsowania daty, ignorujemy tę linię
                    continue
            else:
                # Ignorujemy linie, które nie pasują do formatu daty
                continue
    
    return ''.join(filtered_logs)

def analyze_logs(log_file_path):
    openai.api_key = 'twoj-klucz-api'

    logs = filter_last_10_hours_logs(log_file_path)

    try:
        response = openai.chat.completions.create(
          model="gpt-4",
          messages=[
              {"role": "system", "content": "Wykonaj analizę poniższych logów. Najpierw wymień w punktach (zaczynając od najstarszego zdarzenia) co się działo. Następnie w maksymalnie 300 znakach zaproponuj poprawki, które warto wdrożyć:"},
              {"role": "user", "content": logs}
          ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

log_file_path = '/var/log/audit/audit.log'
response_message = analyze_logs(log_file_path)
print(response_message)

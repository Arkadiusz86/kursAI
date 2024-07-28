Skrypt logi.py służy  analizy logów serwera, z naciskiem na wydarzenia z ostatnich 10 godzin. Składa się z dwóch głównych funkcji:
1)    filter_last_10_hours_logs(log_file_path): Ta funkcja filtruje logi z pliku, który jej podasz, wyciągając tylko te wpisy, które pochodzą z ostatnich 10 godzin. Używa do tego wyrażeń regularnych (regex), aby znaleźć daty i godziny w logach, a następnie porównuje je z obecnym czasem.

2)    analyze_logs(log_file_path): Ta funkcja to serce skryptu. Wykorzystuje API OpenAI (prawdopodobnie GPT-4) do analizy przefiltrowanych logów. Logi są przesyłane do modelu GPT-4, który generuje analizę tych logów, podając co się działo (w punktach, od najstarszego wydarzenia) oraz proponując ewentualne poprawki.

Scenariusz użycia tego skryptu wyglądałby tak: uruchamiasz funkcję analyze_logs, podając ścieżkę do pliku logów (na przykład /var/log/audit/audit.log). Skrypt filtruje logi z ostatnich 10 godzin, a następnie używa modelu GPT-4 do ich analizy. Wynikiem jest opis wydarzeń z logów oraz propozycje poprawek.



Aby uruchomic skrypt, potrzebujesz:
- pythona (oczywiście)
- konto na OpenAI (Na start otrzymujesz 5$ do przetestowania. Później trzeba zasilić konto.)
- zainstalowaną bibliotekę openAI
- klucz API (do pobrania ze strony OpenAI https://platform.openai.com/api-keys )


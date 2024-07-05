Sprawozdanie dotyczące działania serwerowej części aplikacji
============================================================

Cel aplikacji
-------------
Celem serwerowej części aplikacji jest zarządzanie danymi klientów przy użyciu bazy danych PostgreSQL. Aplikacja umożliwia tworzenie i usuwanie tabeli klientów, import danych z pliku CSV do bazy danych, wyświetlanie całej tabeli, wyświetlanie wybranej części tabeli oraz wyświetlanie pojedynczego rekordu na podstawie ID.

Struktura bazy danych
---------------------
Aplikacja korzysta z bazy danych PostgreSQL, w której tworzona jest tabela `clients`. Struktura tabeli jest następująca:
- `id`: unikalny identyfikator klienta (klucz główny, autoinkrement),
- `city`: miasto zamieszkania klienta,
- `building_number`: numer budynku,
- `street`: ulica,
- `name`: imię,
- `surname`: nazwisko,
- `comments`: dodatkowe komentarze dotyczące klienta (opcjonalne).

Funkcje aplikacji
-----------------
Aplikacja składa się z kilku funkcji, które realizują różne operacje na bazie danych PostgreSQL:

1. **Usuwanie tabeli `clients`**:
   Funkcja `remove_db` usuwa tabelę `clients` z bazy danych, jeśli taka tabela istnieje.

2. **Tworzenie tabeli `clients`**:
   Funkcja `create_table` tworzy tabelę `clients` w bazie danych, jeśli jeszcze nie istnieje.

3. **Import danych z pliku CSV do bazy danych**:
   Funkcja `import_csv_to_postgres` importuje dane z pliku CSV do tabeli `clients` w bazie danych.

4. **Wyświetlanie całej tabeli**:
   Funkcja `display_entire_table` wyświetla wszystkie rekordy z tabeli `clients`.

5. **Wyświetlanie wybranej części tabeli**:
   Funkcja `display_chosen_part` pozwala na wyświetlenie rekordów z tabeli `clients`, które spełniają podane kryterium (filtracja po kolumnie i wartości).

6. **Wyświetlanie pojedynczego rekordu po ID**:
   Funkcja `display_single_row` wyświetla dane konkretnego klienta na podstawie podanego ID.

7. **Pobieranie pliku CSV**:
   Funkcja `download_csv` pobiera dane z pliku CSV i importuje je do tabeli `clients`.

8. **Sprawdzanie istnienia tabeli**:
   Funkcja `check_table_exists` sprawdza, czy tabela `clients` istnieje w bazie danych.

Połączenie z bazą danych
------------------------
Aplikacja łączy się z bazą danych PostgreSQL przy użyciu poświadczeń zapisanych w pliku JSON. Plik ten zawiera informacje takie jak nazwa użytkownika, hasło, nazwa hosta, port oraz nazwa bazy danych. Po nawiązaniu połączenia aplikacja tworzy obiekt silnika bazodanowego, który jest wykorzystywany do wykonywania zapytań SQL.

Interaktywny interfejs użytkownika
----------------------------------
Główna część aplikacji zawiera interaktywny interfejs użytkownika, który pozwala na wybór jednej z kilku dostępnych opcji:

1. **Pobieranie tabeli z pliku CSV**:
   Użytkownik może zaimportować dane z pliku CSV do tabeli `clients` w bazie danych.

2. **Wyświetlanie całej tabeli**:
   Aplikacja pobiera i wyświetla wszystkie rekordy klientów z tabeli `clients`.

3. **Wyświetlanie wybranej części tabeli**:
   Użytkownik może wybrać kolumnę oraz wartość, według których chce filtrować rekordy, a aplikacja wyświetli odpowiednie dane.

4. **Wyświetlanie pojedynczego rekordu po ID**:
   Użytkownik wprowadza ID klienta, którego dane chce zobaczyć, a aplikacja wyświetla odpowiednie informacje.

5. **Usuwanie tabeli**:
   Aplikacja usuwa tabelę `clients` z bazy danych.

6. **Zakończenie programu**:
   Aplikacja kończy działanie.

Wnioski
-------
Serwerowa część aplikacji umożliwia efektywne zarządzanie danymi klientów w bazie danych PostgreSQL. Użycie SQLAlchemy jako warstwy abstrakcji bazy danych zapewnia elastyczność i łatwość zarządzania połączeniami oraz wykonywania zapytań SQL. Dalsze ulepszenia mogłyby obejmować bardziej rozbudowane interfejsy użytkownika oraz dodatkowe funkcje analityczne i raportowe.

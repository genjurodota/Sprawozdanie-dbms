Sprawozdanie dotyczące działania aplikacji ze strony użytkownika
================================================================

Cel aplikacji
-------------
Celem aplikacji jest zarządzanie danymi klientów za pomocą bazy danych SQLite oraz możliwość eksportu tych danych do pliku CSV. Aplikacja pozwala na dodawanie, aktualizowanie, usuwanie i przeglądanie danych klientów oraz generowanie raportów w formacie CSV.

Struktura bazy danych
---------------------
Baza danych zawiera jedną tabelę `clients`, która przechowuje dane klientów. Struktura tabeli jest następująca:
- `id`: unikalny identyfikator klienta (klucz główny, autoincrement),
- `city`: miasto zamieszkania klienta,
- `building_number`: numer budynku,
- `street`: ulica,
- `name`: imię,
- `surname`: nazwisko,
- `comments`: dodatkowe komentarze dotyczące klienta (opcjonalne).

Funkcje aplikacji
-----------------
Aplikacja składa się z kilku funkcji, które realizują różne operacje na bazie danych i plikach CSV:

1. **Tworzenie tabeli `clients`**:
   Funkcja `create_table` tworzy tabelę `clients` w bazie danych, jeśli jeszcze nie istnieje.

2. **Dodawanie nowego klienta**:
   Funkcja `insert_client` dodaje nowy rekord klienta do tabeli `clients`.

3. **Pobieranie wszystkich klientów**:
   Funkcja `get_all_clients` zwraca wszystkie rekordy z tabeli `clients`.

4. **Pobieranie klienta po ID**:
   Funkcja `get_client_by_id` zwraca dane konkretnego klienta na podstawie podanego ID.

5. **Aktualizacja danych klienta**:
   Funkcja `update_client` aktualizuje informacje o kliencie na podstawie podanego ID.

6. **Usuwanie klienta**:
   Funkcja `delete_client` usuwa rekord klienta z tabeli `clients` na podstawie podanego ID.

7. **Usuwanie tabeli `clients`**:
   Funkcja `delete_data_base` usuwa całą tabelę `clients` z bazy danych.

8. **Generowanie pliku CSV**:
   Funkcja `generate_csv` generuje plik CSV zawierający dane wszystkich klientów.

9. **Zamykanie połączenia z bazą danych**:
   Funkcja `close_connection` zamyka połączenie z bazą danych.

10. **Wprowadzanie danych z konsoli**:
    Funkcja `input_client_data` umożliwia wprowadzanie danych klienta z konsoli.

Interaktywny interfejs użytkownika
----------------------------------
Główna część aplikacji zawiera interaktywny interfejs użytkownika, który pozwala na wybór jednej z kilku dostępnych opcji:

1. **Dodawanie nowego klienta**:
   Użytkownik wprowadza dane klienta z konsoli, które są następnie dodawane do bazy danych.

2. **Wyświetlanie wszystkich klientów**:
   Aplikacja pobiera i wyświetla wszystkie rekordy klientów z bazy danych.

3. **Wyświetlanie klienta po ID**:
   Użytkownik wprowadza ID klienta, którego dane chce zobaczyć, a aplikacja wyświetla odpowiednie informacje.

4. **Aktualizacja danych klienta**:
   Użytkownik wprowadza ID klienta, którego dane chce zaktualizować, oraz nowe wartości dla poszczególnych pól. Aplikacja aktualizuje dane w bazie.

5. **Usuwanie klienta**:
   Użytkownik wprowadza ID klienta, którego chce usunąć, a aplikacja usuwa odpowiedni rekord z bazy danych.

6. **Generowanie pliku CSV**:
   Użytkownik podaje nazwę pliku CSV, a aplikacja generuje plik zawierający dane wszystkich klientów.

7. **Usuwanie tabeli `clients`**:
   Aplikacja usuwa całą tabelę `clients` z bazy danych.

8. **Zakończenie programu**:
   Aplikacja zamyka połączenie z bazą danych i kończy działanie.

Wnioski
-------
Aplikacja umożliwia efektywne zarządzanie danymi klientów za pomocą prostego interfejsu użytkownika. Użycie bazy danych SQLite zapewnia trwałość danych, a możliwość eksportu do CSV pozwala na łatwe generowanie raportów i analizę danych w innych narzędziach. Dalsze ulepszenia mogłyby obejmować bardziej rozbudowane interfejsy użytkownika oraz dodatkowe funkcje analityczne.

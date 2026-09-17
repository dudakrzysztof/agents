2.6. Dragon Sprint 05
Important
Name: Dragon Sprint 05

Difficulty: easy

Lines: ?

Minutes: 13

2.6.1. Functional Requirements
Smok w trakcie gry może zwrócić pozycję którą zajmuje

2.6.2. Use Case
Stwórz smoka o nazwie "Wawelski"

Stworzenie smoka bez nazwy podnosi błąd

Smok przy tworzeniu ma losowe punkty życia

Ustaw inicjalną pozycję smoka na x=50, y=100

Pobierz aktualną pozycję

2.6.3. Tests
Feature: Dragon position

Scenario: Dragon returns its position
    Given Dragon is created with name "Wawelski"
      And Position x is 1
      And Position y is 2
     When Gets position
     Then Result is exactly "(1, 2)"
2.6.4. Acceptance Criteria
Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu

Rozwiązanie jest w katalogu dragon

Rozwiązanie jest zapisane w lokalnym repozytorium (git commit)

Rozwiązanie jest wypchnięta do centralnego repozytorium (git push)
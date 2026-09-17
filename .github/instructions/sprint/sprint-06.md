2.7. Dragon Sprint 06
Important
Name: Dragon Sprint 06

Difficulty: easy

Lines: ?

Minutes: 13

2.7.1. Functional Requirements
Smok w trakcie gry może być ustawiony w dowolne miejsce ekranu

2.7.2. Use Case
Stwórz smoka o nazwie "Wawelski"

Stworzenie smoka bez nazwy podnosi błąd

Smok przy tworzeniu ma losowe punkty życia

Ustaw inicjalną pozycję smoka na x=50, y=100

Pobierz aktualną pozycję

Ustaw nową pozycję smoka na x=10, y=20

2.7.3. Tests
Feature: Dragon position

Scenario: Dragon can be set at any position
    Given Dragon is created with name "Wawelski"
     When Sets position x=1 y=2
     Then Position x is 1
      And Position y is 2
2.7.4. Acceptance Criteria
Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu

Rozwiązanie jest w katalogu dragon

Rozwiązanie jest zapisane w lokalnym repozytorium (git commit)

Rozwiązanie jest wypchnięta do centralnego repozytorium (git push)
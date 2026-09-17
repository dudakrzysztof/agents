2.8. Dragon Sprint 07
Important
Name: Dragon Sprint 07

Difficulty: easy

Lines: ?

Minutes: 13

2.8.1. Functional Requirements
Smok w trakcie gry może zmienić pozycję w jedną stronę o zadaną wartość (tylko: prawo lub lewo lub góra lub dół)

Smok w trakcie gry może zmienić pozycję horyzontalnie o zadaną wartość (jednocześnie: prawo i lewo)

Smok w trakcie gry może zmienić pozycję wertykalnie o zadaną wartość (jednocześnie: góra i dół)

Smok w trakcie gry może zmienić pozycję dookólnie o zadaną wartość (jednocześnie: prawo i lewo i dół i góra)

2.8.2. Non-Functional Requirements
Przyjmij górny lewy róg ekranu za punkt początkowy x=0 y=0

Idąc w prawo dodajesz x

Idąc w lewo odejmujesz x

Idąc w górę odejmujesz y

Idąc w dół dodajesz y

Zwróć uwagę, że w grafice komputerowej oś y jest odwrócona

2.8.3. Use Case
Stwórz smoka o nazwie "Wawelski"

Stworzenie smoka bez nazwy podnosi błąd

Smok przy tworzeniu ma losowe punkty życia

Ustaw inicjalną pozycję smoka na x=50, y=100

Pobierz aktualną pozycję

Ustaw nową pozycję smoka na x=10, y=20

Przesuń smoka w lewo o 10 i w dół o 20

Przesuń smoka w lewo o 10 i w prawo o 15

Przesuń smoka w prawo o 15 i w górę o 5

Przesuń smoka w dół o 5

2.8.4. Tests
Feature: Dragon position

Scenario: Dragon moves right
    Given Dragon is created with name "Wawelski"
      And Position x is 10
      And Position y is 20
     When Changes position right by 1
     Then Position x is 11
      And Position y is 20

Scenario: Dragon moves left
    Given Dragon is created with name "Wawelski"
      And Position x is 10
      And Position y is 20
     When Changes position left by 1
     Then Position x is 9
      And Position y is 20

Scenario: Dragon moves down
    Given Dragon is created with name "Wawelski"
      And Position x is 10
      And Position y is 20
     When Changes position down by 1
     Then Position x is 10
      And Position y is 21

Scenario: Dragon moves up
    Given Dragon is created with name "Wawelski"
      And Position x is 10
      And Position y is 20
     When Changes position up by 1
     Then Position x is 10
      And Position y is 19

Scenario: Dragon moves horizontal
    Given Dragon is created with name "Wawelski"
      And Position x is 10
      And Position y is 20
     When Changes position right by 1
      And Changes position left by 2
     Then Position x is 9
      And Position y is 20

Scenario: Dragon moves vertical
    Given Dragon is created with name "Wawelski"
      And Position x is 10
      And Position y is 20
     When Changes position down by 1
      And Changes position up by 2
     Then Position x is 10
      And Position y is 19

Scenario: Dragon moves omnidirectional
    Given Dragon is created with name "Wawelski"
      And Position x is 10
      And Position y is 20
     When Changes position right by 1
      And Changes position left by 2
      And Changes position down by 3
      And Changes position up by 4
     Then Position x is 9
      And Position y is 19
2.8.5. Acceptance Criteria
Rozwiązanie jest rozwinięciem kodu z poprzedniego sprintu

Rozwiązanie jest w katalogu dragon

Rozwiązanie jest zapisane w lokalnym repozytorium (git commit)

Rozwiązanie jest wypchnięta do centralnego repozytorium (git push)

2.8.6. Hints
To nie błąd: "lewo o 10 i w prawo o 15"

Pozycja końcowa powinna być: x=20, y=40
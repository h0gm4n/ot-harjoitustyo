## Viikko 3

- Lisätty Game-luokka, jossa toistaiseksi tapahtuu kaikki toiminta
- Käyttäjä pääsee Main Menuun
- Käyttäjä pääsee vaikeustasonäkymään
- Käyttäjä pääsee valitsemaan Normaalin vaikeustason
- Vaikeustason valittua ratkaistava Sudoku latautuu ruudulle (jota ei toistaiseksi voi ratkoa)
- Testattu, että punaista väriä indikoivan muuttujan määrittely on oikein

## Viikko 4

- Lisätty main_menu.py sekä sudoku_grid.py, joista ensimmäinen sisältää Main Menun toiminnallisuuden,
ja jälkimmäinen toistaiseksi ainoan ruudukon
- Näin ollen toiminnallisuutta ollaan hajautettu useampaan luokkaan
- Ruudukon ylintä riviä voi alkaa ratkomaan, ja peli ilmoittaa, mikäli ollaan valittu ilmeisen väärä numero
- Numeroiden asettaminen tapahtuu siten, että hiirellä "hoveroidaan" ruudun yllä, jolloin numero asetetaan
numeronäppäimellä
- Asetettu numero voidaan pyyhkiä pois painamalla 0
- Testaaminen ei toimi tällä hetkellä

## Viikko 5

 - Sudokun voi täyttää kokonaan
 - Peli ilmoittaa, mikäli ilmeisen väärä luku on asetettu, ja antaa jatkaa vasta, kun se on korjattu painamalla 0
 - Kun ruudukko on täytetty, ruudukko tyhjenee ja peli onnittelee
 - Muutama testi lisätty ja testaaminen saatu toimimaan
 - Sovelluslogiikkaa päivitetty ja koodia jaettu useampaan hakemistoon (entities, services)

## Viikko 6
 
 - Sudokussa nyt mahdollista ratkaista helppo ja vaikea sudoku
 - Peli laskee sudokuun käytetyn ajan ja ilmoittaa sen sudokun ratkaistuttua
 - Peli varmistaa pelaajan painettua ESCiä, haluaako pelaaja keskeyttää täyttämänsä sudokun
 - Testejä lisätty
 - Docstringit lisätty luokkiin Gameplay ja Functions
 - Käyttöohje lisätty

## Viikko 7

 - Pelaaja voi nyt tallentaa tuloksensa
 - Lisätty moduuli, joka tallentaa tulokset
 - Tallennukseen käytetään csv-tiedostoja data-hakemistossa
 - Lisätty tulostaulu
 - Lisätty testejä
 - Lisätty docstringejä
 - Päivitetty vaatimusmäärittely
 - Päivitetty arkkitehtuuri
 - Päivitetty käyttöohje
 - Hienosäädöt ja koodin siistiminen
# Vaatimusmäärittely

## Sovellukset tarkoitus
Sovellus sisältää perinteisen 9x9-ruutuisen Sudoku-pelin. Peliin rekisteröidytään ja se tallentaa tulokset järjestyksessä tulostauluun ratkaisunopeuden perusteella.

## Perusversion toiminnallisuudet 

### Ennen kirjautumista ###
- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syötettäessä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle
  - Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä

### Kirjautumisen jälkeen ###
- Käyttäjä pääsee pelin etusivulle ja voi valita peluun (tehty)
  - Sudoku vastaa vaikeustasoltaan suurin piirtein normaalia vaikeusastetta
- Käyttäjä voi alkaa ratkaisemaan Sudokua (tehty)
  - Alussa ruudukossa on muutama oikein asetettu numero valmiiksi
  - Ruudukon täyttö toimii siten, että pelaaja syöttää jokaiseen ruutuun näppäimistöllään numeron väliltä 1-9 (tehty)
  - Ajastin laskee ratkaisuun käytetyn ajan
- Käyttäjä voi keskeyttää halutessaan Sudokun, jolloin palataan etusivulle (tehty)
- Ratkaistuaan Sudokun peli näyttää ratkaisuun käytetyn ajan, jonka jälkeen käyttäjä voi palata etusivulle (tehty)
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita
- Käyttäjä voi valita helpon, normaalin ja haastavan Sudokun väliltä (tehty)
- Käyttäjän tulokset tallentuvat
- Pelin etusivulle lisätään mahdollisuus nähdä tulostaulu
- Käyttäjä voi halutessaan lisätä tuloksensa tulostauluun, eli ratkaisuun käytetyn ajan vaikeusasteineen ja käyttäjänimineen
- Peli näyttää Sudokua ratkaistaessa, kuinka monta kertaa kutakin numeroa on käytetty
- Peli merkitsee Sudokua ratkaistaessa kaikki ilmeisen väärin asetetut numerot esim. punaisella (tehty)
- Käyttäjätunnuksen voi poistaa

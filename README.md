# Otsikko


Sovellus sisältää perinteisen 9x9-ruutuisen Sudoku-pelin.


## Huomio Python-sovelluksesta

Sovelluksen toiminta on testattu Python-versiolla 3.8. Etenkin vanhempien Python-versioiden kanssa saattaa ilmentyä ongelmia.


## Dokumentaatio

[Vaatimusmäärittely](https://github.com/h0gm4n/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/h0gm4n/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/h0gm4n/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/h0gm4n/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/h0gm4n/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Releaset](https://github.com/h0gm4n/ot-harjoitustyo/releases)

[Testaus](https://github.com/h0gm4n/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```

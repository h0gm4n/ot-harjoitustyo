
# Testausdokumentti

Ohjelmaa on testattu yksikkö- ja integraatiotestein UnitTestillä.

### Yksikkö ja -integraatiotestaus

#### Sovelluslogiikka

Luokka _TestGame_ testaa pääosin luokkaa _Functions_.

#### Testauskattavuus

Sovelluslogiikan testauksen haaraumakattavuus on 68%.

![](./kuvat/coveragereport.png)

### Sovellukseen jääneet laatuongelmat

- Ainakin Cubbli Linux -ympäristössä testatessa Sudokua täyttäessä sekä sen ratkaistua joutuu tuntemattomasta 
syystä painamaan Esciä pari kertaa, ennen kuin voi palata vaikeustasovalikkoon.
Windowsissa cmd:n kautta ajaessa ongelmaa ei kuitenkaan ilmene.


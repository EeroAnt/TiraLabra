# TiraLabra

## Asennus

[Poetry](https://python-poetry.org/) tulee olla asennettuna koneelle. Ajamalla komento 'poetry install' repositorion juurihakemistossa tuotetaan virtuaaliympäristö, jossa on kaikki tarvittavat riippuvaisuudet mukana.

## Ohjelman käynnistys

Virtuaaliympäristö käynnistetään komennolla 'poetry shell', jälleen repositorion juurihakemistossa. Tämän jälkeen voidaan käyttää invoke komentoa 'poetry run invoke start' käynnistämään itse ohjelma. 'exit' -komennolla pääset pois virtuaaliympäristöstä.

## Ohjelman käyttö 

### 1: Tuota avainpari

Ohjelma pyytää avainparille nimeä. Tämän jälkeen ohjelma luo ja tallentaa tämän nimisen avainparin.

### 2: Salaa viesti
Ohjelma pyytää syötteenä salattavan viestin, tiedostonimen (tiedostopääte tulee automaattisesti) viestin tallennusta varten ja millä avaimella salaus tehdään. Jos kaikki menee kivasti, ohjelma kertoo salauksen onnistuneen.

### 3: Pura viesti
Ohjelma pyytää syötteeksi purettavan tiedoston tiedostonimeä ja käytettävää avainta. Onnistuessaan ohjelma tulostaa viestin, jonka salaus on purettu.

## Huomioita:
 - Avainta kysyttäessä ensiksi kysytään avaimen nimeä ja sen jälkeen tarkentamaan, käytetäänkö julkista (j) vai yksityistä (y) avainta.
 - Salaus ja purku toimii utf-8 merkistöllä, joten ääkköset tulee jättää pois salattavista viesteistä.

## Testaus:
Testit voi ajaa virtuaaliympäristössä komennolla 'poetry invoke run test' ja kattavuusraportin luotua testien kanssa komennolla 'poetry run invoke report'.

## Lisätietoa:

[Määrittelydokumentti](https://github.com/EeroAnt/TiraLabra/blob/main/Dokumentaatio/M%C3%A4%C3%A4rittelydokumentti.md)

[Viikkoraportit](https://github.com/EeroAnt/TiraLabra/tree/main/Dokumentaatio/Viikkoraportit)

[Testausdokumentti](https://github.com/EeroAnt/TiraLabra/tree/main/Dokumentaatio/Testaus.md)

[Toteutusdokumentti](https://github.com/EeroAnt/TiraLabra/tree/main/Dokumentaatio/Toteutusdokumentti.pdf)

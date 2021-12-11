# Ruokatilauksen laskija 

Tämä sovellus auttaa säätämään ruokatilauksen määrät kymmenille ihmisille, jotka asuvat n. 11 päivää meditaatiokurssilla. Ohjelma lukee reseptit tekstitiedostosta, etsii relevanteista resepteistä ruokamäärät ja säätää ne annetulle ihmismäärälle. Laskemansa ruokamäärät ohjelma tallentaa neljään eri tiedostoon, koska ruoka-aineet tilataan kolmesta eri paikasta kahtena eri toimitusajankohtana (käytännön syistä ja taloudellisista syistä).

Tämä ohjelma sekä vastaa tosielämän automaatiotarpeeseen että toimii [HY:n Ohjelmistotekniikka-kurssin](https://ohjelmistotekniikka-hy.github.io/) harjoitustyönä. 

## Huomio Python-versiosta

Tämä sovellus on tehty ja testattu pythonin versiolla ``3.8``.

## Dokumentaatio

-[Vaatimusmäärittely](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/dokumentaatio/requirements.md)

-[Harjoitustyön työaikakirjanpito](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.txt)

-[Sovellusarkkitehtuuri](https://github.com/anuvirtane/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Lataus

Lataa uusin [release (listan ylin)](https://github.com/anuvirtane/ot-harjoitustyo/releases)

## Asennus

Asenna riippuvuudet komennolla:

``poetry install``



## Komentorivitoiminnot

Suorita ohjelma komennolla:

``poetry run invoke start``

Suorita yksikkötestit komennolla:

`` poetry run invoke test``

Generoi testikattavuusraportti komennolla:

``poetry run invoke coverage-report``

Raportti generoituu _htmlcov_-hakemistoon.


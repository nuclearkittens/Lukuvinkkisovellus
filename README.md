# Ohjelmistotuotanto, syksy 2021

![GitHub Actions](https://github.com/TopiasHarjunpaa/Lukuvinkkisovellus/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/TopiasHarjunpaa/Lukuvinkkisovellus/branch/main/graph/badge.svg?token=IIHLH6RUFG)](https://codecov.io/gh/TopiasHarjunpaa/Lukuvinkkisovellus)

### Lukuvinkkikirjasto | miniprojekti

Lisää sovelluksen kuvaus...

## Releaset

Placeholder...

## Dokumentaatio

- [Product backlog](https://docs.google.com/spreadsheets/d/10ld7weDSDLxcA8vwZXymfioQPwHWz-7xzCbk3FgV9HU/edit#gid=0)
- [Flinga](https://flinga.fi/s/FTVMGVC)

## Asennus

Aloita kloonaamalla repositorio:

```
$ git clone git@github.com:TopiasHarjunpaa/ot-harjoitustyo.git
$ cd ot-harjoitustyo
```

Asenna seuraavaksi tarvittavat riippuvuudet:

```
$ poetry install
```

Ohjelma käynnistetään komennolla:

```
$ poetry run invoke start
```

## Muut komentorivitoiminnot


#### Testaus:

Testit voidaan suorittaa komennolla:

```
poetry run invoke test
```

Testikattavuusraportin saa generoitua komennolla:

```
poetry run invoke coverage-report
```

Raportti generoidaan kansioon nimeltä `htmlcov`. Testeihin liittyvä koodi on jätetty raportista pois.

#### Pylint:

Laatutarkastukset voidaan suorittaa komennolla:

```
poetry run invoke lint
```

Testeihin liittyvä koodi on jätetty pois laatutarkastuksista.

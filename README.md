<img src='src/static/pics/Lukuvinkkisovellus_logo.png'></img>

# Ohjelmistotuotanto, syksy 2021

Lukuvinkkikirjasto on web-sovellus, joka toteutetaan Helsingin Yliopiston Ohjelmistotuotantokurssin projektityönä. Sovelluksen käyttäjä voi tallettaa, hakea sekä jaotella erilaisia lukuvinkkejä sekä muistiinpanoja, kuten kirjoja, podcasteja, videoita tai blogipostauksia. Tarkemmat tiedot löytyvät [tehtävänannosta](https://ohjelmistotuotanto-hy.github.io/speksi/).

Linkki sovellukseen: https://lukuvinkkiapp.herokuapp.com/

![GitHub Actions](https://github.com/TopiasHarjunpaa/Lukuvinkkisovellus/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/TopiasHarjunpaa/Lukuvinkkisovellus/branch/main/graph/badge.svg?token=IIHLH6RUFG)](https://codecov.io/gh/TopiasHarjunpaa/Lukuvinkkisovellus)

Materiaali on lisenssoitu [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.html) lisenssillä.

<img src='documentation/pics/gplv3-or-later.svg'></img>

## Releaset

- [2. Sprintin release](https://github.com/TopiasHarjunpaa/Lukuvinkkisovellus/releases/tag/v0.1.0)

## Dokumentaatio

- [Product backlog](https://docs.google.com/spreadsheets/d/10ld7weDSDLxcA8vwZXymfioQPwHWz-7xzCbk3FgV9HU/edit#gid=0)
- [Flinga](https://flinga.fi/s/FTVMGVC)
- [Tietokantakaavio](https://github.com/TopiasHarjunpaa/Lukuvinkkisovellus/blob/main/documentation/database_schema.md)
- [Definition of Done](https://github.com/TopiasHarjunpaa/Lukuvinkkisovellus/blob/main/documentation/definition_of_done.md)
- [Sprint review](https://jamboard.google.com/d/1hcJFA41aawSID_24-UuxcD_BTQnUseG9cyPpsFXyDnY/viewer)

## Asennus

Aloita kloonaamalla repositorio:

```
$ git clone git@github.com:TopiasHarjunpaa/Lukuvinkkisovellus.git
$ cd lukuvinkkisovellus
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

Järjestelmätestit voidaan suorittaa komennolla:

```
poetry run invoke robot
```

#### Pylint:

Laatutarkastukset voidaan suorittaa komennolla:

```
poetry run invoke lint
```

Testeihin liittyvä koodi on jätetty pois laatutarkastuksista.

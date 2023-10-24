# Testaamisesta

Testit voi ajaa komennolla "coverage run --branch -m pytest src" ja komennolla "coverage report -m" saa kattavuusraportin tulostettua terminaaliin.

Sovelluslogiikkaa on testattu yksikkötesteillä. Käyttöliittymiä manuaalisesti.
![](testirapsa.png)

Testit vievät noin minuutin. Kaikki muu toimii hyvin nopsasti, mutta alkuluvun tuottaminen Miller-Rabin -testillä ottaa aikansa. Tässä tulee myös testattua sen tehokkuutta, koska Miller-Rabinin tarkkuutta testattaessa tuotetaan 40 alkulukua ja avainpareja tuotettaessa aina 2 lisää. Jos testeihin ei kulu useampaa minuuttia, niin asian pitäisi olla ihan mukavasti.

Testailin pythonin unittestillä ehkä osittain turhiakin asioita. Testasin mm.
 - onko tuottamani pienten alkulukujen listan sisältö on oikein.
 - factor_out funktiota testasin kahdella luvulla, parillisella ja parittomalla
 - koitin alkulukutestiä parittomalla komposiitilla
 - luon 40 kpl potentiaalisia alkulukuja ja tarkastan ne sympyn isPrime()-funktiolla. Hyväksyn yhden ei-alkuluvun, koska kyse on epädeterministestä funktiosta kuitenkin. Tässä menee valtaosa testien käyttämästä ajasta
 - testaan matikkapalikat.py:n apufunktiot yksittäisillä syötteillä. Tämä tuntuu nimelliseltä testikattavuuden kasvattamiselta, mutta jos jokin isompi ei toimi ja joku näistä testeistä epäonnistuu, on kait helppo lähteä liikkeelle täältä.
 - avaimia testaan lähtökohtaisesti vain, onko tulosteen tyyppi oikein. Avaimen luomiseen liittyy satunnaisuutta, enkä keksinyt kuinka luoda kattavaa ja determinististä testiä, joka antaisi parempaakaan dataa ulos.
 - Salausta testaan purkamalla. Purku ei toimi, jos salaus ei toimi. Purun osalta testaan oikeaa avainta, väärää avainta ja huonoa tiedostonimeä.
 - Testaan paikantimen osalta skenaariot, missä löydän ja missä en löydä, nimettyä avainta/viestiä

Testeistä puuttuvat rivit ovat:
 - 2 virheprinttiä. En keksinyt/löytänyt helppoa tapaa testata printtejä
 - jos avaingeneraattori arpookin 2 samaa alkulukua, pitää toinen arpoa uudestaan.
 - Miller-Rabinin ensimmäinen komposiittiehto. En keksinyt lukua, mikä osuisi siihen. Testi itsessään toimii riittävällä tarkkuudella ja riittävällä tehokkuudella, joten oletan tämänkin toimivan ainakin lähes oikein.

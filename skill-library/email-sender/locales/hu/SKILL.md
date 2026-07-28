---
name: email-sender
description: >-
  Valódi SMTP-n keresztül ténylegesen elküldi az e-mailt (nem csupán megírja a szöveget). Bármilyen olyan helyzetben használd ezt a Skill-t, ahol „információt kell e-mailben eljuttatni másoknak” – tömeges értesítés, óraátcsoportosítás/óraközés/vizsga-emlékeztető, levelezés egy személynek vagy csoportnak, elkészített tartalom e-mailben történő kiküldése stb. Még ha a felhasználó nem is mondja ki egyértelműen, hogy „küldj e-mailt”, ha a szándék „értesítés / tájékoztatás / küldd el valakinek / küldd el mindenkinek”, akkor is ezt a Skill-t aktiváld. Trigger szavak: e-mail küldése, levél küldése, tömeges küldés, hallgatók/diákok/szülők értesítése, küldd el …-t …-nek, e-mail emlékeztető, levél, email, send email, notify by email, mail this to.
category: Fejlesztői eszközök
---

# email-sender · E-mail küldő Skill

A Skill telepítése után az agent a `scripts/send-email.py` segítségével **valóban képes e-mailt küldeni** – nem csupán megírja a levél szövegét, hanem el is küldi azt. A script önálló, a konkrét munkaterülettől független; a hitelesítési adatok a felhasználó saját könyvtárában tárolódnak, egyszeri beállítás után munkaterületek és munkamenetek között újrahasználhatóak.

> A `<SKILL_DIR>` a Skill könyvtárát jelöli (ahol a `SKILL.md` található). A parancsok végrehajtásakor a relatív útvonalat a könyvtár alatti abszolút útvonallá kell feloldani, pl. `python <SKILL_DIR>/scripts/send-email.py ...`.
> Függőség: Python 3 (csak szabványos könyvtár, nincs szükség további telepítésre).

## Folyamat áttekintés

A küldési kérelem három lépésből áll: először ellenőrizd, hogy a konfiguráció megvan-e → ha nincs, vezesd végig a felhasználót egy beállításon → írd meg, jelenítsd meg, erősítsd meg, küldd el. Azért különül el a „megjelenítés és megerősítés” lépése, mert az e-mailt küldés után nem lehet visszavonni, különösen tömeges küldésnél; a címzettek és a szöveg előzetes ellenőrzésével elkerülhetők a tévesztések.

## 1. lépés: Konfiguráció önértékelése

Bármilyen küldési kérelemnél először futtasd az öntesztet, és állapítsd meg, hogy az SMTP készen áll-e:

```bash
python <SKILL_DIR>/scripts/send-email.py check
```

- `✅ A konfiguráció teljes` → ugorj a 3. lépésre.
- `⚠️ A konfiguráció nem teljes` → folytasd a 2. lépéssel a beállítások elvégzésével.

## 2. lépés: Beállítások elvégzése (csak ha még nincs konfigurálva)

A cél három dolog megszerzése és a konfigurációba írása: **e-mail szolgáltató, feladó címe, kliensengedélyezési kód**.

Fontos: a legtöbb e-mail szolgáltatónál az SMTP bejelentkezéshez nem a webes bejelentkezési jelszót kell használni, hanem egy különálló „kliensengedélyezési kód / alkalmazás-specifikus jelszót”. Ha bejelentkezési jelszót használsz, szinte biztosan `535 hitelesítési hiba` lép fel, ezért a beállítás során tisztázd ezt a különbséget. Az egyes szolgáltatók engedélyezési kódjának beszerzési lépéseit a `references/providers.md` tartalmazza – a felhasználó szolgáltatójának megfelelő bejegyzést olvasd be, és úgy add tovább, ne hagyd, hogy a felhasználó maga találja ki.

1. Kérdezd meg a felhasználótól, melyik szolgáltatót használja (alapértelmezett: 163 / 126 / qq / exmail / aliyun / feishu / gmail / outlook; egyéb szolgáltató esetén kérdezz rá a host/port/tls értékekre, a paramétereket lásd a references-ben).
2. Kérdezd meg a feladó e-mail címét.
3. Vezesd végig a felhasználót az engedélyezési kód beszerzésén (lépések a references-ben). **A folyamat során ne írasd ki az engedélyezési kódot a beszélgetésbe.**
4. Írd be a konfigurációba (`--provider` segítségével automatikusan kitölti a host/port/tls értékeket, így a felhasználónak nem kell ezeket megjegyeznie):

```bash
python <SKILL_DIR>/scripts/send-email.py config set \
    --provider 163 --user teacher@163.com --password "<engedélyezési kód>"
```

5. Fiók és engedélyezési kód ellenőrzése (valóban csatlakozik az SMTP-hez, de nem küld levelet):

```bash
python <SKILL_DIR>/scripts/send-email.py check --test
```

   Sikertelenség esetén a script megadja a megfelelő szolgáltatóra vonatkozó engedélyezési kód tippet; a `references/providers.md` hibakeresési táblázata alapján segítsd a felhasználót a javításban, majd próbálja újra.

## 3. lépés: Írás, megjelenítés, megerősítés, küldés

1. **Címzettek és szöveg meghatározása**. A címzettek a felhasználó által megadott címből vagy névsorból származnak, ne találj ki e-mail címeket. A szövegben tüntesd fel, hogy „ki, milyen ügyben, mikor, hol, mit kell tennie”, hogy a címzett azonnal megértse.
2. **Először dry-run előnézet** (alapértelmezett viselkedés, nem küld levelet):

```bash
python <SKILL_DIR>/scripts/send-email.py send \
    --to "a@x.com,b@y.com" --subject "【Óraátcsoportosítási értesítés】 Adatszerkezetek" --body-file /tmp/notice.txt
```

3. **Az előnézetet mutasd meg teljes egészében a felhasználónak, és kérdezd meg, hogy elküldheti-e.** Ha nem kapsz egyértelmű megerősítést, maradj a dry-run módban, ne küldjétek el saját szakértőre.
4. **Megerősítés után add hozzá a `--send` paramétert a tényleges küldéshez**:

```bash
python <SKILL_DIR>/scripts/send-email.py send \
    --to "a@x.com,b@y.com" --subject "【Óraátcsoportosítási értesítés】 Adatszerkezetek" --body-file /tmp/notice.txt --send
```

5. Küldés után a script automatikusan hozzáfűzi a rekordot az `$INNO_HOME/email-send-log.md` fájlhoz, és jelentést tesz az eredményről; sikertelenség esetén hibakeresési tippet ad (a részleteket lásd a references hibatáblázatában).

## Parancsok gyors áttekintése

| Parancs | Funkció |
|---|---|
| `check` / `check --test` | Konfiguráció önértékelése / valódi bejelentkezési ellenőrzéssel (nem küld levelet) |
| `config set --provider <név> --user <e-mail> --password <engedélyezési kód>` | Konfiguráció írása |
| `config show` / `config path` | Konfiguráció megtekintése maszkírozva / konfigurációs útvonal kiírása |
| `send --to --subject --body-file [--send]` | Előnézet (alapértelmezett) / küldés (`--send` megadásával) |

## Konfiguráció és biztonság

- A hitelesítő adatok fájlja: `$INNO_HOME/email.json` (alapértelmezett: `~/.inno-agent/email.json`), mentéskor automatikusan 600 jogosultságra állítva. Felülírható környezeti változókkal is: `SMTP_HOST/PORT/USER/PASS/FROM/TLS`, vagy az `INNO_EMAIL_CONFIG` változóval megadható az elérési út.
- Az engedélyezési kód egyenértékű a jelszóval: ne írd olyan fájlba, amely commitolható/megosztható, és ne írasd ki a válaszban; ha gyanítod, hogy kiszivárgott, a szolgáltató beállításaiban visszavonhatod az engedélyezési kódot, nem kell megváltoztatnod a fő jelszót.
- Alapértelmezés szerint dry-run, csak az explicit `--send` küldi el a levelet. Tömeges küldés előtt mindig ellenőrizd újra a címzettek körét, hogy elkerüld a tévesztést vagy a kihagyást.

## További referenciák

- `references/providers.md` — az egyes szolgáltatók host/port/tls paraméterei, az engedélyezési kód beszerzésének lépései, az SMTP hibák hibakeresési táblázata. Ha konfigurálási vagy küldési problémád van, ezt olvasd el.

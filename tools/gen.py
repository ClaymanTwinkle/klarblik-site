"""生成 etikett-site 的支持页和隐私政策（英语、瑞典语、丹麦语）。用法：python3 -I gen.py <站点目录>"""
import os
import sys

OUT = sys.argv[1]
ISSUES = "https://github.com/ClaymanTwinkle/etikett-site/issues"
EMAIL = "claymantwinkle@gmail.com"
MAIL = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
OFF_PRIVACY = {"en": "https://world.openfoodfacts.org/privacy", "sv": "https://se.openfoodfacts.org/privacy", "da": "https://dk.openfoodfacts.org/privacy"}
GH_PRIVACY = "https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement"
DATA_REPO = "https://github.com/ClaymanTwinkle/etikett-data"


def services(lang):
    off, gh, repo = OFF_PRIVACY[lang], GH_PRIVACY, DATA_REPO
    if lang == "en":
        return f"""The app has no server of its own. It connects to two outside services, and you can turn both off in Settings (“Look up on Open Food Facts”):
<ul><li><b>Open Food Facts</b>: when a scanned product is not in the database on your phone, the barcode number (the number of the product, not information about you) is sent to the Open Food Facts public database. Product pictures are also loaded from Open Food Facts. No account, location or device identifier is sent. See the <a href="{off}">Open Food Facts privacy policy</a>.</li>
<li><b>GitHub</b>: once a week the app downloads the latest product database as a file from <a href="{repo}">GitHub</a>. Nothing is sent except the download request. See the <a href="{gh}">GitHub privacy statement</a>.</li></ul>
Like any internet request, these services can see your IP address. We do not receive it."""
    if lang == "sv":
        return f"""Appen har ingen egen server. Den ansluter till två externa tjänster, och båda kan stängas av i Inställningar (”Slå upp i Open Food Facts”):
<ul><li><b>Open Food Facts</b>: när en skannad vara inte finns i databasen på telefonen skickas streckkodsnumret (varans nummer, inte uppgifter om dig) till Open Food Facts öppna databas. Produktbilder hämtas också från Open Food Facts. Inget konto, ingen plats och ingen enhetsidentitet skickas. Se <a href="{off}">Open Food Facts integritetspolicy</a>.</li>
<li><b>GitHub</b>: en gång i veckan hämtar appen den senaste produktdatabasen som en fil från <a href="{repo}">GitHub</a>. Inget skickas utom själva nedladdningen. Se <a href="{gh}">GitHubs integritetspolicy</a>.</li></ul>
Som vid alla anrop på internet kan tjänsterna se din IP-adress. Vi får inte del av den."""
    return f"""Appen har ingen egen server. Den forbinder til to eksterne tjenester, og begge kan slås fra i Indstillinger (”Slå op i Open Food Facts”):
<ul><li><b>Open Food Facts</b>: når en scannet vare ikke findes i databasen på telefonen, sendes stregkodsnummeret (varens nummer, ikke oplysninger om dig) til Open Food Facts’ åbne database. Produktbilleder hentes også fra Open Food Facts. Der sendes ingen konto, placering eller enheds-id. Se <a href="{off}">Open Food Facts’ privatlivspolitik</a>.</li>
<li><b>GitHub</b>: en gang om ugen henter appen den nyeste produktdatabase som en fil fra <a href="{repo}">GitHub</a>. Der sendes intet ud over selve hentningen. Se <a href="{gh}">GitHubs privatlivserklæring</a>.</li></ul>
Som ved alle forespørgsler på internettet kan tjenesterne se din IP-adresse. Vi får den ikke."""


T = {
    "en": dict(
        home="Support", privacy="Privacy policy", updated="Last updated: 2 November 2026", title="Klarblik support",
        intro="Klarblik shows the additives, allergens and signs of ultra-processing in food sold in Sweden, Denmark and Finland. Scan the barcode or photograph the ingredient list.",
        faq=[
            ("How do I restore my purchase?", "Open Settings → Unlock personal features → Restore purchase. Use the same Apple ID you bought with. Family members in your Family Sharing group get the purchase automatically."),
            ("The result doesn’t match the package.", "Tap “Different from the pack?” at the bottom of the result and photograph the ingredient list. The photo is read on your phone, and the result follows what is printed on the package you are holding."),
            ("Why is the product not found?", "Over 18,000 Nordic products are built into the app and updated weekly. If a product is missing and online lookup is on, the barcode number is sent to Open Food Facts. If it is not there either, photograph the ingredient list."),
            ("Where do the explanations come from?", "Every statement points to an official source: EU regulations, EFSA scientific opinions and IARC classifications. The scoring method is public and versioned in the app. The app provides information, not medical advice. Always read the package if you have an allergy."),
            ("Does the app work offline?", "Yes. The product database and reading of photos work without a connection. Online lookup and the weekly database update can be turned off in Settings."),
        ],
        contact_title="Contact", contact=f'Report a problem or ask a question by email: {MAIL}, or on GitHub: <a href="{ISSUES}">{ISSUES}</a> (public). Please do not include health information you do not need to share.',
        pp_title="Privacy policy",
        summary="Short version: Klarblik has no account, no ads and no analytics. We do not collect any personal data. Photos, lists and history stay on your phone.",
        pp=[
            ("What stays on your phone", "Ingredient photos and images you pick are read with Apple’s on-device text recognition and are never uploaded. Your avoid lists, family profiles and scan history are stored only on your phone. Deleting the app deletes them."),
            ("What is sent over the internet", services("en")),
            ("Purchases", "The one-time purchase goes through Apple’s App Store. We never see your name, Apple ID or payment details."),
            ("No tracking", "There is no advertising, no analytics and no attribution software in the app, and nothing is shared with data brokers."),
            ("Children", "The app does not collect data from anyone, including children."),
            ("If you email us", "If you write to us, we receive your email address and message through Gmail (Google). We use them only to answer you, and delete the conversation when the matter is settled, at the latest after 12 months. Ask us at any time and we delete it straight away."),
            ("Your rights", "The app gives us no personal data about you, so apart from emails you send us there is nothing for us to access, correct or delete. You can delete everything the app has stored by deleting the app."),
            ("Changes", "If this policy changes, the new version is published on this page with a new date."),
        ],
        footer="Product data: Open Food Facts (ODbL). Additive names: official EU texts."),
    "sv": dict(
        home="Support", privacy="Integritetspolicy", updated="Senast uppdaterad: 2 november 2026", title="Klarblik – support",
        intro="Klarblik visar tillsatser, allergener och tecken på ultraprocessad mat i livsmedel som säljs i Sverige, Danmark och Finland. Skanna streckkoden eller fota ingredienslistan.",
        faq=[
            ("Hur återställer jag mitt köp?", "Öppna Inställningar → Lås upp personliga funktioner → Återställ köp. Använd samma Apple-ID som när du köpte. Familjemedlemmar i din familjedelning får köpet automatiskt."),
            ("Resultatet stämmer inte med förpackningen.", "Tryck på ”Stämmer det inte med förpackningen?” längst ned i resultatet och fota ingredienslistan. Bilden läses på telefonen, och resultatet följer det som står på förpackningen du håller i."),
            ("Varför hittas inte varan?", "Över 18 000 nordiska varor finns i appen och uppdateras varje vecka. Saknas varan och uppslag är på skickas streckkodsnumret till Open Food Facts. Finns den inte där heller, fota ingredienslistan."),
            ("Var kommer förklaringarna ifrån?", "Varje uppgift hänvisar till en officiell källa: EU:s förordningar, EFSA:s vetenskapliga yttranden och IARC:s klassningar. Bedömningsmetoden är öppen och har versionsnummer i appen. Appen ger information, inte medicinska råd. Läs alltid förpackningen om du har en allergi."),
            ("Fungerar appen utan nät?", "Ja. Produktdatabasen och avläsningen av bilder fungerar utan uppkoppling. Uppslag och den veckovisa uppdateringen kan stängas av i Inställningar."),
        ],
        contact_title="Kontakt", contact=f'Rapportera ett problem eller ställ en fråga via e-post: {MAIL}, eller på GitHub: <a href="{ISSUES}">{ISSUES}</a> (offentligt). Skriv inga uppgifter om hälsa som du inte behöver dela.',
        pp_title="Integritetspolicy",
        summary="Kort version: Klarblik har inget konto, ingen reklam och ingen analys. Vi samlar inte in några personuppgifter. Bilder, listor och historik stannar på telefonen.",
        pp=[
            ("Det här stannar på telefonen", "Bilder på ingredienslistor och bilder du väljer läses med Apples textigenkänning på telefonen och laddas aldrig upp. Dina listor, familjeprofiler och skanningshistorik sparas bara på telefonen. Tar du bort appen försvinner de."),
            ("Det här skickas över internet", services("sv")),
            ("Köp", "Engångsköpet görs via Apples App Store. Vi ser aldrig ditt namn, Apple-ID eller dina betaluppgifter."),
            ("Ingen spårning", "Appen har ingen reklam, ingen analys och inga verktyg för attribution, och inget delas med datamäklare."),
            ("Barn", "Appen samlar inte in uppgifter från någon, inte heller från barn."),
            ("Om du mejlar oss", "Om du skriver till oss får vi din e-postadress och ditt meddelande via Gmail (Google). Vi använder dem bara för att svara dig och raderar konversationen när ärendet är klart, senast efter 12 månader. Be oss när som helst, så raderar vi den direkt."),
            ("Dina rättigheter", "Appen ger oss inga personuppgifter om dig, så utöver mejl du skickar till oss finns det inget för oss att lämna ut, rätta eller radera. Allt appen har sparat tas bort när du tar bort appen."),
            ("Ändringar", "Om policyn ändras publiceras den nya versionen på den här sidan med nytt datum."),
        ],
        footer="Produktdata: Open Food Facts (ODbL). Tillsatsnamn: EU:s officiella texter."),
    "da": dict(
        home="Support", privacy="Privatlivspolitik", updated="Senest opdateret: 2. november 2026", title="Klarblik – support",
        intro="Klarblik viser tilsætningsstoffer, allergener og tegn på ultraforarbejdet mad i fødevarer, der sælges i Danmark, Sverige og Finland. Scan stregkoden eller tag et billede af ingredienslisten.",
        faq=[
            ("Hvordan gendanner jeg mit køb?", "Åbn Indstillinger → Lås personlige funktioner op → Gendan køb. Brug det samme Apple-id, som du købte med. Familiemedlemmer i din familiedeling får købet automatisk."),
            ("Resultatet passer ikke med emballagen.", "Tryk på ”Passer det ikke med pakken?” nederst i resultatet, og tag et billede af ingredienslisten. Billedet læses på telefonen, og resultatet følger det, der står på emballagen, du holder i hånden."),
            ("Hvorfor findes varen ikke?", "Over 18.000 nordiske varer ligger i appen og opdateres hver uge. Mangler varen, og opslag er slået til, sendes stregkodsnummeret til Open Food Facts. Findes den heller ikke der, så tag et billede af ingredienslisten."),
            ("Hvor kommer forklaringerne fra?", "Hver oplysning henviser til en officiel kilde: EU-forordninger, EFSA’s videnskabelige udtalelser og IARC’s klassificeringer. Vurderingsmetoden er åben og har versionsnummer i appen. Appen giver information, ikke medicinsk rådgivning. Læs altid emballagen, hvis du har en allergi."),
            ("Virker appen uden netværk?", "Ja. Produktdatabasen og aflæsningen af billeder virker uden forbindelse. Opslag og den ugentlige opdatering kan slås fra i Indstillinger."),
        ],
        contact_title="Kontakt", contact=f'Rapportér et problem eller stil et spørgsmål via e-mail: {MAIL}, eller på GitHub: <a href="{ISSUES}">{ISSUES}</a> (offentligt). Skriv ingen helbredsoplysninger, som du ikke behøver at dele.',
        pp_title="Privatlivspolitik",
        summary="Kort fortalt: Klarblik har ingen konto, ingen reklamer og ingen analyse. Vi indsamler ingen personoplysninger. Billeder, lister og historik bliver på telefonen.",
        pp=[
            ("Det bliver på telefonen", "Billeder af ingredienslister og billeder, du vælger, læses med Apples tekstgenkendelse på telefonen og uploades aldrig. Dine lister, familieprofiler og scanningshistorik gemmes kun på telefonen. Sletter du appen, forsvinder de."),
            ("Det sendes over internettet", services("da")),
            ("Køb", "Engangskøbet foregår via Apples App Store. Vi ser aldrig dit navn, Apple-id eller dine betalingsoplysninger."),
            ("Ingen sporing", "Appen har ingen reklamer, ingen analyse og ingen værktøjer til attribution, og intet deles med datamæglere."),
            ("Børn", "Appen indsamler ikke oplysninger fra nogen, heller ikke fra børn."),
            ("Hvis du skriver til os", "Hvis du skriver til os, modtager vi din e-mailadresse og din besked via Gmail (Google). Vi bruger dem kun til at svare dig og sletter samtalen, når sagen er afklaret, senest efter 12 måneder. Bed os når som helst, så sletter vi den med det samme."),
            ("Dine rettigheder", "Appen giver os ingen personoplysninger om dig, så ud over e-mails, du sender os, er der intet for os at udlevere, rette eller slette. Alt, appen har gemt, slettes, når du sletter appen."),
            ("Ændringer", "Hvis politikken ændres, offentliggøres den nye version på denne side med ny dato."),
        ],
        footer="Produktdata: Open Food Facts (ODbL). Navne på tilsætningsstoffer: EU’s officielle tekster."),
}
PATH = {"en": "", "sv": "sv/", "da": "da/"}
NAMES = [("en", "English"), ("sv", "Svenska"), ("da", "Dansk")]


def nav(lang, kind, up):
    cur = ' aria-current="page"'
    links = [f'<a href="{up}{PATH[lang]}"{cur if kind == "support" else ""}>{T[lang]["home"]}</a>',
             f'<a href="{up}{PATH[lang]}privacy.html"{cur if kind == "privacy" else ""}>{T[lang]["privacy"]}</a>', "<span>·</span>"]
    target = "privacy.html" if kind == "privacy" else ""
    links += [f'<a href="{up}{PATH[l]}{target}" hreflang="{l}">{name}</a>' for l, name in NAMES]
    return "<nav>" + "".join(links) + "</nav>"


def render(lang, kind):
    t = T[lang]
    up = "" if lang == "en" else "../"
    if kind == "support":
        title = t["title"]
        body = f'<h1>{title}</h1><p>{t["intro"]}</p>' + "".join(f"<section><h2>{q}</h2><p>{a}</p></section>" for q, a in t["faq"])
    else:
        title = f'{t["pp_title"]} – Klarblik'
        body = f'<h1>{title}</h1><p class="updated">{t["updated"]}</p><p><b>{t["summary"]}</b></p>' + "".join(f"<h2>{h}</h2><p>{p}</p>" for h, p in t["pp"])
    body += f'<h2>{t["contact_title"]}</h2><p>{t["contact"]}</p>'
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><link rel="stylesheet" href="{up}style.css"></head>
<body><main>{nav(lang, kind, up)}
{body}
<footer>{t["footer"]}</footer></main></body></html>
"""


for lang in T:
    folder = os.path.join(OUT, PATH[lang])
    os.makedirs(folder, exist_ok=True)
    for kind, name in [("support", "index.html"), ("privacy", "privacy.html")]:
        with open(os.path.join(folder, name), "w", encoding="utf-8") as f:
            f.write(render(lang, kind))
print("ok")

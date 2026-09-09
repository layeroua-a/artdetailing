# -*- coding: utf-8 -*-
import os, base64

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# ICONS  (minimal line-icon set, single family, stroke=currentColor)
# ---------------------------------------------------------------------------
ICON = {
"phone": '<svg viewBox="0 0 24 24" class="icon"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.9 21 3 13.1 3 3c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1L6.6 10.8Z"/></svg>',
"mail": '<svg viewBox="0 0 24 24" class="icon"><path d="M3 6h18v12H3z"/><path d="m3 6 9 7 9-7"/></svg>',
"pin": '<svg viewBox="0 0 24 24" class="icon"><path d="M12 22s7-7.4 7-13a7 7 0 1 0-14 0c0 5.6 7 13 7 13Z"/><circle cx="12" cy="9" r="2.6"/></svg>',
"clock": '<svg viewBox="0 0 24 24" class="icon"><circle cx="12" cy="12" r="9.2"/><path d="M12 7v5.2l3.6 2.1"/></svg>',
"instagram": '<svg viewBox="0 0 24 24" class="icon"><rect x="3.3" y="3.3" width="17.4" height="17.4" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.1" cy="6.9" r="1" fill="currentColor" stroke="none"/></svg>',
"facebook": '<svg viewBox="0 0 24 24" class="icon"><path d="M14.5 8.5h2.3V5.2h-2.3c-2.3 0-3.8 1.5-3.8 3.9v1.9H8.5v3.3h2.2V21h3.3v-6.7h2.3l.4-3.3h-2.7V9.4c0-.6.3-.9 1-.9Z"/></svg>',
"telegram": '<svg viewBox="0 0 24 24" class="icon"><path d="M3 11.4 20.4 4l-3 16-5.5-4.2-2.7 2.6-.4-4L18 7.3 8.2 13.7 3 11.4Z"/></svg>',
"check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><path d="M4 12.5 9.3 18 20 6"/></svg>',
"chev-r": '<svg viewBox="0 0 24 24" class="icon"><path d="m9 5 7 7-7 7"/></svg>',
"arrow-r": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
"shield": '<svg viewBox="0 0 24 24" class="icon"><path d="M12 3 20 6v6c0 5-3.4 8.4-8 9-4.6-.6-8-4-8-9V6l8-3Z"/><path d="m8.5 12 2.4 2.5L15.5 9"/></svg>',
"droplet": '<svg viewBox="0 0 24 24" class="icon"><path d="M12 3s6.5 7 6.5 11.5a6.5 6.5 0 0 1-13 0C5.5 10 12 3 12 3Z"/></svg>',
"sparkle": '<svg viewBox="0 0 24 24" class="icon"><path d="M12 3v5M12 16v5M3 12h5M16 12h5M6 6l3 3M18 6l-3 3M6 18l3-3M18 18l-3-3"/></svg>',
"sun": '<svg viewBox="0 0 24 24" class="icon"><circle cx="12" cy="12" r="4.3"/><path d="M12 2.5v3M12 18.5v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2.5 12h3M18.5 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg>',
"target": '<svg viewBox="0 0 24 24" class="icon"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.3"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/></svg>',
"layers": '<svg viewBox="0 0 24 24" class="icon"><path d="m12 3 8.5 4.6L12 12.2 3.5 7.6 12 3Z"/><path d="m3.5 12 8.5 4.6L20.5 12M3.5 16.4 12 21l8.5-4.6"/></svg>',
"coffee": '<svg viewBox="0 0 24 24" class="icon"><path d="M4 9h13v5.4A4.6 4.6 0 0 1 12.4 19H8.6A4.6 4.6 0 0 1 4 14.4V9Z"/><path d="M17 10.2h1.4a2.6 2.6 0 0 1 0 5.2H17"/><path d="M7.5 5.5c0-1 1-1.2 1-2.2M11.5 5.5c0-1 1-1.2 1-2.2"/></svg>',
"badge": '<svg viewBox="0 0 24 24" class="icon"><path d="M12 2 20 6v6c0 5-3.4 8.4-8 9-4.6-.6-8-4-8-9V6l8-4Z"/><path d="M9 12.4l2 2.1 4-4.5"/></svg>',
"wallet": '<svg viewBox="0 0 24 24" class="icon"><path d="M3 7.5A2.5 2.5 0 0 1 5.5 5h11A2.5 2.5 0 0 1 19 7.5v9A2.5 2.5 0 0 1 16.5 19h-11A2.5 2.5 0 0 1 3 16.5v-9Z"/><path d="M15 12.3h4v3.4h-4a1.7 1.7 0 0 1 0-3.4Z"/></svg>',
"close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" width="18" height="18"><path d="M5 5l14 14M19 5 5 19"/></svg>',
"info": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" width="20" height="20"><circle cx="12" cy="12" r="9.2"/><path d="M12 11v5.5M12 8v.01"/></svg>',
"car": '<svg viewBox="0 0 24 24" class="icon"><path d="M4 15.5 5.4 10a2 2 0 0 1 1.9-1.4h9.4A2 2 0 0 1 18.6 10L20 15.5"/><path d="M3.6 15.5h16.8v3a1 1 0 0 1-1 1h-1.2a1 1 0 0 1-1-1v-1H6.8v1a1 1 0 0 1-1 1H4.6a1 1 0 0 1-1-1v-3Z"/><circle cx="7.3" cy="15.6" r="1.3" fill="currentColor" stroke="none"/><circle cx="16.7" cy="15.6" r="1.3" fill="currentColor" stroke="none"/></svg>',
}

BRAND_MARK = '''<svg viewBox="0 0 48 48" class="brand-mark" fill="none" stroke="currentColor" stroke-width="2.2">
<path d="M24 4 42 14v20L24 44 6 34V14Z" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M14.5 26.5c3-8.5 8.5-13.5 17-14.5" stroke-linecap="round"/>
<circle cx="32" cy="11" r="1.7" fill="currentColor" stroke="none"/>
</svg>'''

FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#17201a"/><path d="M24 6 40 15v18L24 42 8 33V15Z" fill="none" stroke="#EADFB8" stroke-width="2.3" stroke-linejoin="round"/><path d="M15.5 26c2.7-7.6 7.6-12 15-13" fill="none" stroke="#EADFB8" stroke-width="2.3" stroke-linecap="round"/></svg>'''
FAVICON_B64 = base64.b64encode(FAVICON.encode("utf-8")).decode("ascii")

HERO_SVG = '''<svg viewBox="0 0 800 460" preserveAspectRatio="xMidYMid meet">
  <path class="car-path" d="M120,330 C128,296 154,282 182,276 C206,238 246,196 300,188 L438,186 C486,186 516,202 534,232 C578,230 624,240 652,258 C678,270 694,288 698,316 L698,332 Z"/>
  <path class="car-path" style="animation-delay:.5s" d="M182,276 C300,262 470,258 610,266"/>
  <path class="car-path" style="animation-delay:.8s" d="M300,188 L332,276 M438,186 L474,232"/>
  <circle class="car-path" style="animation-delay:1.1s" cx="228" cy="336" r="46"/>
  <circle class="car-path" style="animation-delay:1.1s" cx="228" cy="336" r="19"/>
  <circle class="car-path" style="animation-delay:1.3s" cx="600" cy="336" r="46"/>
  <circle class="car-path" style="animation-delay:1.3s" cx="600" cy="336" r="19"/>
  <path class="car-path" style="animation-delay:1.5s" d="M120,332 L60,332 M698,324 L748,324"/>
</svg>'''

def icon(name):
    return ICON[name]

def ph_tile(label="", light=False):
    cls = "ph-tile light" if light else "ph-tile"
    lab = f'<span style="position:absolute;bottom:10px;left:12px;font-size:11px;font-weight:700;letter-spacing:.02em;">{label}</span>' if label else ""
    return f'<div class="{cls}">{icon("car")}{lab}</div>'

# ---------------------------------------------------------------------------
# TEXT CONTENT  per language
# ---------------------------------------------------------------------------
T = {}

T["ru"] = dict(
    lang="ru", root="", other_root="../", other_label="UA", self_label="RU",
    html_lang="ru",
    site_name="Art Detailing",
    phone1="+38 (067) 000-00-00", phone1_href="+380670000000",
    phone2="+38 (050) 000-00-00", phone2_href="+380500000000",
    email="hello@artdetailing.ua",
    address="Киев, ул. Примерная, 5",
    hours="Пн–Вс: 9:00 – 21:00",
    nav=[("Главная","index.html"),("Услуги","index.html#services"),("Галерея","gallery.html"),
         ("Цены","pricing.html"),("О нас","about.html"),("FAQ","faq.html"),("Контакты","contacts.html")],
    top_msg="Работаем по записи — привозите авто в удобное время",
    header_cta="Записаться",
    footer_rights="Все права защищены.",
    footer_tag="Ателье по уходу за автомобилем в Киеве.",
)

T["ua"] = dict(
    lang="ua", root="", other_root="ru/", other_label="RU", self_label="UA",
    html_lang="uk",
    site_name="Art Detailing",
    phone1="+38 (067) 000-00-00", phone1_href="+380670000000",
    phone2="+38 (050) 000-00-00", phone2_href="+380500000000",
    email="hello@artdetailing.ua",
    address="Київ, вул. Прикладна, 5",
    hours="Пн–Нд: 9:00 – 21:00",
    nav=[("Головна","index.html"),("Послуги","index.html#services"),("Галерея","gallery.html"),
         ("Ціни","pricing.html"),("Про нас","about.html"),("FAQ","faq.html"),("Контакти","contacts.html")],
    top_msg="Працюємо за записом — привозьте авто у зручний час",
    header_cta="Записатися",
    footer_rights="Всі права захищені.",
    footer_tag="Ательє з догляду за автомобілем у Києві.",
)

print("base loaded")

# ---------------------------------------------------------------------------
# HEAD / HEADER / FOOTER templates
# ---------------------------------------------------------------------------

def head(t, title, desc, active_css="", extra_css=""):
    root = t["root"]
    return f'''<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml;base64,{FAVICON_B64}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body>
'''

def topbar(t):
    root = t["root"]
    return f'''<div class="topbar">
  <div class="container">
    <div class="topbar-links">
      <a href="tel:{t['phone1_href']}">{icon('phone')}<span class="hidden-mobile">{t['phone1']}</span></a>
      <span class="hidden-mobile" style="opacity:.7">{t['top_msg']}</span>
    </div>
    <div style="display:flex;align-items:center;gap:22px;">
      <div class="topbar-social">
        <a href="#" aria-label="Instagram">{icon('instagram')}</a>
        <a href="#" aria-label="Facebook">{icon('facebook')}</a>
        <a href="#" aria-label="Telegram">{icon('telegram')}</a>
      </div>
      <div class="lang-switch">
        <a href="{root}index.html" class="active">{t['self_label']}</a>
        <a href="{root}{t['other_root']}index.html">{t['other_label']}</a>
      </div>
    </div>
  </div>
</div>'''

def header(t):
    root = t["root"]
    nav_links = "\n".join(f'<a href="{root}{href}">{label}</a>' for label, href in t["nav"])
    mobile_links = "\n".join(f'<a href="{root}{href}">{label}</a>' for label, href in t["nav"])
    return f'''{topbar(t)}
<header class="site-header">
  <div class="container">
    <div class="nav-row">
      <a href="{root}index.html" class="brand">{BRAND_MARK}<b>Art</b>&nbsp;<span>Detailing</span></a>
      <nav class="main-nav">
        {nav_links}
      </nav>
      <div class="nav-cta">
        <div class="nav-phone">
          <small>{"Дзвоніть" if t['lang']=='ua' else "Звоните"}</small>
          <a href="tel:{t['phone1_href']}">{t['phone1']}</a>
        </div>
        <a href="{root}contacts.html" class="btn btn-primary btn-sm hidden-mobile">{t['header_cta']}</a>
        <button class="burger" aria-label="Menu"><span></span></button>
      </div>
    </div>
  </div>
</header>
<div class="mobile-nav">
  <div class="mobile-nav-top">
    <a href="{root}index.html" class="brand" style="color:#fff;">{BRAND_MARK}<b>Art</b>&nbsp;<span>Detailing</span></a>
    <button class="mobile-nav-close" aria-label="Close">{icon('close')}</button>
  </div>
  {mobile_links}
  <div class="mobile-nav-foot">
    <a href="tel:{t['phone1_href']}">{t['phone1']}</a>
    <span>{t['address']}</span>
    <span>{t['hours']}</span>
  </div>
</div>'''

def footer(t):
    root = t["root"]
    ua = t["lang"] == "ua"
    col_services_title = "Послуги" if ua else "Услуги"
    col_company_title = "Компанія" if ua else "Компания"
    col_contacts_title = "Контакти" if ua else "Контакты"
    services = [
        ("Мийка та хімчистка" if ua else "Мойка и химчистка", "index.html#services"),
        ("Полірування кузова" if ua else "Полировка кузова", "index.html#services"),
        ("Керамічне покриття" if ua else "Керамическое покрытие", "index.html#services"),
        ("Захисна плівка" if ua else "Антигравийная плёнка", "index.html#services"),
        ("Тонування" if ua else "Тонировка", "index.html#services"),
        ("PDR" if ua else "PDR", "index.html#services"),
    ]
    company = [
        ("Про нас" if ua else "О нас", "about.html"),
        ("Галерея робіт" if ua else "Галерея работ", "gallery.html"),
        ("Ціни" if ua else "Цены", "pricing.html"),
        ("FAQ", "faq.html"),
    ]
    svc_html = "\n".join(f'<li><a href="{root}{h}">{n}</a></li>' for n, h in services)
    comp_html = "\n".join(f'<li><a href="{root}{h}">{n}</a></li>' for n, h in company)
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="{root}index.html" class="brand">{BRAND_MARK}<b>Art</b>&nbsp;<span>Detailing</span></a>
        <p>{t['footer_tag']}</p>
        <div class="footer-social">
          <a href="#" aria-label="Instagram">{icon('instagram')}</a>
          <a href="#" aria-label="Facebook">{icon('facebook')}</a>
          <a href="#" aria-label="Telegram">{icon('telegram')}</a>
        </div>
      </div>
      <div><h4>{col_services_title}</h4><ul>{svc_html}</ul></div>
      <div><h4>{col_company_title}</h4><ul>{comp_html}</ul></div>
      <div>
        <h4>{col_contacts_title}</h4>
        <ul>
          <li><a href="tel:{t['phone1_href']}">{t['phone1']}</a></li>
          <li><a href="tel:{t['phone2_href']}">{t['phone2']}</a></li>
          <li><a href="mailto:{t['email']}">{t['email']}</a></li>
          <li>{t['address']}</li>
          <li>{t['hours']}</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2018–2026 Art Detailing. {t['footer_rights']}</span>
      <a href="#top" class="back-top">{"Нагору" if ua else "Наверх"} {icon('arrow-r')}</a>
    </div>
  </div>
</footer>
<script src="{root}assets/js/main.js"></script>
</body>
</html>'''


# ---------------------------------------------------------------------------
# SERVICES
# ---------------------------------------------------------------------------
SERVICES = {}

SERVICES["ru"] = [
  dict(id="wash", ic="droplet", title="Комплексная мойка и химчистка",
       short="Бережная мойка кузова, чернение резины, чистка салона паром и экстракция — авто как из шоурума.",
       price="від 600 грн".replace("від","от"),
       bullets=["Бесконтактная мойка кузова","Мойка дисков и арок","Чистка резиновых уплотнителей",
                "Пылесос салона и багажника","Обработка пластика и кожи","Ароматизация салона"]),
  dict(id="polish", ic="sparkle", title="Полировка кузова",
       short="Убираем паутинку царапин и возвращаем родной блеск ЛКП — от лёгкой полировки до многоэтапной коррекции.",
       price="от 3 000 грн",
       bullets=["Диагностика толщины ЛКП","Абразивная и финишная полировка","Снятие царапин и потёртостей",
                "Полировка фар","Защитный воск после полировки","Работаем на станках Rupes"]),
  dict(id="ceramic", ic="shield", title="Керамическое покрытие",
       short="Керамика создаёт прочный слой защиты от химии, ультрафиолета и мелких сколов — глянец держится годами.",
       price="от 6 000 грн",
       bullets=["Подготовка и полировка кузова","1–3 слоя керамического состава","Гидрофобный эффект",
                "Защита от 1 до 5 лет","Керамика для дисков и пластика","Сертификат на покрытие"]),
  dict(id="film", ic="layers", title="Антигравийная плёнка",
       short="Прозрачная плёнка защищает кузов от сколов, гравия и мелких царапин, сохраняя заводской вид авто.",
       price="от 9 000 грн",
       bullets=["Оклейка зон риска: капот, бампер, фары","Полная оклейка кузова","Плёнки с самовосстановлением",
                "Прозрачная и матовая фактура","Гарантия на материал и работу","Без демонтажа элементов"]),
  dict(id="vinyl", ic="car", title="Виниловая плёнка",
       short="Меняем цвет и фактуру кузова без покраски — от глянца до матового шёлка, с возможностью вернуть заводской цвет.",
       price="от 3 500 грн",
       bullets=["Полная переклейка кузова","Отдельные элементы: крыша, зеркала, капот","60+ цветов и фактур",
                "Брендирование и графика","Аккуратный демонтаж без следов","Срок службы до 5–7 лет"]),
  dict(id="tint", ic="sun", title="Тонировка стёкол",
       short="Тонировка снижает нагрев салона, защищает от УФ-излучения и добавляет автомобилю завершённый вид.",
       price="от 1 500 грн",
       bullets=["Тонировка боковых и заднего стекла","Атермальная плёнка на лобовое","Любая степень затемнения",
                "Плёнки без искажения сигнала","Защита от 99% УФ","Работа по нормам ДСТУ"]),
  dict(id="pdr", ic="target", title="PDR — удаление вмятин без покраски",
       short="Выправляем вмятины от града, парковки и мелких столкновений без покраски и шпаклёвки, сохраняя заводское ЛКП.",
       price="от 800 грн",
       bullets=["Вмятины от двери и парковки","Ремонт после града","Работа без покраски",
                "Сохранение заводского ЛКП","От 40 минут на элемент","Дешевле покраски в 2 раза"]),
]

SERVICES["ua"] = [
  dict(id="wash", ic="droplet", title="Комплексна мийка та хімчистка",
       short="Дбайлива мийка кузова, чорніння гуми, чищення салону парою та екстракція — авто як із шоуруму.",
       price="від 600 грн",
       bullets=["Безконтактна мийка кузова","Мийка дисків та арок","Чищення гумових ущільнювачів",
                "Пилосос салону та багажника","Обробка пластику та шкіри","Ароматизація салону"]),
  dict(id="polish", ic="sparkle", title="Полірування кузова",
       short="Прибираємо павутинку подряпин і повертаємо рідний блиск ЛФП — від легкого полірування до багатоетапної корекції.",
       price="від 3 000 грн",
       bullets=["Діагностика товщини ЛФП","Абразивне та фінішне полірування","Зняття подряпин і потертостей",
                "Полірування фар","Захисний віск після полірування","Працюємо на верстатах Rupes"]),
  dict(id="ceramic", ic="shield", title="Керамічне покриття",
       short="Кераміка створює міцний шар захисту від хімії, ультрафіолету та дрібних сколів — глянець тримається роками.",
       price="від 6 000 грн",
       bullets=["Підготовка та полірування кузова","1–3 шари керамічного складу","Гідрофобний ефект",
                "Захист від 1 до 5 років","Кераміка для дисків і пластику","Сертифікат на покриття"]),
  dict(id="film", ic="layers", title="Захисна плівка (антигравій)",
       short="Прозора плівка захищає кузов від сколів, гравію та дрібних подряпин, зберігаючи заводський вигляд авто.",
       price="від 9 000 грн",
       bullets=["Оклеювання зон ризику: капот, бампер, фари","Повне оклеювання кузова","Плівки із самовідновленням",
                "Прозора та матова фактура","Гарантія на матеріал і роботу","Без демонтажу елементів"]),
  dict(id="vinyl", ic="car", title="Вінілова плівка",
       short="Змінюємо колір і фактуру кузова без фарбування — від глянцю до матового шовку, з можливістю повернути заводський колір.",
       price="від 3 500 грн",
       bullets=["Повне переклеювання кузова","Окремі елементи: дах, дзеркала, капот","60+ кольорів і фактур",
                "Брендування та графіка","Акуратний демонтаж без слідів","Термін служби до 5–7 років"]),
  dict(id="tint", ic="sun", title="Тонування скла",
       short="Тонування знижує нагрів салону, захищає від УФ-випромінювання і додає автомобілю завершеного вигляду.",
       price="від 1 500 грн",
       bullets=["Тонування бокового та заднього скла","Атермальна плівка на лобове","Будь-який ступінь затемнення",
                "Плівки без викривлення сигналу","Захист від 99% УФ","Робота за нормами ДСТУ"]),
  dict(id="pdr", ic="target", title="PDR — видалення вм'ятин без фарбування",
       short="Виправляємо вм'ятини від граду, парковки та дрібних зіткнень без фарбування і шпаклівки, зберігаючи заводське ЛФП.",
       price="від 800 грн",
       bullets=["Вм'ятини від дверей і парковки","Ремонт після граду","Робота без фарбування",
                "Збереження заводського ЛФП","Від 40 хвилин на елемент","Дешевше фарбування вдвічі"]),
]

# ---------------------------------------------------------------------------
# WHY US
# ---------------------------------------------------------------------------
WHY = {}
WHY["ru"] = [
  dict(ic="badge", title="Только профматериалы", text="Работаем на автохимии и составах проверенных мировых брендов — Koch Chemie, Gtechniq, Rupes, 3M."),
  dict(ic="shield", title="Оплата по результату", text="Рассчитываетесь только после того, как проверили результат и остались довольны работой."),
  dict(ic="coffee", title="Комфортное ожидание", text="Бесплатный Wi-Fi, чай и кофе в зоне отдыха — ждите авто с удобством или поработайте за ноутбуком."),
  dict(ic="phone", title="Консультация бесплатно", text="Подскажем, какой уход нужен именно вашему авто, ещё до записи — просто позвоните."),
]
WHY["ua"] = [
  dict(ic="badge", title="Тільки профматеріали", text="Працюємо на автохімії та складах перевірених світових брендів — Koch Chemie, Gtechniq, Rupes, 3M."),
  dict(ic="shield", title="Оплата за результатом", text="Розраховуєтесь лише після того, як перевірили результат і залишились задоволені роботою."),
  dict(ic="coffee", title="Комфортне очікування", text="Безкоштовний Wi-Fi, чай і кава в зоні відпочинку — чекайте на авто з комфортом або попрацюйте за ноутбуком."),
  dict(ic="phone", title="Консультація безкоштовно", text="Підкажемо, який догляд потрібен саме вашому авто, ще до запису — просто зателефонуйте."),
]

# ---------------------------------------------------------------------------
# PROCESS
# ---------------------------------------------------------------------------
PROCESS = {}
PROCESS["ru"] = [
  dict(title="Звонок или заявка", text="Рассказываете о запросе, мы советуем формат работ и называем сроки."),
  dict(title="Осмотр авто", text="Мастер оценивает состояние кузова и салона, фиксирует дефекты на фото."),
  dict(title="Согласование цены", text="Озвучиваем точную стоимость до начала работ — без сюрпризов в конце."),
  dict(title="Работы в боксе", text="Выполняем детейлинг по чек-листу, вы можете подождать на месте."),
  dict(title="Приёмка результата", text="Показываем результат при дневном свете и передаём авто с рекомендациями."),
]
PROCESS["ua"] = [
  dict(title="Дзвінок або заявка", text="Розповідаєте про запит, ми радимо формат робіт і називаємо строки."),
  dict(title="Огляд авто", text="Майстер оцінює стан кузова та салону, фіксує дефекти на фото."),
  dict(title="Погодження ціни", text="Озвучуємо точну вартість до початку робіт — без сюрпризів наприкінці."),
  dict(title="Роботи в боксі", text="Виконуємо детейлінг за чек-листом, ви можете почекати на місці."),
  dict(title="Приймання результату", text="Показуємо результат при денному світлі та передаємо авто з рекомендаціями."),
]

# ---------------------------------------------------------------------------
# STATS
# ---------------------------------------------------------------------------
STATS = {}
STATS["ru"] = [dict(n="8", suf="+", label="лет студии"), dict(n="4600", suf="+", label="авто в работе"),
                dict(n="12", suf="", label="мастеров в команде"), dict(n="97", suf="%", label="клиентов возвращаются")]
STATS["ua"] = [dict(n="8", suf="+", label="років студії"), dict(n="4600", suf="+", label="авто в роботі"),
                dict(n="12", suf="", label="майстрів у команді"), dict(n="97", suf="%", label="клієнтів повертаються")]

# ---------------------------------------------------------------------------
# BRANDS
# ---------------------------------------------------------------------------
BRANDS = ["Meguiar's", "Koch Chemie", "Gtechniq", "Rupes", "3M", "Suntek"]

# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------
FAQ = {}
FAQ["ru"] = [
  dict(q="Сколько по времени занимает детейлинг?", a="Комплексная мойка с химчисткой салона занимает 2–4 часа, полировка — от 4 часов до 2 дней в зависимости от объёма, оклейка плёнкой всего кузова — 3–5 дней. Точные сроки называем после осмотра авто."),
  dict(q="Нужно ли записываться заранее?", a="Да, мы работаем по записи, чтобы выделить на ваш автомобиль достаточно времени и бокс. Записаться можно по телефону или через форму на сайте — обычно ближайшая свободная дата в течение 2–3 дней."),
  dict(q="Можно ли подождать на месте, пока делают авто?", a="Конечно. В зоне ожидания есть Wi-Fi, чай, кофе и удобные места для работы за ноутбуком. Для длительных работ вроде оклейки плёнкой удобнее оставить авто на несколько дней."),
  dict(q="Какая гарантия на керамику и плёнку?", a="На керамические покрытия даём гарантию от 1 до 5 лет в зависимости от выбранной линейки состава, на защитные плёнки — гарантию производителя на материал плюс нашу гарантию на работу. Все условия фиксируем в акте."),
  dict(q="Что если плёнка отклеится или керамика потускнеет?", a="Такие случаи по гарантии устраняем бесплатно — записывайтесь на диагностику, мастер оценит причину и предложит решение."),
  dict(q="Работаете с автомобилями после ДТП или со СТО?", a="Да, выполняем PDR, полировку и подготовку кузова к покраске в паре со СТО-партнёрами. Можем проконсультировать, что делать в первую очередь."),
  dict(q="Как можно оплатить услуги?", a="Принимаем наличные, оплату картой и переводом на карту. Оплата — по факту выполненных работ, после того как вы проверили результат."),
]
FAQ["ua"] = [
  dict(q="Скільки часу займає детейлінг?", a="Комплексна мийка з хімчисткою салону займає 2–4 години, полірування — від 4 годин до 2 днів залежно від обсягу, оклеювання плівкою всього кузова — 3–5 днів. Точні строки називаємо після огляду авто."),
  dict(q="Чи потрібно записуватись заздалегідь?", a="Так, ми працюємо за записом, щоб виділити на ваш автомобіль достатньо часу та бокс. Записатись можна за телефоном або через форму на сайті — зазвичай найближча вільна дата протягом 2–3 днів."),
  dict(q="Чи можна почекати на місці, поки роблять авто?", a="Звісно. У зоні очікування є Wi-Fi, чай, кава та зручні місця для роботи за ноутбуком. Для тривалих робіт на кшталт оклеювання плівкою зручніше залишити авто на кілька днів."),
  dict(q="Яка гарантія на кераміку та плівку?", a="На керамічні покриття даємо гарантію від 1 до 5 років залежно від обраної лінійки складу, на захисні плівки — гарантію виробника на матеріал плюс нашу гарантію на роботу. Всі умови фіксуємо в акті."),
  dict(q="Що як плівка відклеїться або кераміка потьмяніє?", a="Такі випадки за гарантією усуваємо безкоштовно — записуйтесь на діагностику, майстер оцінить причину і запропонує рішення."),
  dict(q="Працюєте з автомобілями після ДТП або зі СТО?", a="Так, виконуємо PDR, полірування та підготовку кузова до фарбування у парі зі СТО-партнерами. Можемо проконсультувати, що робити в першу чергу."),
  dict(q="Як можна оплатити послуги?", a="Приймаємо готівку, оплату карткою та переказом на карту. Оплата — за фактом виконаних робіт, після того як ви перевірили результат."),
]

# ---------------------------------------------------------------------------
# TEAM
# ---------------------------------------------------------------------------
TEAM = {}
TEAM["ru"] = [
  dict(name="Алексей", role="Мастер детейлинга, основатель"),
  dict(name="Дмитрий", role="Специалист по плёнкам и тонировке"),
  dict(name="Артём", role="Мастер PDR"),
  dict(name="Мария", role="Администратор студии"),
]
TEAM["ua"] = [
  dict(name="Олексій", role="Майстер детейлінгу, засновник"),
  dict(name="Дмитро", role="Спеціаліст з плівок і тонування"),
  dict(name="Артем", role="Майстер PDR"),
  dict(name="Марія", role="Адміністраторка студії"),
]

# ---------------------------------------------------------------------------
# BLOG
# ---------------------------------------------------------------------------
BLOG = {}
BLOG["ru"] = [
  dict(cat="Керамика", title="Керамика или воск: что выбрать для защиты кузова",
       text="Разбираемся, чем керамическое покрытие отличается от классического воска и в каких случаях оправдана более высокая цена."),
  dict(cat="Плёнки", title="Зачем нужна антигравийная плёнка на новом авто",
       text="Рассказываем, какие зоны кузова страдают от сколов сильнее всего и как плёнка продлевает жизнь заводскому лаку."),
  dict(cat="Уход", title="Как часто нужна химчистка салона",
       text="Собрали ориентиры по частоте чистки салона в зависимости от того, как и кем используется автомобиль."),
]
BLOG["ua"] = [
  dict(cat="Кераміка", title="Кераміка чи віск: що обрати для захисту кузова",
       text="Розбираємось, чим керамічне покриття відрізняється від класичного воску і коли виправдана вища ціна."),
  dict(cat="Плівки", title="Навіщо потрібна захисна плівка на новому авто",
       text="Розповідаємо, які зони кузова найбільше страждають від сколів і як плівка подовжує життя заводському лаку."),
  dict(cat="Догляд", title="Як часто потрібна хімчистка салону",
       text="Зібрали орієнтири щодо частоти чищення салону залежно від того, як і ким використовується автомобіль."),
]

# ---------------------------------------------------------------------------
# GALLERY
# ---------------------------------------------------------------------------
GALLERY_CATS = {
  "ru": [("all","Все"),("wash","Мойка"),("polish","Полировка"),("ceramic","Керамика"),("film","Плёнка"),("pdr","PDR")],
  "ua": [("all","Всі"),("wash","Мийка"),("polish","Полірування"),("ceramic","Кераміка"),("film","Плівка"),("pdr","PDR")],
}
GALLERY_ITEMS = {
  "ru": [
    ("wash","Комплексная мойка"), ("polish","Полировка кузова"), ("ceramic","Керамика на капот"),
    ("film","Антигравийная плёнка"), ("pdr","Удаление вмятины"), ("polish","Полировка фар"),
    ("film","Оклейка винилом"), ("wash","Химчистка салона"), ("ceramic","Керамика на диски"),
    ("pdr","Ремонт после града"), ("polish","Коррекция ЛКП"), ("film","Тонировка стёкол"),
  ],
  "ua": [
    ("wash","Комплексна мийка"), ("polish","Полірування кузова"), ("ceramic","Кераміка на капот"),
    ("film","Захисна плівка"), ("pdr","Видалення вм'ятини"), ("polish","Полірування фар"),
    ("film","Оклеювання вінілом"), ("wash","Хімчистка салону"), ("ceramic","Кераміка на диски"),
    ("pdr","Ремонт після граду"), ("polish","Корекція ЛФП"), ("film","Тонування скла"),
  ],
}

# ---------------------------------------------------------------------------
# PRICING (grouped)
# ---------------------------------------------------------------------------
PRICING = {}
PRICING["ru"] = [
  dict(ic="droplet", title="Мойка и химчистка", items=[
    ("Экспресс-мойка кузова", "бесконтактная, без салона", "600 грн"),
    ("Комплексная мойка", "кузов + диски + арки + пылесос салона", "900 грн"),
    ("Локальная химчистка", "1–2 зоны: сиденье, коврик, потолок", "1 200 грн"),
    ("Полная химчистка салона", "с демонтажем сидений, экстракция", "3 500 грн"),
    ("Озонирование салона", "удаление запахов и дезинфекция", "700 грн"),
    ("Чернение резины и пластика", "наружный пластик, шины", "400 грн"),
  ]),
  dict(ic="sparkle", title="Полировка", items=[
    ("Восстановительная полировка (1 этап)", "лёгкая паутинка, освежение блеска", "3 000 грн"),
    ("Глубокая полировка (2–3 этапа)", "царапины, помутнение лака", "7 000 грн"),
    ("Полировка фар", "за пару", "800 грн"),
    ("Полировка одного элемента", "капот, дверь, крыло", "от 500 грн"),
  ]),
  dict(ic="shield", title="Керамика и защита", items=[
    ("Базовое покрытие (1 слой)", "защита 1–2 года", "6 000 грн"),
    ("Премиум покрытие (2–3 слоя)", "защита 3–5 лет", "14 000 грн"),
    ("Керамика для дисков", "комплект 4 шт.", "2 000 грн"),
    ("Керамика для пластика салона", "торпедо, двери", "1 800 грн"),
  ]),
  dict(ic="layers", title="Плёнки и тонировка", items=[
    ("Антигравийная плёнка — зоны риска", "капот, бампер, зеркала, фары", "9 000 грн"),
    ("Антигравийная плёнка — весь кузов", "полная оклейка", "от 55 000 грн"),
    ("Виниловая плёнка — элемент", "крыша, зеркала, капот", "3 500 грн"),
    ("Виниловая плёнка — весь кузов", "смена цвета целиком", "от 45 000 грн"),
    ("Тонировка 2 задних стекла", "любая степень затемнения", "1 500 грн"),
    ("Тонировка всего салона (5 стёкол)", "боковые + заднее", "3 000 грн"),
    ("Тонировка лобового стекла", "атермальная плёнка", "2 500 грн"),
  ]),
  dict(ic="target", title="PDR — вмятины без покраски", items=[
    ("Вмятина малая (до 3 см)", "1 элемент", "800 грн"),
    ("Вмятина средняя (3–10 см)", "1 элемент", "от 1 800 грн"),
    ("Ремонт после града", "полный кузов", "от 12 000 грн"),
  ]),
]
PRICING["ua"] = [
  dict(ic="droplet", title="Мийка та хімчистка", items=[
    ("Експрес-мийка кузова", "безконтактна, без салону", "600 грн"),
    ("Комплексна мийка", "кузов + диски + арки + пилосос салону", "900 грн"),
    ("Локальна хімчистка", "1–2 зони: сидіння, килимок, стеля", "1 200 грн"),
    ("Повна хімчистка салону", "з демонтажем сидінь, екстракція", "3 500 грн"),
    ("Озонування салону", "видалення запахів і дезінфекція", "700 грн"),
    ("Чорніння гуми та пластику", "зовнішній пластик, шини", "400 грн"),
  ]),
  dict(ic="sparkle", title="Полірування", items=[
    ("Відновлювальне полірування (1 етап)", "легка павутинка, освіження блиску", "3 000 грн"),
    ("Глибоке полірування (2–3 етапи)", "подряпини, помутніння лаку", "7 000 грн"),
    ("Полірування фар", "за пару", "800 грн"),
    ("Полірування одного елемента", "капот, двері, крило", "від 500 грн"),
  ]),
  dict(ic="shield", title="Кераміка та захист", items=[
    ("Базове покриття (1 шар)", "захист 1–2 роки", "6 000 грн"),
    ("Преміум покриття (2–3 шари)", "захист 3–5 років", "14 000 грн"),
    ("Кераміка для дисків", "комплект 4 шт.", "2 000 грн"),
    ("Кераміка для пластику салону", "торпедо, двері", "1 800 грн"),
  ]),
  dict(ic="layers", title="Плівки та тонування", items=[
    ("Захисна плівка — зони ризику", "капот, бампер, дзеркала, фари", "9 000 грн"),
    ("Захисна плівка — весь кузов", "повне оклеювання", "від 55 000 грн"),
    ("Вінілова плівка — елемент", "дах, дзеркала, капот", "3 500 грн"),
    ("Вінілова плівка — весь кузов", "зміна кольору повністю", "від 45 000 грн"),
    ("Тонування 2 задніх скла", "будь-який ступінь затемнення", "1 500 грн"),
    ("Тонування всього салону (5 скла)", "бокові + заднє", "3 000 грн"),
    ("Тонування лобового скла", "атермальна плівка", "2 500 грн"),
  ]),
  dict(ic="target", title="PDR — вм'ятини без фарбування", items=[
    ("Вм'ятина мала (до 3 см)", "1 елемент", "800 грн"),
    ("Вм'ятина середня (3–10 см)", "1 елемент", "від 1 800 грн"),
    ("Ремонт після граду", "повний кузов", "від 12 000 грн"),
  ]),
]

# ---------------------------------------------------------------------------
# SHARED SECTION BUILDERS
# ---------------------------------------------------------------------------

def crumbs(t, current):
    root = t["root"]
    home = "Головна" if t["lang"]=="ua" else "Главная"
    return f'<div class="crumbs"><a href="{root}index.html">{home}</a> {icon("chev-r")} <span>{current}</span></div>'

def why_section(t):
    ua = t["lang"]=="ua"
    items = "".join(f'''<div class="why-item">
      <div class="icon-wrap">{icon(w["ic"])}</div>
      <h3>{w["title"]}</h3><p>{w["text"]}</p>
    </div>''' for w in WHY[t["lang"]])
    title = "Чому обирають Art Detailing" if ua else "Почему выбирают Art Detailing"
    lede = ("Ми не женемось за швидкістю — нам важливо, щоб авто виглядало бездоганно і власник повертався знову." if ua else
            "Мы не гонимся за скоростью — нам важно, чтобы авто выглядело безупречно, а владелец возвращался снова.")
    return f'''<section class="section">
  <div class="container">
    <div class="section-head">
      <div><span class="eyebrow">{"Наші переваги" if ua else "Наши преимущества"}</span><h2>{title}</h2></div>
      <p class="lede">{lede}</p>
    </div>
    <div class="why-grid reveal">{items}</div>
  </div>
</section>'''

def services_section(t, on_index=True):
    ua = t["lang"]=="ua"
    tabs = "".join(f'''<button class="svc-tab{' is-active' if i==0 else ''}" data-target="panel-{s['id']}">
      <span class="icon-wrap">{icon(s['ic'])}</span>
      <span><b>{s['title']}</b><small>{s['price']}</small></span>
    </button>''' for i, s in enumerate(SERVICES[t["lang"]]))
    panels = "".join(f'''<div class="svc-panel{' is-active' if i==0 else ''}" id="panel-{s['id']}">
      <div class="svc-panel-media">{ph_tile(s['title'])}</div>
      <div class="svc-panel-top">
        <h3>{s['title']}</h3>
        <div class="from-price"><span>{"Ціна" if ua else "Стоимость"}</span><b>{s['price']}</b></div>
      </div>
      <p>{s['short']}</p>
      <ul class="svc-list">{"".join(f'<li>{icon("check")}{b}</li>' for b in s['bullets'])}</ul>
    </div>''' for i, s in enumerate(SERVICES[t["lang"]]))
    title = "Наші послуги" if ua else "Наши услуги"
    lede = ("Оберіть напрям — розповімо, що входить до роботи і скільки це коштуватиме." if ua else
            "Выберите направление — расскажем, что входит в работу и сколько это будет стоить.")
    anchor = ' id="services"' if on_index else ""
    return f'''<section class="section section-alt"{anchor}>
  <div class="container">
    <div class="section-head">
      <div><span class="eyebrow">{"Послуги" if ua else "Услуги"}</span><h2>{title}</h2></div>
      <p class="lede">{lede}</p>
    </div>
    <div class="svc-shell">
      <div class="svc-tabs">{tabs}</div>
      <div class="svc-panels">{panels}</div>
    </div>
  </div>
</section>'''

def process_section(t):
    ua = t["lang"]=="ua"
    items = "".join(f'<div class="process-item"><h3>{p["title"]}</h3><p>{p["text"]}</p></div>' for p in PROCESS[t["lang"]])
    title = "Як ми працюємо" if ua else "Как мы работаем"
    lede = "П'ять кроків від дзвінка до автомобіля, яким ви задоволені." if ua else "Пять шагов от звонка до автомобиля, которым вы довольны."
    return f'''<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">{"Процес" if ua else "Процесс"}</span><h2>{title}</h2></div><p class="lede">{lede}</p></div>
    <div class="process process-row reveal">{items}</div>
  </div>
</section>'''

def gallery_preview(t):
    ua = t["lang"]=="ua"
    items = GALLERY_ITEMS[t["lang"]][:8]
    cells = "".join(f'''<a href="{t['root']}gallery.html" class="gallery-cell">{ph_tile(name)}<span class="tag">{name}</span></a>''' for cat,name in items)
    title = "Останні роботи" if ua else "Последние работы"
    return f'''<section class="section section-alt">
  <div class="container">
    <div class="section-head">
      <div><span class="eyebrow">{"Портфоліо" if ua else "Портфолио"}</span><h2>{title}</h2></div>
      <a href="{t['root']}gallery.html" class="btn btn-ghost">{"Вся галерея" if ua else "Вся галерея"} {icon('arrow-r')}</a>
    </div>
    <div class="gallery-grid">{cells}</div>
  </div>
</section>'''

def brands_section(t):
    ua = t["lang"]=="ua"
    pills = "".join(f'<div class="brand-pill">{b}</div>' for b in BRANDS)
    title = "У роботі ми використовуємо" if ua else "В работе мы используем"
    return f'''<section class="section">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">{"Матеріали" if ua else "Материалы"}</span><h2>{title}</h2></div></div>
    <div class="brand-strip reveal">{pills}</div>
  </div>
</section>'''

def blog_section(t):
    ua = t["lang"]=="ua"
    cards = "".join(f'''<article class="blog-card">
      <figure>{ph_tile(b['cat'], light=True)}</figure>
      <div class="meta">{b['cat']}</div>
      <h3>{b['title']}</h3><p>{b['text']}</p>
      <span class="read">{"Читати" if ua else "Читать"} {icon('arrow-r')}</span>
    </article>''' for b in BLOG[t["lang"]])
    title = "Блог про детейлінг" if ua else "Блог о детейлинге"
    return f'''<section class="section section-alt">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow">{"Корисне" if ua else "Полезное"}</span><h2>{title}</h2></div></div>
    <div class="blog-grid">{cards}</div>
  </div>
</section>'''

def cta_band(t):
    ua = t["lang"]=="ua"
    title = "Готові повернути авто ідеальний вигляд?" if ua else "Готовы вернуть авто идеальный вид?"
    text = ("Зателефонуйте або залиште заявку — підберемо формат робіт під ваш бюджет і терміни." if ua else
            "Позвоните или оставьте заявку — подберём формат работ под ваш бюджет и сроки.")
    return f'''<section class="section" style="padding-top:0;">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="cta-actions">
        <a href="tel:{t['phone1_href']}" class="btn btn-primary">{icon('phone')} {t['phone1']}</a>
        <a href="{t['root']}contacts.html" class="btn btn-ghost" style="border-color:rgba(255,255,255,.3);color:#fff;">{t['header_cta']}</a>
      </div>
    </div>
  </div>
</section>'''

def stats_band(t):
    items = "".join(f'''<div class="stat-item"><b><span class="js-count" data-count="{s['n']}" data-suffix="{s['suf']}">0</span>{s['suf']}</b><span>{s['label']}</span></div>''' for s in STATS[t["lang"]])
    return f'''<section class="section section-dark">
  <div class="container"><div class="stat-band">{items}</div></div>
</section>'''

def contact_section(t, heading=True):
    ua = t["lang"]=="ua"
    title = "Зв'яжіться з нами" if ua else "Свяжитесь с нами"
    lede = "Залиште заявку, і ми передзвонимо протягом 15 хвилин у робочий час." if ua else "Оставьте заявку, и мы перезвоним в течение 15 минут в рабочее время."
    head_html = f'''<div class="section-head"><div><span class="eyebrow">{"Контакти" if ua else "Контакты"}</span><h2>{title}</h2></div><p class="lede">{lede}</p></div>''' if heading else ""
    name_l = "Ім'я" if ua else "Имя"
    phone_l = "Телефон"
    car_l = "Марка авто" if ua else "Марка авто"
    msg_l = "Коментар" if ua else "Комментарий"
    submit_l = "Надіслати заявку" if ua else "Отправить заявку"
    success_title = "Дякуємо!" if ua else "Спасибо!"
    success_text = "Заявку отримано, ми зателефонуємо найближчим часом." if ua else "Заявка получена, мы перезвоним в ближайшее время."
    note = ("Натискаючи кнопку, ви погоджуєтесь на обробку контактних даних для зворотного зв'язку." if ua else
            "Нажимая кнопку, вы соглашаетесь на обработку контактных данных для обратной связи.")
    return f'''<section class="section">
  <div class="container">
    {head_html}
    <div class="contact-grid">
      <div>
        <div class="contact-info-item"><span class="icon-wrap">{icon('pin')}</span><div><b>{"Адреса" if ua else "Адрес"}</b><span>{t['address']}</span></div></div>
        <div class="contact-info-item"><span class="icon-wrap">{icon('phone')}</span><div><b>{"Телефон" if ua else "Телефон"}</b><br><a href="tel:{t['phone1_href']}">{t['phone1']}</a><br><a href="tel:{t['phone2_href']}">{t['phone2']}</a></div></div>
        <div class="contact-info-item"><span class="icon-wrap">{icon('mail')}</span><div><b>Email</b><span><a href="mailto:{t['email']}">{t['email']}</a></span></div></div>
        <div class="contact-info-item"><span class="icon-wrap">{icon('clock')}</span><div><b>{"Графік роботи" if ua else "Режим работы"}</b><span>{t['hours']}</span></div></div>
        <div class="map-placeholder">{ph_tile(t['address'], light=True)}</div>
      </div>
      <div class="form-card">
        <form class="js-contact-form">
          <div class="field-row">
            <div class="field"><label>{name_l}</label><input type="text" required placeholder="{'Богдан' if ua else 'Богдан'}"></div>
            <div class="field"><label>{phone_l}</label><input type="tel" required placeholder="+380"></div>
          </div>
          <div class="field"><label>{car_l}</label><input type="text" placeholder="BMW 3 series"></div>
          <div class="field"><label>{msg_l}</label><textarea rows="4" placeholder="{'Що потрібно зробити?' if ua else 'Что нужно сделать?'}"></textarea></div>
          <button type="submit" class="btn btn-primary" style="width:100%;">{submit_l}</button>
          <p class="form-note">{note}</p>
        </form>
        <div class="form-success">
          <div class="icon-wrap">{icon('check')}</div>
          <h3>{success_title}</h3><p>{success_text}</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------------------
# PAGE: INDEX
# ---------------------------------------------------------------------------
def page_index(t):
    ua = t["lang"]=="ua"
    title = "Art Detailing — студія детейлінгу авто в Києві" if ua else "Art Detailing — студия детейлинга авто в Киеве"
    desc = ("Мийка, хімчистка, полірування, керамічне покриття, захисні плівки, тонування та PDR. Працюємо за записом у Києві." if ua else
            "Мойка, химчистка, полировка, керамическое покрытие, защитные плёнки, тонировка и PDR. Работаем по записи в Киеве.")

    hero_eyebrow = "Студія детейлінгу в Києві" if ua else "Студия детейлинга в Киеве"
    hero_h1 = "Автомобіль, який виглядає так, наче щойно зійшов з конвеєра" if ua else "Автомобиль, который выглядит так, будто только сошёл с конвейера"
    hero_lede = ("Миємо, полірувальник, захищаємо кераміко та плівкою. Працюємо повільно й акуратно — тому що поспіх це головний ворог гарного детейлінгу." if ua else
                 "Моем, полируем, защищаем керамикой и плёнкой. Работаем медленно и аккуратно — потому что спешка это главный враг хорошего детейлинга.")
    badge_b = "8 років" if ua else "8 лет"
    badge_s = "на ринку Києва" if ua else "на рынке Киева"
    trust1_b, trust1_s = ("4600+", "авто в роботі" if ua else "авто в работе")
    trust2_b, trust2_s = ("12", "майстрів у команді" if ua else "мастеров в команде")
    trust3_b, trust3_s = ("97%", "клієнтів повертаються" if ua else "клиентов возвращаются")

    body = f'''{header(t)}
<main>
  <section class="hero" id="top">
    <div class="container hero-grid">
      <div class="hero-copy">
        <span class="eyebrow">{hero_eyebrow}</span>
        <h1>{hero_h1}</h1>
        <p class="lede">{hero_lede}</p>
        <div class="hero-actions">
          <a href="{t['root']}contacts.html" class="btn btn-primary">{t['header_cta']} {icon('arrow-r')}</a>
          <a href="{t['root']}pricing.html" class="btn btn-ghost">{"Дивитись ціни" if ua else "Смотреть цены"}</a>
        </div>
        <div class="hero-trust">
          <div><b>{trust1_b}</b><span>{trust1_s}</span></div>
          <div><b>{trust2_b}</b><span>{trust2_s}</span></div>
          <div><b>{trust3_b}</b><span>{trust3_s}</span></div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-art">{HERO_SVG}<div class="shine"></div></div>
        <div class="hero-badge">{icon('badge')}<div><b>{badge_b}</b><span>{badge_s}</span></div></div>
      </div>
    </div>
  </section>

  <div class="marquee-wrap">
    <div class="marquee">
      {"".join(f'<span>{b}</span>' for b in (BRANDS*2))}
    </div>
  </div>

  {why_section(t)}
  {services_section(t, on_index=True)}
  {process_section(t)}

  <section class="section section-alt">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">{"До / Після" if ua else "До / После"}</span><h2>{"Побачте різницю самі" if ua else "Увидьте разницу сами"}</h2></div>
        <p class="lede">{"Потягніть повзунок, щоб порівняти стан авто до та після роботи наших майстрів." if ua else "Потяните ползунок, чтобы сравнить состояние авто до и после работы наших мастеров."}</p>
      </div>
      <div class="ba reveal">
        <div class="ph-tile" style="position:absolute;inset:0;">{icon('car')}</div>
        <div class="ba-after"><div class="ph-tile light" style="position:absolute;inset:0;">{icon('sparkle')}</div></div>
        <span class="ba-label before">{"До" if ua else "До"}</span>
        <span class="ba-label after">{"Після" if ua else "После"}</span>
        <div class="ba-line"></div>
        <div class="ba-handle">{icon('chev-r')}</div>
      </div>
    </div>
  </section>

  {gallery_preview(t)}
  {stats_band(t)}
  {brands_section(t)}
  {blog_section(t)}
  {cta_band(t)}
</main>
{footer(t)}'''
    return head(t, title, desc) + body

# ---------------------------------------------------------------------------
# PAGE: PRICING
# ---------------------------------------------------------------------------
def page_pricing(t):
    ua = t["lang"]=="ua"
    title = "Ціни на детейлінг — Art Detailing" if ua else "Цены на детейлинг — Art Detailing"
    desc = "Прайс на мийку, полірування, кераміку, плівки, тонування та PDR." if ua else "Прайс на мойку, полировку, керамику, плёнки, тонировку и PDR."
    groups = ""
    for g in PRICING[t["lang"]]:
        rows = "".join(f'''<div class="price-row">
          <div class="price-row-name"><b>{n}</b><p>{d}</p></div>
          <div class="price-row-cost">{p}</div>
        </div>''' for n,d,p in g["items"])
        groups += f'''<div class="price-group">
          <div class="price-group-head"><span class="icon-wrap">{icon(g['ic'])}</span><h3>{g['title']}</h3></div>
          <div class="price-table">{rows}</div>
        </div>'''
    note = ("Фінальна вартість залежить від стану авто та обсягу робіт і узгоджується до початку. Ціни вказані в гривнях і є орієнтовними." if ua else
            "Финальная стоимость зависит от состояния авто и объёма работ и согласуется до начала. Цены указаны в гривнах и являются ориентировочными.")
    body = f'''{header(t)}
<main>
  <section class="page-hero">
    <div class="container">
      {crumbs(t, "Ціни" if ua else "Цены")}
      <h1>{"Прайс-лист" if ua else "Прайс-лист"}</h1>
      <p class="lede" style="margin-top:16px;">{"Базові ціни на основні послуги. Точну вартість підтвердимо після огляду авто." if ua else "Базовые цены на основные услуги. Точную стоимость подтвердим после осмотра авто."}</p>
    </div>
  </section>
  <section class="section" style="padding-top:0;">
    <div class="container">
      {groups}
      <div class="price-note">{icon('info')}<span>{note}</span></div>
    </div>
  </section>
  {cta_band(t)}
</main>
{footer(t)}'''
    return head(t, title, desc) + body

# ---------------------------------------------------------------------------
# PAGE: GALLERY
# ---------------------------------------------------------------------------
def page_gallery(t):
    ua = t["lang"]=="ua"
    title = "Галерея робіт — Art Detailing" if ua else "Галерея работ — Art Detailing"
    desc = "Фото робіт студії Art Detailing: мийка, полірування, кераміка, плівки, PDR." if ua else "Фото работ студии Art Detailing: мойка, полировка, керамика, плёнки, PDR."
    chips = "".join(f'<button class="chip{" is-active" if c=="all" else ""}" data-filter="{c}">{n}</button>' for c,n in GALLERY_CATS[t["lang"]])
    cells = "".join(f'''<div class="gallery-cell" data-cat="{cat}">{ph_tile(name)}<span class="tag">{name}</span></div>''' for cat,name in GALLERY_ITEMS[t["lang"]])
    body = f'''{header(t)}
<main>
  <section class="page-hero">
    <div class="container">
      {crumbs(t, "Галерея")}
      <h1>{"Наші роботи" if ua else "Наши работы"}</h1>
      <p class="lede" style="margin-top:16px;">{"Реальні кейси студії — фото додаємо після кожного проєкту." if ua else "Реальные кейсы студии — фото добавляем после каждого проекта."}</p>
    </div>
  </section>
  <section class="section" style="padding-top:0;">
    <div class="container">
      <div class="gallery-filter">{chips}</div>
      <div class="gallery-grid">{cells}</div>
    </div>
  </section>
  {cta_band(t)}
</main>
{footer(t)}'''
    return head(t, title, desc) + body

# ---------------------------------------------------------------------------
# PAGE: FAQ
# ---------------------------------------------------------------------------
def page_faq(t):
    ua = t["lang"]=="ua"
    title = "Питання та відповіді — Art Detailing" if ua else "Вопросы и ответы — Art Detailing"
    desc = "Відповіді на популярні питання про детейлінг, гарантію та запис." if ua else "Ответы на популярные вопросы о детейлинге, гарантии и записи."
    items = "".join(f'''<div class="faq-item">
      <button class="faq-q"><span>{f['q']}</span><span class="plus"></span></button>
      <div class="faq-a"><div class="faq-a-inner">{f['a']}</div></div>
    </div>''' for f in FAQ[t["lang"]])
    body = f'''{header(t)}
<main>
  <section class="page-hero">
    <div class="container">
      {crumbs(t, "FAQ")}
      <h1>{"Часті запитання" if ua else "Частые вопросы"}</h1>
      <p class="lede" style="margin-top:16px;">{"Не знайшли відповідь? Зателефонуйте — проконсультуємо безкоштовно." if ua else "Не нашли ответ? Позвоните — проконсультируем бесплатно."}</p>
    </div>
  </section>
  <section class="section" style="padding-top:0;">
    <div class="container" style="max-width:920px;">
      <div class="faq-list">{items}</div>
    </div>
  </section>
  {cta_band(t)}
</main>
{footer(t)}'''
    return head(t, title, desc) + body

# ---------------------------------------------------------------------------
# PAGE: ABOUT
# ---------------------------------------------------------------------------
def page_about(t):
    ua = t["lang"]=="ua"
    title = "Про нас — Art Detailing" if ua else "О нас — Art Detailing"
    desc = "Історія студії Art Detailing, команда та принципи роботи." if ua else "История студии Art Detailing, команда и принципы работы."

    story_h = "Почалось із гаража на двох майстрів" if ua else "Начиналось с гаража на двух мастеров"
    story_p1 = ("Art Detailing відкрився у 2018 році як невелика майстерня на Куренівці. Перші клієнти приїжджали за порадою знайомих — ми обіцяли не швидкість, а результат, і поступово це стало нашим принципом." if ua else
                "Art Detailing открылся в 2018 году как небольшая мастерская на Куренёвке. Первые клиенты приезжали по совету знакомых — мы обещали не скорость, а результат, и постепенно это стало нашим принципом.")
    story_p2 = ("Сьогодні це студія повного циклу: від експрес-мийки до бронювання кузова плівкою. Але підхід не змінився — кожне авто отримує стільки часу, скільки потрібно, а не скільки заплановано в графіку." if ua else
                "Сегодня это студия полного цикла: от экспресс-мойки до бронирования кузова плёнкой. Но подход не изменился — каждое авто получает столько времени, сколько нужно, а не сколько запланировано в графике.")
    ticks = (["Власний бокс на 4 поста у центрі Києва","Навчання майстрів у сертифікованих центрах","Прозорий акт виконаних робіт після кожного візиту"] if ua else
             ["Собственный бокс на 4 поста в центре Киева","Обучение мастеров в сертифицированных центрах","Прозрачный акт выполненных работ после каждого визита"])
    tick_html = "".join(f'<li>{icon("check")}{x}</li>' for x in ticks)

    team_title = "Команда, яка любить свою справу" if ua else "Команда, которая любит своё дело"
    team_cards = "".join(f'''<div class="team-card">
      <figure>{ph_tile("", light=True)}</figure>
      <b>{p['name']}</b><span>{p['role']}</span>
    </div>''' for p in TEAM[t["lang"]])

    body = f'''{header(t)}
<main>
  <section class="page-hero">
    <div class="container">
      {crumbs(t, "Про нас" if ua else "О нас")}
      <h1>{"Про студію Art Detailing" if ua else "О студии Art Detailing"}</h1>
    </div>
  </section>
  <section class="section" style="padding-top:0;">
    <div class="container">
      <div class="split reveal">
        <div class="split-media">{ph_tile("Art Detailing")}</div>
        <div>
          <span class="eyebrow">{"Наша історія" if ua else "Наша история"}</span>
          <h2>{story_h}</h2>
          <p class="lede" style="margin-top:16px;max-width:52ch;">{story_p1}</p>
          <p class="lede" style="margin-top:14px;max-width:52ch;">{story_p2}</p>
          <ul class="tick-list">{tick_html}</ul>
        </div>
      </div>
    </div>
  </section>
  {stats_band(t)}
  <section class="section">
    <div class="container">
      <div class="section-head"><div><span class="eyebrow">{"Команда" if ua else "Команда"}</span><h2>{team_title}</h2></div></div>
      <div class="team-grid">{team_cards}</div>
    </div>
  </section>
  {brands_section(t)}
  {cta_band(t)}
</main>
{footer(t)}'''
    return head(t, title, desc) + body

# ---------------------------------------------------------------------------
# PAGE: CONTACTS
# ---------------------------------------------------------------------------
def page_contacts(t):
    ua = t["lang"]=="ua"
    title = "Контакти — Art Detailing" if ua else "Контакты — Art Detailing"
    desc = "Адреса, телефони та форма запису студії Art Detailing у Києві." if ua else "Адрес, телефоны и форма записи студии Art Detailing в Киеве."
    body = f'''{header(t)}
<main>
  <section class="page-hero">
    <div class="container">
      {crumbs(t, "Контакти" if ua else "Контакты")}
      <h1>{"Як нас знайти" if ua else "Как нас найти"}</h1>
    </div>
  </section>
  <div style="padding-top:0;">{contact_section(t, heading=False)}</div>
</main>
{footer(t)}'''
    return head(t, title, desc) + body

# ---------------------------------------------------------------------------
# WRITE
# ---------------------------------------------------------------------------
PAGES = [
    ("index.html", page_index),
    ("pricing.html", page_pricing),
    ("gallery.html", page_gallery),
    ("faq.html", page_faq),
    ("about.html", page_about),
    ("contacts.html", page_contacts),
]

for lang, out_dir in [("ua", ROOT), ("ru", os.path.join(ROOT, "ru"))]:
    os.makedirs(out_dir, exist_ok=True)
    t = dict(T[lang])
    if lang == "ru":
        t["root"] = ""  # ru pages live one level deep; assets referenced with ../
    for fname, fn in PAGES:
        html = fn(t)
        if lang == "ru":
            html = html.replace('href="assets/', 'href="../assets/').replace('src="assets/', 'src="../assets/')
        with open(os.path.join(out_dir, fname), "w", encoding="utf-8") as f:
            f.write(html)
    print(f"wrote {lang} pages")

print("BUILD OK")

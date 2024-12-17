wiki_title = "//h1[@id='Добро_пожаловать_в_Википедию,']"#здесь заголовок википедии, я думаю вряд ли он поменяется
#к тому же у него есть id а у всего остального над ним нет. Тогда это норм к нему привязаться?
pdf_download = "//*[@id='coll-download-as-rl']//a"#адаптирован
favorite_img = "//*[@id='main-tfa']//*//figure[contains(@class, 'mw-halign-right')]//a[contains(@class, 'mw-file-description')]//img"
enter_comon_text = "//*[@id='mw-content-text']//table[contains(@align, 'center')]//tr[4]//td[2]//p/tt"#ближайшая надежная привязка это div с id
#в таблице кроме align и style тоже ничего нет. А теги в самой таблице вообще без атрибутов
lang_settings = "//*[@id='p-lang']/button"#короче тогда везде, где есть точный идентификатор, типа id - я ставлю *?
login_label = "//*[@for='wpName1']//span"#как понимаю for спеииально сделали?
login_field = "//*[@id='wpName1']"
pass_label = "//*[@for='wpPassword1']"
pass_field = "//*[@id='wpPassword1']"
check_box = "//*[@id='wpRemember']"
enter_button = "//*[@id='wpLoginAttempt']"
login_help = "//*[contains(@class, 'mw-userlogin-help')]//a"#То есть смотри - лучше указать часть класса, чем целиком весь?
#класс целиком - mw-htmlform-field-HTMLInfoField mw-form-related-link-container mw-userlogin-help cdx-field
#я указываю только как бы логическую для этого элемента часть(помощь с логином - mw-userlogin-help). Потому-что все остальное может измениться. Правильно понял?
#но в следующем локаторе как раз нет этой логической части в атрибуте
pass_reset = "//div[@class='mw-htmlform-field-HTMLInfoField mw-form-related-link-container cdx-field']//div//a"#здесь класс почти точно такой же
#mw-htmlform-field-HTMLInfoField mw-form-related-link-container cdx-field
#тогда здесь как, целиком только, правильно?
join = "//*[@id='mw-createaccount-join']"#адаптирован

wiki_title = "//h1[@id='Добро_пожаловать_в_Википедию,']//span"#здесь заголовок википедии, я думаю вряд ли он поменяется
#к тому же у него есть id а у всего остального над ним нет. Тогда это норм к нему привязаться?
pdf_download = "//li[@id='coll-download-as-rl']//a"#адаптирован
favorite_img = "//div[@id='main-tfa']//div//figure//a//img"#адаптирован???
enter_comon_text = "//tbody//tr[4]//td[2]//p//tt"#тут ничего не поделаешь, в таблице у тегов никаких атрибутов нет(
lang_settings = "//nav[@id='p-lang']/button"
login_label = "//label[@for='wpName1']//span"#адаптирован
login_field = "//input[@id='wpName1']"#адаптирован
pass_label = "//label[@for='wpPassword1']//span"#адаптирован
pass_field = "//input[@id='wpPassword1']"#адаптирован
check_box = "//input[@id='wpRemember']"#адаптирован
enter_button = "//button[@id='wpLoginAttempt']"#адаптирован
login_help = "//div[@class='mw-htmlform-field-HTMLInfoField mw-form-related-link-container mw-userlogin-help cdx-field']//div//a"#здесь тоже,
# кроме атрибута class у тегов больше ничего нет, и в следующем локаторе также
pass_reset = "//div[@class='mw-htmlform-field-HTMLInfoField mw-form-related-link-container cdx-field']//div//a"#адаптирован
join = "//a[@id='mw-createaccount-join']"#адаптирован

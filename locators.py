from selenium.webdriver.common.by import By

class BurgersLocators:
    #Cтраница Регистрации
    NAME_FIELD = (By.XPATH, "//label[text()='Имя']/ancestor::fieldset//input") #Поле Имя
    EMAIL_REG_FIELD = (By.XPATH, "//label[text()='Email']/ancestor::fieldset//input") #Поле Email
    PASSWORD_REG_FIELD = (By.XPATH, "//label[text()='Пароль']/ancestor::fieldset//input") #Поле Пароль
    SIGN_UP_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") #Кнопка Зарегистрироваться
    PASSWORD_ERROR = (By.XPATH, "//p[@class='input__error text_type_main-default']")  #Cообщение об ошибке пароля
    LOGIN_BUTTON_FOOTER = (By.XPATH, '//a[contains(@href,"/login")]') #Кнопка Войти

    #Страница Профиля
    PROFILE_NAME = (By.XPATH, "//label[contains(text(),'Имя')]/ancestor::li") #Поле Имя
    SIGN_IN_TITLE = (By.XPATH, "//h2") #
    CONSTRUKTOR_HEADER = (By.XPATH,'//p[contains(text(),"Конструктор")]' ) #Кнопка Конструктор
    LOGO_HEADER = (By.XPATH,'//div[@class="AppHeader_header__logo__2D0X2"]') #Лого
    LOGOUT_BUTTON = (By.XPATH, '//button[contains(text(), "Выход")]') #Кнопка Выход

    #Страница Авторизации
    EMAIL_AUTH_FIELD = (By.XPATH, "//label[contains(text(),'Email')]/ancestor::fieldset//input") #Поле Email
    PASSWORD_AUTH_FIELD = (By.XPATH, "//label[contains(text(),'Пароль')]/../input") #Поле Пароль
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") #Кнопка Войти
    FORGOT_PASSWORD = (By.XPATH, "//a[contains(@href,'/forgot-password')]") #Кнопка Восстановить пароль

    #Главная Страница
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]") #Кнопка Личный Кабинет
    AUTH_BUTTON_MAIN_PAGE = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]") #Кнопка Войти в аккаунт
    ORDER_BUTTON = (By.XPATH, "//button[contains (text(),'Оформить заказ')]") #Кнопка Оформить заказ

    BUNS = (By.XPATH, ".//span[text() = 'Булки']/parent::div") #Таб Булки
    SAUCE = (By.XPATH, ".//span[text() = 'Соусы']/parent::div") #Таб Соусы
    SAUCE_CONTAINER = (By.XPATH, '//p[contains (text(),"Соус Spicy-X")]') #Элемент в Соусах
    FILLINGS = (By.XPATH, ".//span[text() = 'Начинки']/parent::div") #Таб Начинки
    ACTIVE_STATE_BUTTON = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'





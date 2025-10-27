from dotenv import load_dotenv
load_dotenv()
import os
login_mail = os.getenv('LOGIN')
pass_mail = os.getenv('PASSWORD')
letter = ("""\
From: {s}
To: {r}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {f}! {m} приглашает тебя на сайт {w}!

{w} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {w}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {w}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.\
""")
receiver = 'ваш e-mail' # не заполнена почта
website = 'https://dvmn.org/profession-ref-program/s.vinogradov.28/Stnbw/'
friend_name = 'Александр'
my_name = 'Игорь'
letter = letter.format(s=login_mail, r=receiver, w=website, f=friend_name, m=my_name)
letter = letter.encode('UTF-8')
import smtplib
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login_mail, pass_mail)
server.sendmail(login_mail, receiver, letter)
server.quit()
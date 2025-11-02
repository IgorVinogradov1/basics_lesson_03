import os
import smtplib


from dotenv import load_dotenv
load_dotenv()
login_mail = os.getenv('LOGIN')
pass_mail = os.getenv('PASSWORD')
receiver = 'ваш e-mail' # не заполнена почта
website = 'https://dvmn.org/profession-ref-program/s.vinogradov.28/Stnbw/'
friend_name = 'Александр'
my_name = 'Игорь'
header = f'From: {login_mail}\nTo: {receiver}\nSubject: Приглашение!\nContent-Type: text/plain; charset="UTF-8";\n\n'
body_letter = f'''\
Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''
letter = header + body_letter
letter = letter.encode('UTF-8')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login_mail, pass_mail)
server.sendmail(login_mail, receiver, letter)
server.quit()
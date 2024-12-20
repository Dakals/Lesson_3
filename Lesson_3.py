import os
import smtplib

from dotenv import load_dotenv

load_dotenv()

website = 'https://dvmn.org/profession-ref-program/dakals/Xlbmu/'
friend_name = 'Иван'
my_name = 'Иван'
mail_input = "s.kirill.work@gmail.com"

Letter = '''From: %MyMail%
To: mail_input
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8";


Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл'''.replace('%website%', website).replace('%friend_name%', friend_name).replace('%my_name%', my_name).replace('%MyMail%', os.getenv('LOGIN').replace('mail_input', mail_input))
Letter = Letter.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))
server.sendmail(os.getenv('LOGIN'), mail_input, Letter)
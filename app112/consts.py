GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'

GENDER_CHOICE = (
        (GENDER_MALE, 'Мужчина'),
        (GENDER_FEMALE, 'Женщина')
    )

STATUS_IN_WORK = 'In_work'
STATUS_COMPLETED = 'Completed'

STATUS_CHOICE = (
        (STATUS_IN_WORK, 'В работе'),
        (STATUS_COMPLETED, 'Завершено')
    )

# Переделать как с status_choice
TRAFFIC_ACCIDENT = 'ДТП'
THEFT = 'Кража'
ATTACK = 'Нападение'
INJURY = 'Травма'
FIRE = 'Пожар'
THREAT_OF_TERRORISM = 'Угроза терроризма'
OTHER = 'Другое'

INCIDENT_CHOICES = (
    (TRAFFIC_ACCIDENT, TRAFFIC_ACCIDENT),
    (THEFT, THEFT),
    (ATTACK, ATTACK),
    (INJURY, INJURY),
    (FIRE, FIRE),
    (THREAT_OF_TERRORISM, THREAT_OF_TERRORISM),
    (OTHER, OTHER)
)
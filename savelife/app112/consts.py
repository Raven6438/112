GENDER_CHOICE = (
        ('m', 'Мужчина'),
        ('w', 'Женщина')
    )

STATUS_CHOICE = (
        ('in work', 'В работе'),
        ('completed', 'Завершено')
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
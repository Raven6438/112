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

INCIDENT_TRAFFIC_ACCIDENT = 'Traffic_accident'
INCIDENT_THEFT = 'Theft'
INCIDENT_ATTACK = 'Attack'
INCIDENT_INJURY = 'Injury'
INCIDENT_FIRE = 'Fire'
INCIDENT_THREAT_OF_TERRORISM = 'Threat_of_terrorism'
INCIDENT_OTHER = 'Other'

INCIDENT_CHOICES = (
    (INCIDENT_TRAFFIC_ACCIDENT, 'ДТП (Дорожно-транспортное происшествие)'),
    (INCIDENT_THEFT, 'Кража'),
    (INCIDENT_ATTACK, 'Нападение'),
    (INCIDENT_INJURY, 'Травма'),
    (INCIDENT_FIRE, 'Пожар'),
    (INCIDENT_THREAT_OF_TERRORISM, 'Угроза терроризма'),
    (INCIDENT_OTHER, 'Другое')
)

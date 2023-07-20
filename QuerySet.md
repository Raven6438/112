Сохранение объектов в БД:
1. Сохр. несколько объектов моделей "Экстр. службы", "Обращения", "Заявители" с помощью ".objects.create()" и save()
	a) Applicant.objects.create(surname='Сергеев', name='Сергей', phone=79173345566, gender='m', descr_state_health='Сердечный приступ')
	Applicant.objects.create(surname='Ялунин', name='Евгений', phone=79173344422, gender='m')
	
	б) pers = Applicant()
	pers.surname = 'Андреев'
	pers.name = 'Семен'
	pers.patronymic = 'Андреевич'
	pers.phone = 88005553555
	pers.save()

2. Создать "Обращение" через менеджер запросов от объекта "Заявитель"
	applicant = Applicant.objects.filter(name='Семен').first()
	Result: <Applicant: Семен>
	
	applicant.appeals.create(count_injured=2) 
	Result: <Appeal: e3ae18aa-59b8-48d1-981e-dbed56e7b65d>

3. Доб. объекту "Обращения" несколько "Экстр. служб" с помощью add() и set().
	serv = EmergencyService.objects.all()
	Result: <QuerySet [<EmergencyService: Полиция>, <EmergencyService: Скорая помощь>, <EmergencyService: Пожарная служба>]>
	
	appeal = Appeal.objects.get(pk=1)
	Result: <Appeal: e3ae18aa-59b8-48d1-981e-dbed56e7b65d>
	
	appeal.service.add(serv[0])
	Result: <QuerySet [<EmergencyService: Полиция>]>
	
	appeal.service.set([serv[1], serv[2]])
	Result: <QuerySet [<EmergencyService: Скорая помощь>, <EmergencyService: Пожарная служба>]>

Запросы в БД
1. Получ. объект "Заявителя" с id=1 тремя способами
	Applicant.objects.get(pk=1)
	Applicant.objects.filter(pk=1).first()
	Applicant.objects.filter(pk=1)[0]
	Result: <Applicant: Иван>

2. Получ. все "Обращения" у объекта "Заявитель" двумя способ.
	pers = Applicant.objects.get(pk=1)
	а) pers.appeals.all()
	б) Appeal.objects.filter(applicant = pers.id)
	Result: <QuerySet [<Appeal: 7d7db990-fa82-4021-9576-b6e1c1ac27ed>]>

3. Получ. первые 3 "Экстр. службы"
	EmergencyService.objects.all()[:3]
	Result:

4. Получ. последнние 5 "Заявителей"
	Applicant.objects.all().reverse()[:5]
	Result:

5. Получ. самое старое и самое новое обращение 2 способ (latest, earliest, order_by)
	Appeal.objects.latest('date')           - самое новое обращение
	Appeal.objects.earliest('date')         - самое старое обращение
	Appeal.objects.order_by('date').first() - самое старое обращение
	Appeal.objects.order_by('date').last()  - самое новое обращение
	Result:

6. Получ. каждое 2 обращение
	Appeal.objects.all()[::2]
	Result:

7. Если дважды проитерироваться по полученному Queryset'у, то сколько будет сделано обращений в БД?
    С помощью конструкции len(connection.queries) можно проверить кол-во запросов в БД.
    Для сброса испол. reset_queries() из django.db.

    >>> reset_queries()
    >>> len(connection.queries)
    0
    >>> a = Appeal.objects.all()[::2]
    >>> for i in range(2):
    ...     a
    ...
    [<Appeal: e3ae18aa-59b8-48d1-981e-dbed56e7b65d>, <Appeal: 7d7db990-fa82-4021-9576-b6e1c1ac27ed>, <Appeal: fa185186-d3df-4eca-b679-bd0aa19e1e9a>]
    [<Appeal: e3ae18aa-59b8-48d1-981e-dbed56e7b65d>, <Appeal: 7d7db990-fa82-4021-9576-b6e1c1ac27ed>, <Appeal: fa185186-d3df-4eca-b679-bd0aa19e1e9a>]
    >>> len(connection.queries)
    1
    В случае, когда через полученный объект a[0] в цикле мы обращаемся к другой связанной таблице, произойдет еще одно
    и только одно обращение в БД.
    >>> for i in range(2):
    ...     a[0].applicant
    ...
    <Applicant: Семен>
    <Applicant: Семен>
    >>> len(connection.queries)
    2

8. Вывести общее число Обращений
	Appeal.objects.count()
	Result:

9. Вывести случайное обращение
	Appeal.objects.order_by('?').first()
	Result:

Фильтрация
1. Получ. обращение заявителя с id=1
	Appeal.objects.filter(applicant_id = 1).first()
	Result:

2. Получ. всех заявителей по опред. полу и без обращ.
	Applicant.objects.exclude(id__in=Appeal.objects.filter(gender='m').values('applicant_id', flat=True))
	Result:

3. Отсортировать всех заявителей по id 
	Applicant.objects.order_by('id')
	Applicant.objects.order_by('-id')
	Result:

4. Получ. всех несовершеннолетних заявителей
    from django.utils import timezone
    from datetime import timedelta
	Applicant.objects.filter(birthday__gte=timezone.now() - timedelta(weeks=936))
	Result:

5. Получить всех совершеннолетних заявителей
    from django.utils import timezone
    from datetime import timedelta
	Applicant.objects.filter(birthday__lte=timezone.now() - timedelta(weeks=936))
	Result:

6. Узнать, есть ли вообще какие-либо заявители? Например, у которых состояние здоровья НЕ "Практически здоров"
	Applicant.objects.exclude(descr_state_health = 'Практически здоров').exists()
	Applicant.objects.filter(~Q(descr_state_health = 'Практически здоров')).exists()
	Result:

7. Узнать, есть ли заявители с похожими именами (например, Евгений и Евгения)
	Applicant.objects.filter(name__startswith='Евгени')
	Result:

8. Получ. все обращения, кроме у которых нет назнач. служб
	Appeal.objects.filter(service__isnull=True)
	Result:

9. Вывести дату самого первого обращений, у которых призванна служба с кодом 03
	Appeal.objects.filter(service__service_code = '03').earliest('date')
	Result:

10. Получ. все обращения, созданные до опред. даты
	Appeal.objects.filter(date__lt=datetime.date(2022, 10, 21))
	Result:

11. Получ. всех заявителей без фото или/и без телефона
    from django.db.models import Q
	Applicant.objects.filter(photo__isnull=True, phone__isnull=True)
	Applicant.objects.filter(Q(photo__isnull=True) | Q(phone__isnull=True))
	Result:

12. Получ. всех заявителей с определ. кодом оператора 917
	Applicant.objects.filter(phone__contains=917)
	Result:

13. Получ. результаты объедин., пересеч. и разницы двух предыдущих запросов.
    Не работаю с SQLite
    Объединение - Applicant.objects.filter(Q(Q(photo='') | Q(phone__isnull=True)) & Q(phone__contains=917))
    Пересечение - Applicant.objects.filter(Q(photo='') | Q(phone__isnull=True) | Q(phone__contains=917))

14. Вывести все обращения за опред период
	Appeal.objects.filter(date__date__range=(date(2022,10,10), date(2022,10,21)))
	Result: <QuerySet []>

15. Получ. кол-во заявителей без номера телефона
	Applicant.objects.filter(phone__isnull=True).count()
	Result: 0

16. Вывести все уникальные записи заявителей
	Applicant.objects.all().distinct()
	Result: <QuerySet [<Applicant: John>, <Applicant: d>, <Applicant: person>, <Applicant: person>, <Applicant: Евгения>,
	<Applicant: Семен>, <Applicant: Иван>, <Applicant: Василий>, <Applicant: Андрей>, <Applicant: Сергей>, <Applicant: Евгений>]>

17. Получ. все обращения, у которых в описании есть ключ. слово в любом регистре
	Appeal.objects.filter(descr_state_health__icontains='Практически')
	Result:

18. Получ. номера тлф всех заявителей
	Applicant.objects.values_list('phone', flat=True)
	Result: <QuerySet [89877873212, 12, 43214321, 11, 3443223442, 88005553555, 79179998009, 3456754, 3123, 79173345566, 79173344422]>

19. Выбрать всех заявителей, и вывести все поля, кроме "состояния здоровья"
    Applicant.objects.values('surname', 'name', 'patronymic', 'birthday', 'gender', 'phone', 'photo')
    Result: <QuerySet [{'surname': 'Wick', 'name': 'John', 'patronymic': '', 'birthday': datetime.datetime(1980, 12, 12, 0, 0, tzinfo=datetime.timezone.utc), 'gender'
: 'm', 'phone': 89877873212, 'photo': ''}, ...]>

20. Получ. все службы используя SQL-запрос - RawQuerySet -> QuerySet
    for i in EmergencyService.objects.raw("SELECT * FROM app112_emergencyservice"):
        print(i)

	Result: Полиция
            Скорая помощь
            Пожарная служба


1. Вывести или создать заявителя с номером тлф 12341234
   Applicant.objects.get_or_create(phone=12341234)
   Result: (<Applicant: Василий>, False)

2. Изменить номер тлф заявителя с номером тлф 12341234 на другой, если такого заявителя нет, то создать его
   man, _ = Applicant.objects.update_or_create(phone=12341234, defaults={'surname':'new', 'name': 'person', 'phone': 43214321})

3. Создать сразу несколько заявителей
   a = Applicant.objects.bulk_create([
       Applicant(...),
       Applicant(...)
   ])
4. Изменить несколько заявителей: сост. здоровья на "полностью здоров"
   objs = [Applicant.objects.get(pk=i) for i in range(1,3)] #id=1 id=2
   for i in objs:
       i.descr_state_health = 'Полностью здоров'
   Applicant.objects.bulk_update(objs, ['descr_state_health'])
   Result: 2

5. Вывести имя заявителя у которого какое-либо обращение в один запрос (Оптизация запросов)
    Appeal.objects.select_related("applicant").order_by('?').first().applicant.name
    Result: 'Евгения'

6. Вывести список обращений с указанием задействованных служб в формате (№ обращ, список кодов служб).
   Не более 2 запросов (Переделать с оптимизацией запросов)

   appeals = []
   for appeal in Appeal.objects.prefetch_related('service'):
       codes = [service.service_code for service in appeal.service.all()]
       appeals.append({'appeal': appeal.number, 'codes':codes})
   appeals
   Result: [{'appeal': UUID('e3ae18aa-59b8-48d1-981e-dbed56e7b65d'), 'codes': ['03', '01']}, ...]
	
7. Вывести все значения дат создания происшествий(Обращений). Даты добавить в список
   Appeal.objects.values_list('date')
   Result: <QuerySet [(datetime.datetime(2022, 10, 26, 13, 39, 18, 750358, tzinfo=datetime.timezone.utc),), ...]>

8. Создать queryset, который всегда будет пустым
   Appeal.objects.none()
   Result: <QuerySet []>

9. Вывести среднее кол-во пострадавших в происшествиях (обращениях)
   Appeal.objects.aggregate(models.Avg('count_injured'))
   Result: {'count_injured__avg': 2.0}

10. Вывести общее кол-во пострадавших в происшествиях
    Appeal.objects.aggregate(models.Sum('count_injured'))
    Result: {'count_injured__sum': 14}

11. Вывести кол-во вызванных служб для каждого происшествия
    Appeal.objects.annotate(count=models.Count('service')).values('number', 'count')
    Result: <QuerySet [{'number': UUID('7d7db990-fa82-4021-9576-b6e1c1ac27ed'), 'count': 2}, ...]>

12. Вывести среднее кол-во вызванных экстр служб
    EmergencyService.objects.annotate(count=models.Avg('appeals')).values('title', 'count')
    Result: <QuerySet [{'title': 'Полиция', 'count': 5.4}, {'title': 'Скорая помощь', 'count': 4.428571428571429}, {'title': 'Пожарная служба', 'count': 2.5}]>

13. Вывести наиб и наим кол-во пострадавших
    Appeal.objects.aggregate(models.Max('count_injured'), models.Min('count_injured'))
    Result: {'count_injured__max': 5, 'count_injured__min': 1}

14. Сформировать запрос к модели заявитель, в котором будет добавлено поле с кол-вом обращений каждого заявителя
    Applicant.objects.annotate(count_appeals=models.Count('appeals')).values('id', 'count_appeals')
    Result: <QuerySet [{'id': 1, 'count_appeals': 1}, {'id': 2, 'count_appeals': 2}, {'id': 3, 'count_appeals': 1}, {'id': 4, 'count_appeals': 1}, {'id': 5, 'count_ap
peals': 1}, {'id': 10, 'count_appeals': 1}, {'id': 11, 'count_appeals': 0}, {'id': 12, 'count_appeals': 0}, {'id': 42, 'count_appeals': 1}, {'id': 43, 'count_appea
ls': 0}]>

15. Не подгружать некоторые поля, пока явно не обратишься к ним
    Applicant.objects.defer('phone', 'photo')

16. Немедленно загрузить некоторые поля (противоположность defer)
	Applicant.objects.only('surname', 'name', 'descr_state_health')

17. Найти всех заявителей у которых числа заявок строго больше 10
	Applicant.objects.alias(appeals=Count('appeal')).filter(appeals__gt=10)

18. Проверить наличие объекта заявителя в qs
	joe = Applicant.objects.filter(name='Joe', age=18).first()
	adult_applicants = Applicant.objects.filter(birthday__lte=timezone.now() - timedelta(weeks=936))
	adult_applicant.contains(joe)

19. Вывести словарь с тремя объектами Appeal, ключи которых числа от 1 до 3
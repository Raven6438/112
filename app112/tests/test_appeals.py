from django.test import TestCase
from django.urls import reverse

from app112 import factories, models, consts
from app112.utils.tests.faker_init import faker_ru


class TestAppeal(TestCase):
    def setUp(self) -> None:
        self.applicant = factories.Applicant()
        self.services = [factories.EmergencyService() for _ in range(3)]
        self.appeal = factories.Appeal(applicant=self.applicant, service=self.services)

        self.origin_appeal_count = models.Appeal.objects.count()

    def test_list(self) -> None:
        url = reverse('app112:appeals')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create(self) -> None:
        url = reverse('app112:create_appeal')
        data = {
            'incidents': consts.INCIDENT_OTHER,
            'count_injured': faker_ru.pyint(min_value=0, max_value=100),
            'status': consts.STATUS_IN_WORK,
            'dontCall': True,
            'applicant': factories.Applicant().pk,
            'service': [factories.EmergencyService().pk for _ in range(3)]
        }

        response = self.client.post(url, data, follow=True)
        new_appeal = models.Appeal.objects.last()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_appeal.status, data['status'])
        self.assertEqual(new_appeal.dontCall, data['dontCall'])
        self.assertEqual(new_appeal.incidents, data['incidents'])
        self.assertEqual(new_appeal.applicant.pk, data['applicant'])
        self.assertEqual(new_appeal.count_injured, data['count_injured'])
        self.assertSequenceEqual(new_appeal.service.values_list('pk', flat=True), data['service'])

    def test_update(self) -> None:
        url = reverse('app112:edit_appeal', args=[self.appeal.pk])
        data = {
            'incidents': consts.INCIDENT_FIRE,
            'count_injured': faker_ru.pyint(min_value=0, max_value=100),
            'status': consts.STATUS_COMPLETED,
            'dontCall': False,
            'applicant': factories.Applicant().pk,
            'service': [factories.EmergencyService().pk for _ in range(3)]
        }

        response = self.client.post(url, data, follow=True)
        self.appeal.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.appeal.status, data['status'])
        self.assertEqual(self.appeal.dontCall, data['dontCall'])
        self.assertEqual(self.appeal.incidents, data['incidents'])
        self.assertEqual(self.appeal.applicant.pk, data['applicant'])
        self.assertEqual(self.appeal.count_injured, data['count_injured'])
        self.assertSequenceEqual(self.appeal.service.values_list('pk', flat=True), data['service'])

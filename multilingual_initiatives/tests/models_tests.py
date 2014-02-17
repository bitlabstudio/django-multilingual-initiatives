"""Tests for the models of the ``multilingual_initiatives`` app."""
from mock import Mock

from django.test import TestCase
from people.tests.factories import PersonFactory

from ..models import Initiative
from .factories import (
    InitiativeFactory,
    InitiativePersonRoleFactory,
    InitiativePluginModelFactory,
)


class InitiativeManagerTestCase(TestCase):
    """Tests for the ``InitiativeManager`` model manager."""
    longMessage = True

    def setUp(self):
        self.en_ini = InitiativeFactory(language_code='en')
        self.de_ini = InitiativeFactory(language='de')

        new_trans = self.en_ini.translate('de')
        new_trans.is_published = True
        new_trans.save()
        new_trans = self.de_ini.translate('en')
        new_trans.is_published = True
        new_trans.save()

    def test_manager(self):
        """Test, if the ``InitiativeManager`` returns the right entries."""
        request = Mock(LANGUAGE_CODE='de')
        self.assertEqual(
            Initiative.objects.published(request).count(), 1, msg=(
                'In German, there should be two published initiatives.'))

        request = Mock(LANGUAGE_CODE='en')
        self.assertEqual(
            Initiative.objects.published(request).count(), 1, msg=(
                'In English, there should be one published initiative.'))

        request = Mock(LANGUAGE_CODE=None)
        self.assertEqual(
            Initiative.objects.published(request).count(), 0, msg=(
                'If no language set, there should be no published'
                ' initiatives.'))


class InitiativeTestCase(TestCase):
    """Tests for the ``Initiative`` model."""
    longMessage = True

    def test_model(self):
        obj = InitiativeFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))


class InitiativePersonRoleTestCase(TestCase):
    """Tests for the ``InitiativePersonRole`` model."""
    longMessage = True

    def test_model(self):
        person = PersonFactory(language_code='en')
        obj = InitiativePersonRoleFactory(person=person)
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))


class InitiativePluginModelTestCase(TestCase):
    """Tests for the ``InitiativePluginModel`` model."""
    longMessage = True

    def test_model(self):
        obj = InitiativePluginModelFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))

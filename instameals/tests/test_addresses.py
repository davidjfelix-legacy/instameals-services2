from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from instameals.models import Address, APIUser


class AddressTests(APITestCase):
    def setUp(self):
        APIUser.objects.create(username='tester')
        self.new_address = {
            'line1': '123 Test Ave',
            'city': 'Testville',
            'state': 'TX',
            'postal_code': '12345',
            'country': 'USA',
            'coordinates': {
                'type': 'Point',
                'coordinates': [
                    -123.0123, 45.6789
                ],
            },
        }

    # Create REST/CRUD tests
    def test_user_can_create_address(self):
        url = reverse('address-list')
        user = APIUser.objects.get(username='tester')
        self.client.force_authenticate(user)
        response = self.client.post(url, self.new_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)

    def test_non_user_cannot_create_address(self):
        url = reverse('address-list')
        response = self.client.post(url, self.new_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Address.objects.count(), 0)

    # Read REST/CRUD tests
    def test_user_can_read_owned_address(self):
        pass

    def test_user_can_read_order_address(self):
        pass

    def test_cannot_list_address(self):
        pass

    # Update REST/CRUD tests
    # Address is immutable. We create a new one on update
    def test_cannot_update_address(self):
        pass

    def test_cannot_partially_update_address(self):
        pass

    # Delete REST/CRUD tests
    # Cannot delete addresses
    def test_user_cannot_delete_address(self):
        pass

    def test_non_user_cannot_delete_address(self):
        pass

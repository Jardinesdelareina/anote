from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class CustomUserTestCase(APITestCase):
    # Тесты CustomUser

    user_list_url=reverse('all')

    def setUp(self):
        # Cоздание нового пользователя, запрос к эндпоинту djoser
        self.user=self.client.post('/auth/users/', data={
            'email': 'testuser@gmail.com',
            'username': 'testuser',
            'password': 'this-is-password8354'
        })

        # Получение jwt нового пользователя
        response=self.client.post('/auth/jwt/create/', data={
            'email': 'testuser@gmail.com',
            'password': 'this-is-password8354'
        })
        self.token=response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    # Получение списка пользователей (/all_users)
    def test_customuser_list_authenticated(self):
        response=self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Получение списка пользователей пока запрос не прошел проверку подлинности
    def test_customuser_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response=self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Получение данных аутентифицированного пользователя
    def test_customuser_detail_retrieve(self):
        response=self.client.get(reverse('account', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Редактирование профиля пользователя, который был автоматически создан с использованием сигналов
    def test_customuser_account(self):
        account_data = {
            'about': 'Im testuser',
            'gender': 'male',
            'phone': '89759538793',
        }
        response=self.client.put(reverse('account', kwargs={'pk': 2}), data = account_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

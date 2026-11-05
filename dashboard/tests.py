from django.test import TestCase

# Create your tests here.

class DashboardViewTestCase(TestCase):
    def test_dashboard_view(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')


    def test_dashboard_view_with_authenticated_user(self):
        # Create a test user and log them in
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')


    def test_dashboard_view_with_unauthenticated_user(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

    def test_dashboard_view_with_post_request(self):
        response = self.client.post('/dashboard/', data={'key': 'value'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')



    def test_dashboard_view_with_invalid_method(self):
        response = self.client.put('/dashboard/', data={'key': 'value'})
        self.assertEqual(response.status_code, 405)  # Method Not Allowed   

    def test_dashboard_view_with_query_parameters(self):
        response = self.client.get('/dashboard/?param=value')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')



        

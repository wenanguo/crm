import re
import unittest
from flask import url_for
from app import create_app, db
from app.models import User, Role

class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        #db.create_all()
        #Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        #db.session.remove()
        #db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue(b'Stranger' in response.data)

    def test_register_and_login(self):
        # register a new account
        response = self.client.post(url_for('main.register'), data={
            'email': 'john@example.com',
            'username': 'john',
            'password': 'cat',
            'password2': 'cat'
        })
        self.assertTrue(response.status_code == 200)

        # login with the new account
        response = self.client.post(url_for('main.login'), data={
            'username': 'john',
            'password': 'cat'
        }, follow_redirects=True)


        self.assertTrue(re.search(b'Hello,\s+Stranger!', response.data))

        user = User.query.filter_by(username='john').first()

        self.assertTrue('john' == user.username)

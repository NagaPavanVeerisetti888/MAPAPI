import pytest
from utilities import get_yaml, read_authenticated_email_ids, read_non_authenticated_email_ids
from helpers import hit_api

@pytest.fixture(scope='module')
def api_config():
   """Fixture to load API configuration."""
   config = get_yaml()
   print(config)
   return {
       'base_url': config['accessAPI']['base_url'],
       'endpoint': config['accessAPI']['users_endpoint'],
       'authenticated_users': read_authenticated_email_ids(),
       'non-authenticated_users': read_non_authenticated_email_ids()
   }

@pytest.mark.access
@pytest.mark.test_id('TC001')
@pytest.mark.description('Check users have access')
def test_authenticate(api_config):
   """Test to check users have access."""
   for user in api_config['authenticated_users']:
       response = hit_api(api_config['base_url'], api_config['endpoint'], user)
       assert response == 200, f"User {user} should have access. Response code: {response}"

@pytest.mark.access
@pytest.mark.test_id('TC002')
@pytest.mark.description('Check users do not have access.')
def test_non_authenticate(api_config):
   """Test to check users do not have access."""
   for user in api_config['non-authenticated_users']:
       response = hit_api(api_config['base_url'], api_config['endpoint'], user)
       assert response == 404, f"User {user} does not exist. Response code: {response}"


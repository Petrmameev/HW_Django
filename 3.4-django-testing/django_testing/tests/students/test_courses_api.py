import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_one_course(client, course_factory):
    courses = course_factory(_quantity=1)
    course_id = courses[0].id
    response = client.get(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == courses[0].name

@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len (courses)
    for a, b in enumerate(data):
        assert b['name'] == courses[a].name

@pytest.mark.django_db
def test_filter_course_id(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/?id={courses[0].id}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[0].id

@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/?name={courses[0].name}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name

@pytest.mark.django_db
def test_success_create_course(client):
    course = {'name': 'django'}
    response = client.post(f'/api/v1/courses/', data=course)
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == course['name']

@pytest.mark.django_db
def test_success_patch_course(client, course_factory):
    course = course_factory(_quantity=1)
    new_name_course = {'name': 'django'}
    response = client.patch(f'/api/v1/courses/{course[0].id}/', data=new_name_course)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == new_name_course['name']

@pytest.mark.django_db
def test_success_delete_course(client, course_factory):
    course = course_factory(_quantity=10)
    count = Course.objects.count()
    response = client.get(f'/api/v1/courses/')
    assert response.status_code == 200
    client.delete(f'/api/v1/courses/{course[0].id}/')
    assert Course.objects.count() == count - 1


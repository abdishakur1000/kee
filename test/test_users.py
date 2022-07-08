import pytest
from jose import jwt
from app.config import settings
from app import schemas


def test_root(client, session):
    session.query()  # ha hilmaamin in aad ka saarto ama aad fahanto
    print(session)
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'abdishakur waakan'
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/users/", json={'email': 'abdishakur0@gmail.com', 'password': 'agree101'})
    new_user = schemas.UserOut(**res.json())
    assert new_user.id == new_user.id
    assert new_user.email == 'abdishakur0@gmail.com'
    assert new_user.created_at == new_user.created_at
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        "/login", data={'username': test_user['email'], 'password': test_user['password']})
    print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get('user_id')
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200


@pytest.mark.parametrize('email, password, status_code', [
    ('wrong@gmail.com', 'agree101', 403),
    ('abdishakur0@gmail.com', 'whatis123', 403),
    ('wrong2346@gmail.com', 'come12349', 403),
    (None, 'password123', 422),
    ('abdi@gmail.com', None, 422)
])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post(
        "/login", data={'username': email,
                        'password': password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'


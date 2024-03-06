import json

import pytest
import requests

BASE_URL = "https://api.github.com"
USERNAME = "ell-ink"
TOKEN = ""  # Вставьте свой специальный токен GitHub для тестирования API

@pytest.fixture
def auth_headers():
    return {"Authorization": f"token {TOKEN}"}

def test_get_user():
    """Тест проверяет, что запрос информации о пользователе выполняется успешно и возвращается корректный ответ"""
    response = requests.get(f"{BASE_URL}/users/{USERNAME}")
    assert response.status_code == 200
    assert "login" in response.json()


def test_get_repos():
    """Тест проверяет получение контента со страницы репозиториев пользователя"""
    response = requests.get(f"{BASE_URL}/users/{USERNAME}/repos")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_create_repo_status():
    """Тест проверяет, что создание нового репозитория возвращает ожидаемый статус код 403 - Запрещено"""

    headers = {"Authorization": "token " + TOKEN}
    data = {"name": "test_repo", "description": "Test repository"}

    response = requests.post(f"{BASE_URL}/user/repos", headers=headers, json=data)

    assert response.status_code == 403


def test_get_user_info():
    """Тест проверяет получение информации о пользователе."""
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(f"{BASE_URL}/users/{USERNAME}", headers=headers)

    assert response.status_code == 200

    user_info = response.json()
    assert "login" in user_info
    assert "name" in user_info
    assert "public_repos" in user_info


def test_get_user_repos():
    """Тест проверяет получение списка репозиториев пользователя."""
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(f"{BASE_URL}/users/{USERNAME}/repos", headers=headers)

    assert response.status_code == 200

    repos = response.json()
    assert isinstance(repos, list)
    assert len(repos) > 0


def test_get_repo_info():
    """Тест проверяет получение информации о конкретном репозитории."""
    repo_name = "LinGo"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(f"{BASE_URL}/repos/{USERNAME}/{repo_name}", headers=headers)

    assert response.status_code == 200

    repo_info = response.json()
    assert "name" in repo_info
    assert "description" in repo_info
    assert "language" in repo_info

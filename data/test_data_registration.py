from dataclasses import dataclass
from typing import List, Optional


@dataclass
class RegistrationData:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    day: int
    month: int
    year: int
    subjects: List[str]
    hobbies: List[str]
    current_address: str
    state: str
    city: str


@dataclass
class PartialRegistrationData:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    mobile: Optional[str] = None
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    subjects: Optional[List[str]] = None
    hobbies: Optional[List[str]] = None
    current_address: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None


REGISTRATION_TEST_DATA = [
    RegistrationData(
        first_name="Мария",
        last_name="Иванова",
        email="maria.ivanova@test.com",
        gender="Female",
        mobile="0987654321",
        day=1,
        month=7,
        year=2008,
        subjects=["Chemistry", "Biology"],
        hobbies=["Music"],
        current_address="г. Санкт-Петербург",
        state="Uttar Pradesh",
        city="Agra"
    ),
    RegistrationData(
        first_name="Иван",
        last_name="Иванов",
        email="ivan.ivanov@test.com",
        gender="Male",
        mobile="0987654321",
        day=12,
        month=8,
        year=2009,
        subjects=["Maths"],
        hobbies=["Sports"],
        current_address="г. Санкт-Петербург",
        state="NCR",
        city="Noida"
    )
]

PARTIAL_TEST_DATA = [
    PartialRegistrationData(
        last_name="Петров",
        email="ivan@test.com",
        gender="Male",
        mobile="1234567890",
        day=20,
        month=12,
        year=1989
    ),
    PartialRegistrationData(
        first_name="Иван",
        email="ivan@test.com",
        gender="Male",
        mobile="1234567890",
        day=20,
        month=12,
        year=1989
    ),
    PartialRegistrationData(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        mobile="1234567890",
        day=20,
        month=12,
        year=1989
    ),
    PartialRegistrationData(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        gender="Male",
        day=20,
        month=12,
        year=1989
    )
]

INVALID_MOBILE_DATA = [
    PartialRegistrationData(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        gender="Male",
        mobile="123",
        day=20,
        month=12,
        year=1989,
        current_address="г. Москва",
        state="NCR",
        city="Delhi"
    ),
    PartialRegistrationData(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        gender="Male",
        mobile="123456789",
        day=20,
        month=12,
        year=1989,
        current_address="г. Москва",
        state="NCR",
        city="Delhi"
    ),
    PartialRegistrationData(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        gender="Male",
        mobile="12345678901",
        day=20,
        month=12,
        year=1989,
        current_address="г. Москва",
        state="NCR",
        city="Delhi"
    ),
    PartialRegistrationData(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        gender="Male",
        mobile="abcdefghij",
        day=20,
        month=12,
        year=1989,
        current_address="г. Москва",
        state="NCR",
        city="Delhi"
    ),
    PartialRegistrationData(
        first_name="Иван",
        last_name="Петров",
        email="ivan@test.com",
        gender="Male",
        mobile="123-456-7890",
        day=20,
        month=12,
        year=1989,
        current_address="г. Москва",
        state="NCR",
        city="Delhi"
    )
]

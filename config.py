
class BasicConfig:
    USER_DB='postgres'
    PASS_DB='admin'
    URL_DB='localhost'
    NAME_DB='tokens'
    FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
    SQLALCHREMY_DATABASE_URI=FULL_URL_DB
    DEBUG=True
    SECRET_KEY="secretKey1212"
    BCRYPT_LOG_ROUNDS=13
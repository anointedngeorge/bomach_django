
from superadmin.celery import app as celery_app

# import pymysql

# pymysql.version_info = (1, 3, 13, "final", 0)
# pymysql.install_as_MySQLdb()

# pymysql.version_info = (1, 4, 0, "final", 0)
# pymysql.install_as_MySQLdb()



__all__ = ("celery_app",)
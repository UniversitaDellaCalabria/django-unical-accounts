Setup
-----

- Copy this app on top of your project's BASE_DIR, do not install it in your environment, custom django's user models still need this way to do, at this moment;
- Insert at the first position of `settings.INSTALLED_APP`, before `'django.contrib.admin'`;
- Add also in `settings.py` `AUTH_USER_MODEL = "unical_accounts.User"`;
- make migrations and migrate.


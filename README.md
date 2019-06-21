Setup
-----

- Copy this app on top of your project's BASE_DIR, do not install it in your environment, custom django's user models need still this way at this moment;
- Insert on top of `settings.INSTALLED_APP`;
- Add also in `settings.py` `AUTH_USER_MODEL = "unical_accounts.User"`;
- make migrations and migrate.


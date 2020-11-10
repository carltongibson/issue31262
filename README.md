
Reproduce for performance regression on PR 12449
https://github.com/django/django/pull/12449

* Create a new venv
* `pip install -e path/to/django`
* `pip install django-debug-toolbar`
* `./manage.py migrate`
* `./manage.py loaddata fixtures.json`
* `./manage.py createsuperuser`
* `./manage.py runserver`

Visit: <http://127.0.0.1:8000/admin/example/book/>

* 14 queries on `master`/`3.1.x`
* 74 queries on `pull/12449/head`

14 and 74 is too high:

* there's an issue with debug-toolbar-duplicating queries
* https://github.com/jazzband/django-debug-toolbar/issues/1239
* Comment out overriding `chunked_cursor` in `site-packages/debug_toolbar/panels/sql/tracking.py` to see it properly.
* It's about 11 vs 45, like so, but still.

This diff fixes the regression:

```diff
(django) django (pr/12449)$ git diff django/forms/fields.py
diff --git a/django/forms/fields.py b/django/forms/fields.py
index 0728db9922..32153819ff 100644
--- a/django/forms/fields.py
+++ b/django/forms/fields.py
@@ -791,7 +791,7 @@ class ChoiceField(Field):

         # Setting choices on the field also sets the choices on the widget.
         # Note that we bypass the property setter to avoid re-normalizing.
-        self._choices = self.widget._choices = value
+        self._choices = self.widget.choices = value

     def to_python(self, value):
         """Return a string."""
```


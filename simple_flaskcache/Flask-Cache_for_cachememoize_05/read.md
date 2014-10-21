modify /lib/python2.6/site-packages/flask_cache/__init__.py 
to print cache_key
233                 try:
234                     cache_key = decorated_function.make_cache_key(*args, **kwargs)
235                     rv = self.cache.get(cache_key)
&
438                 try:
439                     cache_key = decorated_function.make_cache_key(f, *args, **kwargs)
440                     rv = self.cache.get(cache_key)
441                 except Exception:
442                     if current_app.debug:
443                         raise
444                     logger.exception("Exception possibly due to cache backend.")
445                     return f(*args, **kwargs)
to test the note
Note
With functions that do not receive arguments, cached() and memoize() are effectively the same.

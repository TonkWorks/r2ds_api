========
r2ds-api
========


.. image:: https://img.shields.io/pypi/v/r2ds_api.svg
        :target: https://pypi.python.org/pypi/r2ds_api

.. image:: https://img.shields.io/travis/tonkworks/r2ds_api.svg
        :target: https://travis-ci.org/TonkWorks/r2ds_api

.. image:: https://readthedocs.org/projects/r2ds-api/badge/?version=latest
        :target: https://r2ds-api.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/tonkworks/r2ds_api/shield.svg
     :target: https://pyup.io/repos/github/TonkWorks/r2ds_api/
     :alt: Updates



R2DS Python API


* Free software: MIT license
* Documentation: https://r2ds-api.readthedocs.io.


QuickStart
--------

```
pip install r2ds_api
```

```
import r2ds_api


response = r2ds.get("EXAMPLE AUTH KEY", {
"score__gt": 100
})
print(response.json())
```

Features
--------

* R2DS Search and filtering
* Topic Notifications
* Streaming


More Information
--------
* https://r2ds.tonkworks.com/
* https://r2ds.tonkworks.com/api/
* https://r2ds-api.readthedocs.io/en/latest/
import requests


class HttpTool:
    @classmethod
    def url2httpr(cls, url, args=None, kwargs=None, session=None, adapter=None, ):
        _a = args or []
        __k = kwargs or {}

        s = session or requests.Session()
        a = adapter or requests.adapters.HTTPAdapter()

        s.mount('http://', a)
        s.mount('https://', a)

        # k_get = config.get("get", {}) if config else {}
        return s.get(url, *_a, **__k)

    @classmethod
    def url_retries2httpr(cls, url, max_retries):
        adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
        return cls.url2httpr(url, adapter=adapter)


class HttprToolkit:
    @classmethod
    def httpr2status_code(cls, httpr): return httpr.status_code

    @classmethod
    def httpr2is_ok(cls, httpr): return httpr.ok

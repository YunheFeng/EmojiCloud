import timeit
from httpx import AsyncClient
import dateutil.parser
import requests
import pickle
# from rich import print
import re
from typing import *
from bs4 import Tag


def with_client(func):
    def wrapper(*args, client: requests.Session = None, **kwargs):
        if not client:
            print('Client not specified')
            return
        res = func(*args, client=client, **kwargs)
        return res
    return wrapper


def print_size(size, unit_size: int = 1024, unit: str = 'B', current: str = ''):
    if size < unit_size ** 1:
        pass
    elif size < unit_size ** 2:
        unit = 'K' + unit
        size = float(size) / unit_size
    elif size < unit_size ** 3:
        unit = 'M' + unit
        size = float(size) / unit_size ** 2
    elif size < unit_size ** 4:
        unit = 'G' + unit
        size = float(size) / unit_size ** 3
    elif size < unit_size ** 5:
        unit = 'T' + unit
        size = float(size) / unit_size ** 4
    else:
        return size
    return '%.2f %s' % (size, unit)


def load_cookie(client: AsyncClient, cookie_filename):
    with open(cookie_filename, 'rb') as f:
        client.cookies.update(pickle.load(f))


def save_cookie(cookie_jar, cookie_filename):
    with open(cookie_filename, 'wb') as f:
        pickle.dump(cookie_jar, f)


def with_timeit(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        func(*args, **kwargs)
        duration = timeit.default_timer() - start
        print("Finish in {:.2f} seconds".format(duration))
    return wrapper


def with_async_timeit(func):
    async def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        await func(*args, **kwargs)
        duration = timeit.default_timer() - start
        print("Finish in {:.2f} seconds".format(duration))
    return wrapper


def parse_iso_datetime(dt_string):
    return dateutil.parser.isoparse(dt_string).replace(tzinfo=None)


headers1 = {
    "accept": r'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "accept-encoding": r'gzip, deflate, br',
    "accept-language": r'en',
    "sec-ch-ua": r'" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    "sec-ch-ua-arch": r'"x86"',
    "sec-ch-ua-bitness": r'"64"',
    "sec-ch-ua-full-version": r'"99.0.4844.51"',
    "sec-ch-ua-mobile": r'?0',
    "sec-ch-ua-model": r'""',
    "sec-ch-ua-platform": r'"macOS"',
    "sec-ch-ua-platform-version": r'"12.2.1"',
    "sec-fetch-dest": r'document',
    "sec-fetch-mode": r'navigate',
    "sec-fetch-site": r'none',
    "sec-fetch-user": r'?1',
    "upgrade-insecure-requests": r'1',
    "user-agent": r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
}


def try_select(
    source: Union[str, Tag],
    target: str,
    default: str = '',
    default_factory: Callable = None,
    first: bool = True,
    post=lambda x: x
) -> any:
    if isinstance(source, Tag):
        t = source.select(target)
    elif isinstance(source, str):
        t = re.findall(target, source)
    else:
        print("Unsupported source type: %s" % type(source))
        return None
    if t:
        try:
            if first:
                return post(t[0])
            else:
                return post(t)
        except Exception as e:
            print(e)
            return default_factory() if default_factory else default
    else:
        return default


def try_soup_select_text(soup, selector: str, **kwargs):
    return try_select(soup, selector, post=lambda x: x.text.strip(), **kwargs)


def try_soup_select_link(soup, selector: str, **kwargs):
    return try_select(soup, selector, post=lambda x: x['href'], **kwargs)


def chain_select(selectables, initial_args: tuple, kwargs: dict):
    if len(selectables) == 0:
        return

    output = selectables[0](*initial_args, **kwargs)

    if len(selectables) == 1:
        return output

    for s in selectables[1:]:
        output = ''

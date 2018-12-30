from mahler.client import Client

from ops import run


mahler = Client()


tags = ['examples', 'random', 'local', 'v1.0']


if __name__ == "__main__":
    for i in range(100):
        mahler.register(run.delay(dummy=i), tags=tags)

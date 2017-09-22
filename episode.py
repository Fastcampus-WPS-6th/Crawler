# Episode = namedtuple('Episode', ['no', 'img_url', 'title', 'rating', 'created_date'])
import os

import requests


class Episode:
    """
    namedtuple 'Episode'와 같은 역할을 할 수 있도록 생성
    """
    def __init__(self, webtoon, no, url_thumbnail, title, rating, created_date):
        self._webtoon = webtoon
        self._no = no
        self._url_thumbnail = url_thumbnail
        self._title = title
        self._rating = rating
        self._created_date = created_date

        self.thumbnail_dir = f'webtoon/{self.webtoon.title_id}_thumbnail'
        self.save_thumbnail()

    @property
    def webtoon(self):
        return self._webtoon

    @property
    def no(self):
        return self._no

    @property
    def url_thumbnail(self):
        return self._url_thumbnail

    @property
    def title(self):
        return self._title

    @property
    def rating(self):
        return self._rating

    @property
    def created_date(self):
        return self._created_date

    @property
    def has_thumbnail(self):
        """
        현재경로/webtoon/{self.webtoon.title_id}_thumbnail/{self.no}.jpg
          파일이 있는지 검사 후 리턴
        :return:
        """
        path = f'{self.thumbnail_dir}/{self.no}.jpg'
        return os.path.exists(path)

    def save_thumbnail(self, force_update=True):
        """
        Episode자신의 img_url에 있는 이미지를 저장한다
        :param force_update:
        :return:
        """
        if not self.has_thumbnail or force_update:
            # webtoon/{self.webtoon.title_id}에 해당하는 폴더 생성
            os.makedirs(self.thumbnail_dir, exist_ok=True)
            response = requests.get(self.url_thumbnail)
            filepath = f'{self.thumbnail_dir}/{self.no}.jpg'
            if not os.path.exists(filepath):
                with open(filepath, 'wb') as f:
                    f.write(response.content)

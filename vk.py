from sql.SQL import *
import json
import requests
from tqdm import tqdm
from tokens import user_token


class VK_Parse:
    def __init__(self, access_token, vk_user_id, gender, age, city):  # Инициализация входных параметров
    # Инициализация входных параметров
    def __init__(self, access_token, vk_user_id, gender, age, city):
        self.access_token = access_token
        self.vk_user_id = vk_user_id
        self.age = age
@@ -34,29 +34,29 @@ def parse(self):
                  'v': '5.131'
                  }
        response = requests.get(
                'https://api.vk.com/method/users.search', params=params)
            'https://api.vk.com/method/users.search', params=params)
        result = response.json()
        try:
            if result['response']['count'] != 0:
                res = result['response']['items']
            # Прогресс-бар каждой итерации отображается в терминале
                for item in tqdm(res, desc='Идет поиск...'):
                    

                    profile_url = f"https://vk.com/id{item['id']}"
                    photos = self.get_photos(item['id'])
                    if photos:
                        first_name = item['first_name']
                        last_name = item['last_name']
                        city = self.city
                        # Запись в базу данных при каждой итерации
                        push_pair_data_in_base(self.vk_user_id, first_name, last_name, city, profile_url, photos)
                        push_pair_data_in_base(
                            self.vk_user_id, first_name, last_name, city, profile_url, photos)
                return 'Всё готово!'
            else:
                raise Exception
        

        except Exception:
            return f'&#10060; Ошибка:\nОдин или несколько параметров указаны неверно.\nПопробуйте ещё раз.'


    def get_photos(self, user_id):
        '''
@@ -76,10 +76,11 @@ def get_photos(self, user_id):
            photo_urls = []
            if 'response' in photos_result:
                photos = photos_result['response']['items']
                sorted_photos = sorted(photos, key=lambda x: x.get('likes', {}).get('count', 0), reverse=True)  # Сортировка по лайкам
                sorted_photos = sorted(photos, key=lambda x: x.get('likes', {}).get(
                    'count', 0), reverse=True)  # Сортировка по лайкам
                for photo in sorted_photos[:3]:
                    photo_urls.append(photo['sizes'][-1]['url'])
            return photo_urls
        except Exception as e:
            print(f"Ошибка при получении фотографий: {e}")
            return []

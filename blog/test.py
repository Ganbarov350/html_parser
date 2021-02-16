from django.test import TestCase
from django.urls import reverse


class UserLogin(TestCase):
    url = reverse("blog:parser")

    def payment(self):
        # Create begin payment
        response = self.client.post(self.url, {"url": "https://www.trendyol.com/trendyolmilla/siyah-yuksek-bel-toparlayici-orme-tayt-twoaw20ta0087-p-31515569?boutiqueId=554412&merchantId=968"})
        self.assertEqual(201, response.status_code)


from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from blog.models import Post


class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 클래스 전체에서 사용되는 설정을 위해서 테스트 시작 때 딱 한 번만 실행됩니다. 테스트 메쏘드가 실행되면서 수정되거나 변경되지 않을 객체들을 이곳에서 생성할 수 있습니다.
        print('1.setUpTestData')
        num_of_post = 10
        author = User.objects.create(username='hsj2334', email='hsj2334@gmail.com')
        for i in range(num_of_post):
            Post.objects.create(
                author=author,
                title={i},
                text={i},
                created_date=now()
            )

    def test_view_url_exists_at_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_access_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/post_list.html')

    def test_view_correct_cnt_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        posts=response.context['posts']
        self.assertEqual(len(posts),10)
        # self.assertEqual(response.context['id'])

    # def setUp(self):
    #     # 각각의 테스트 메쏘드가 실행될 때마다 실행됩니다. 테스트 중 내용이 변경될 수 있는 객체를 이곳에서 생성할 수 있습니다
    #     print("2.setUp")
    #     author = User.objects.get(id=1)
    #     field_label = author._meta.get_field('username').verbose_name
    #     self.assertEqual(field_label, '사용자 이름')
    #     pass
    #
    # def test_false_is_false(self):
    #     print('method: false_is_false')
    #     self.assertFalse(False)
    #
    # def test_false_is_true(self):
    #     print('method: false_is_true')
    #     self.assertTrue(False)
    #
    # def test_one_plus_equals_two(self):
    #     print('method: test_one_plus_equals_two')
    #     self.assertEqual(1 + 1, 2)

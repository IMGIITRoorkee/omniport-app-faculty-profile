import logging

from notifications.actions import push_notification
from categories.models import Category

from faculty_profile.apps import Config

logger = logging.getLogger('faculty_profile')


def notify(person, notification_text):
    """
    Utility for notifying the faculty that the page has been published.
    :param person: the person related to faculty
    :param notification_text: description of notification
    """

    app_verbose_name = Config.verbose_name
    app_slug = Config.name

    category, _ = Category.objects.get_or_create(
        name=app_verbose_name,
        slug=app_slug,
    )

    try:
        push_notification(
            template=notification_text,
            category=category,
            android_onclick_activity='',
            ios_onclick_action='',
            is_personalised=True,
            person=person,
            has_custom_users_target=False,
            persons=None,
        )
        logger.info(
            f'Successfully notified {person} that the page has been published'
        )
    # ValueError is the only possible error raised by `push_notification` in
    # this case.
    except ValueError:
        logger.warning(
            f'Couldn\'t notify {person} that the page has been published'
        )

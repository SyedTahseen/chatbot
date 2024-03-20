from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_i18n import I18nContext


class Language(CallbackData, prefix="language"):
    """
    Language callback data
    """

    language: str


def select_language() -> InlineKeyboardMarkup:
    """
    Select language keyboard

    :return: InlineKeyboardMarkup with language selection
    """
    keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    keyboard.row(
        *[
            InlineKeyboardButton(text="🇬🇧", callback_data=Language(language="en").pack()),
            InlineKeyboardButton(text="🇺🇦", callback_data=Language(language="uk").pack()),
            InlineKeyboardButton(text="🇯🇵", callback_data=Language(language="ja").pack()),
        ],
        width=2,
    )
    return keyboard.as_markup()


def link_profile(i18n: I18nContext, url: str) -> InlineKeyboardMarkup:
    """
    Link profile keyboard

    :param i18n: I18nContext object.
    :param url: URL of the profile.
    :return: InlineKeyboardMarkup with the link to the profile.
    """
    keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=i18n.get("profile-btn"), url=url))
    return keyboard.as_markup()

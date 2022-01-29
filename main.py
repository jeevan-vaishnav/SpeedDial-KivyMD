from csv import Dialect
from kivymd.app import MDApp
from kivy.lang import Builder


class DialLog(MDApp):

    data = {
        "Python": "language-python",
        "Java": "language-java",
        "Ruby": "language-ruby"

    }

    def callback_it(self, instance):
        if instance.icon == "language-python":
            lang = "Python"
        elif instance.icon == "language-java":
            lang = "Java"
        else:
            lang = "Ruby"

        self.root.ids.m_label.text = f"You pressed {lang}"

    # open

    def open(self):
        self.root.ids.m_label.text = f"Open!"
    # close

    def close(self):
        self.root.ids.m_label.text = f"Close!"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Lime"
        return Builder.load_file('main.kv')


if __name__ == "__main__":
    DialLog().run()

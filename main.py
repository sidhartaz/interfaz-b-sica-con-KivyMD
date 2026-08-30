import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
# En KivyMD 2.0.0 se usan MDButton y MDButtonText
from kivymd.uix.button import MDButton, MDButtonText
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle


class DiagnosticoApp(MDApp):

    def build(self):
        # Configuración Material Design
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"

        # Pantalla principal
        screen = MDScreen()

        # Fondo general oscuro
        with screen.canvas.before:
            Color(0.15, 0.15, 0.15, 1)
            self.background = Rectangle(
                pos=screen.pos,
                size=screen.size
            )

        screen.bind(
            pos=self.update_background,
            size=self.update_background
        )

        # Barra superior naranja
        header = MDBoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=dp(70),
            padding=[dp(20), dp(10)]
        )

        with header.canvas.before:
            Color(1, 0.55, 0, 1)
            self.header_background = Rectangle(
                pos=header.pos,
                size=header.size
            )

        header.bind(
            pos=self.update_header,
            size=self.update_header
        )

        title = MDLabel(
            text="Desarrollo Móvil",
            halign="center",
            valign="middle",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="Title"
        )

        header.add_widget(title)

        # Contenedor principal
        content = MDBoxLayout(
            orientation="vertical",
            spacing=dp(25),
            padding=[dp(35), dp(40)],
            size_hint=(0.9, None),
            height=dp(350),
            pos_hint={"center_x": 0.5, "center_y": 0.45}
        )

        # Mensaje de bienvenida
        welcome = MDLabel(
            text="Bienvenido",
            halign="center",
            font_style="Headline",
            size_hint_y=None,
            height=dp(60)
        )

        # Campo de texto para la organización
        self.organization_input = MDTextField(
            mode="outlined",
            size_hint_y=None,
            height=dp(60)
        )
        # Añadir el texto de referencia (hint) al campo
        self.organization_input.add_widget(
            MDTextField(hint_text="Ingrese el nombre de su organización")
        )

        # Botón para guardar datos (Estructura KivyMD 2.0)
        save_button = MDButton(
            MDButtonText(text="Guardar"),
            pos_hint={"center_x": 0.5},
            on_release=self.save_organization
        )

        # Agregar componentes al contenedor
        content.add_widget(welcome)
        content.add_widget(self.organization_input)
        content.add_widget(save_button)

        # Agregar elementos a la pantalla
        screen.add_widget(header)
        screen.add_widget(content)

        return screen

    def update_background(self, instance, value):
        self.background.pos = instance.pos
        self.background.size = instance.size

    def update_header(self, instance, value):
        self.header_background.pos = instance.pos
        self.header_background.size = instance.size

    def save_organization(self, instance):
        organization = self.organization_input.text.strip()

        if not organization:
            print("Debe ingresar el nombre de una organización.")
            return

        data = {
            "organizacion": organization
        }

        # Guardar en archivo JSON
        with open("organizacion.json", "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        print("Organización guardada correctamente.")


if __name__ == "__main__":
    DiagnosticoApp().run()
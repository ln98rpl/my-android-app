from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        # Create a vertical layout
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Add a label
        self.label = Label(text="Hello from Lubuntu & Python!", font_size='20sp')
        layout.add_widget(self.label)
        
        # Add a button that changes text on click
        btn = Button(text="Click Me!", font_size='20sp', size_hint=(1, 0.3))
        btn.bind(on_press=self.on_button_click)
        layout.add_widget(btn)
        
        return layout

    def on_button_click(self, instance):
        self.label.text = "Button Clicked Successfully!"

if __name__ == '__main__':
    TestApp().run()

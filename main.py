from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random

class RehanLudoApp(App):
    def build(self):
        self.cheat_active = False
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Red Admin Branding
        self.title_label = Label(
            text="ADMIN REHANQAZI", 
            color=(1, 0, 0, 1), 
            font_size=28,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.title_label)
        
        self.result_label = Label(
            text="Welcome! Select 1 to 10 Players & Roll Dice", 
            font_size=18
        )
        layout.add_widget(self.result_label)
        
        # Player Selection (1 to 10 players)
        self.player_input = TextInput(
            text='4', 
            multiline=False, 
            size_hint_y=None, 
            height=40
        )
        layout.add_widget(Label(text="Enter Players (1 to 10):", size_hint_y=None, height=20))
        layout.add_widget(self.player_input)
        
        # Roll Dice Button
        roll_btn = Button(
            text="Roll Dice", 
            background_color=(0.1, 0.6, 0.8, 1),
            size_hint_y=None, 
            height=50
        )
        roll_btn.bind(on_press=self.roll_dice)
        layout.add_widget(roll_btn)
        
        # Hidden Admin Cheat Button (Invisible to others)
        self.secret_btn = Button(
            text="[Hidden Admin Switch]", 
            color=(0, 0, 0, 0), 
            background_color=(0, 0, 0, 0), 
            size_hint_y=None,
            height=40
        )
        self.secret_btn.bind(on_press=self.toggle_cheat)
        layout.add_widget(self.secret_btn)
        
        return layout

    def toggle_cheat(self, instance):
        self.cheat_active = not self.cheat_active
        if self.cheat_active:
            self.result_label.text = ">> CHEAT ACTIVATED (Always 6) <<"
        else:
            self.result_label.text = ">> CHEAT DEACTIVATED (Normal Mode) <<"

    def roll_dice(self, instance):
        try:
            num_players = int(self.player_input.text)
            if num_players < 1 or num_players > 10:
                self.result_label.text = "Please enter players between 1 and 10!"
                return
        except ValueError:
            num_players = 4

        if self.cheat_active:
            dice = 6
        else:
            dice = random.randint(1, 6)
            
        self.result_label.text = f"Players: {num_players} | Dice Rolled: {dice}"

if __name__ == '__main__':
    RehanLudoApp().run()



import os
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
import requests

# ==========================================
# CONFIGURAÇÃO DO TEU TÚNEL NGROK
# ==========================================
NGROK_BASE_URL = "https://major-bursiform-blaine.ngrok-free.dev"

KV = """
<DashboardScreen>:
    name: 'dash'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(15)
        canvas.before:
            Color:
                rgba: 0.03, 0.03, 0.08, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        # Cabeçalho
        Label:
            text: "NEXUS ORACLE v21.0 [REMOTE]"
            font_size: '14sp'
            color: 0.4, 0.4, 0.6, 1
            size_hint_y: None
            height: dp(30)

        # Área de Previsão Principal
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: 0.6
            canvas.before:
                Color:
                    rgba: 0.1, 0.1, 0.2, 0.5
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(20)]
            
            Label:
                text: "PRÓXIMO CRASH ESTIMADO"
                font_size: '16sp'
                color: 1, 1, 1, 0.6
            
            Label:
                text: f"{root.current_prediction:.2f}x"
                font_size: '80sp'
                bold: True
                color: (0, 1, 0.5, 1) if root.confidence > 70 else (1, 0.7, 0, 1)

            Label:
                text: f"CONFIANÇA: {root.confidence:.1f}%"
                font_size: '22sp'
                bold: True
                color: 1, 1, 1, 0.9

        # Barra de Progresso de Confiança
        Widget:
            size_hint_y: None
            height: dp(6)
            canvas:
                Color:
                    rgba: 1, 1, 1, 0.1
                Rectangle:
                    pos: self.x, self.y
                    size: self.width, self.height
                Color:
                    rgba: (0, 1, 0.5, 1) if root.confidence > 70 else (1, 0.7, 0, 1)
                Rectangle:
                    pos: self.x, self.y
                    size: self.width * (root.confidence / 100), self.height

        # Info Adicional (Vindo do teu Ensemble v21.0)
        GridLayout:
            cols: 2
            size_hint_y: 0.2
            Label:
                text: "ALVO ±0.3:"
                halign: 'left'
                color: 0.7, 0.7, 0.7, 1
            Label:
                text: "ACTIVO"
                color: 0, 1, 0, 1
            Label:
                text: "DIST. MLE:"
                halign: 'left'
                color: 0.7, 0.7, 0.7, 1
            Label:
                text: f"{root.dist_mle:.2f}"
                color: 1, 1, 1, 1

        # Status de Conexão
        Label:
            text: root.status_msg
            font_size: '12sp'
            color: (1, 0.3, 0.3, 1) if "Erro" in root.status_msg else (0.3, 0.8, 1, 0.7)
            size_hint_y: None
            height: dp(30)
"""

class DashboardScreen(Screen):
    current_prediction = NumericProperty(1.0)
    confidence = NumericProperty(0.0)
    dist_mle = NumericProperty(0.0)
    status_msg = StringProperty("A ligar ao servidor ThinkPad...")

    def update_data(self, *args):
        try:
            # Rota de predição definida no teu main.py v21.0
            url = f"{NGROK_BASE_URL}/predict/888bets"
            
            # Request com timeout curto para não travar a UI
            response = requests.get(url, timeout=1.2)
            
            if response.status_code == 200:
                data = response.json()
                # Atribui os valores vindos do teu backend v21.0
                self.current_prediction = data.get("point", 1.0)
                self.confidence = data.get("confidence", 0.0)
                self.dist_mle = data.get("dist_mle", 0.0)
                self.status_msg = "Sincronizado: Lenovo Online"
            else:
                self.status_msg = f"Servidor respondeu erro: {response.status_code}"
        except requests.exceptions.ConnectionError:
            self.status_msg = "Erro: Ngrok offline ou link expirado"
        except Exception as e:
            self.status_msg = f"Erro de conexão: {str(e)[:30]}"

class NexusRemoteApp(App):
    def build(self):
        Builder.load_string(KV)
        sm = ScreenManager(transition=FadeTransition(duration=0.2))
        self.dash = DashboardScreen()
        sm.add_widget(self.dash)
        
        # Ciclo de atualização: 1.5 segundos é o ideal para o SM-A23 e Ngrok Free
        Clock.schedule_interval(self.dash.update_data, 1.5)
        
        return sm

if __name__ == '__main__':
    NexusRemoteApp().run()

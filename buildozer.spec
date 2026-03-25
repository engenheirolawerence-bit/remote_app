[app]

# (str) Title of your application
title = NEXUS Remote Oracle

# (str) Package name
package.name = nexusremote

# (str) Package domain (needed for android packaging)
package.domain = ao.nexus

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 21.0

# (list) Application requirements
# MUITO IMPORTANTE: requests e certifi são obrigatórios para o Ngrok/HTTPS
requirements = python3, kivy==2.3.0, requests, certifi, urllib3, idna, charset-normalizer

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
# Necessário para aceder ao link do Ngrok via Wi-Fi ou Dados Móveis
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Presplash background color (Deep Navy para combinar com a UI)
android.presplash_color = #08081a

# (bool) indicates whether the screen should stay on
# Útil para não teres de desbloquear o telemóvel a meio de uma sessão
android.keep_screen_on = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpython.so
android.copy_libs = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1

# buildozer.spec

[app]

# (str) Title of your application
title = Xiaomei Convert

# (str) Package name
package.name = xiaomei_convert

# (str) Package domain (gunakan domain unik Anda)
package.domain = org.xiaomei

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,mp3

# (list) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pygame,vobject

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# Android specific
# (int) Target Android API, gunakan yang terbaru
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (bool) Presplash fullscreen
#android.presplash_fullscreen = 1

# (list) Java classes to add
#android.add_jars =

# (str) Android entry point, default is main.py
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported orientation on Android
#android.orientation = portrait

# (bool) Android logcat
log_level = 2

# (bool) Copy assets (optional)
#android.copy_assets = 1

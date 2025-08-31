[app]

# (str) Title of your app
title = Xiaomei Convert

# (str) Package name
package.name = Xiaomei_Convert

# (str) Package domain (needed for android/ios packaging)
package.domain = org.Xiaomei_Convert

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*/*.jpg

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported android version
android.api = 30

# (int) Android min API to use
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 21

# (str) Release mode (let empty to release version number)
android.release = debug

# (list) Permissions
android.permissions = INTERNET

# (list) features (adds uses-feature -tags to manifest)
android.features = android.hardware.camera,android.hardware.location

# (int) API to use
android.api = 30

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android architecture to use (armeabi-v7l, arm64-v8a, x86)
android.arch = armeabi-v7l

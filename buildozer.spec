[app]
title = JSON to PPT
package.name = jsontoppt
package.domain = org.jsontoppt

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

# Dependencies - adjust based on your actual requirements
requirements = python3,kivy,python-pptx,json

# Android specific
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.arch = arm64-v8a

# iOS specific (if needed)
#ios.kivy_ios_url = https://github.com/kivy/kivy-ios
#ios.kivy_ios_branch = master

# Compilation options
buildozer.warn_on_root = 1

name: Build Kivy APK

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y build-essential libssl-dev zlib1g-dev libffi-dev pkg-config
        pip install buildozer

    - name: Run Buildozer
      run: buildozer android debug

    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: android-apk
        path: bin/*.apk
# This is a basic workflow to help you get started with Actions

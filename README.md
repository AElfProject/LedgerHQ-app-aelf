[![Code style check](https://github.com/blooo-io/LedgerHQ-app-aelf/actions/workflows/lint-workflow.yml/badge.svg)](https://github.com/blooo-io/LedgerHQ-app-aelf/actions/workflows/lint-workflow.yml)
[![Compilation & tests](https://github.com/blooo-io/LedgerHQ-app-aelf/actions/workflows/ci-workflow.yml/badge.svg)](https://github.com/blooo-io/LedgerHQ-app-aelf/actions/workflows/ci-workflow.yml)
[![Sonarcloud](https://github.com/blooo-io/LedgerHQ-app-aelf/actions/workflows/sonarcloud.yml/badge.svg)](https://github.com/blooo-io/LedgerHQ-app-aelf/actions/workflows/sonarcloud.yml)

# Aelf app for Ledger Wallet

## Overview

This app adds support for the Aelf native token to Ledger Nano S/SP/X hardware wallet.

# Prerequisites: Working with the device with VSCode

* [Install Docker](https://docs.docker.com/get-docker/)
* [Install VS Code](https://code.visualstudio.com/download)
* For Linux hosts, install the Ledger Nano [udev rules](https://github.com/LedgerHQ/udev-rules)

You can quickly setup a convenient environment to build and test your application by using the vscode integration and the [ledger-app-dev-tools](https://github.com/LedgerHQ/ledger-app-builder/pkgs/container/ledger-app-builder%2Fledger-app-dev-tools) docker image.

It will allow you, whether you are developing on macOS, Windows or Linux to quickly **build** your apps, **test** them on **Speculos** and **load** them on any supported device.

1. Run Docker.
2. Make sure you have an X11 server running :
    * On Ubuntu Linux, it should be running by default.
    * On macOS, install and launch [XQuartz](https://www.xquartz.org/) (make sure to go to XQuartz > Preferences > Security and check "Allow client connections").
    * On Windows, install and launch [VcXsrv](https://sourceforge.net/projects/vcxsrv/) (make sure to configure it to disable access control).
3. Open a terminal and clone `LedgerHQ-app-aelf` with `git clone https://github.com/blooo-io/LedgerHQ-app-aelf.git`.
4. Open the `LedgerHQ-app-aelf` folder with VSCode.
5. Open the vscode tasks with  `ctrl + shift + b` (`command + shift + b` on a Mac) and run the following actions : Pull and run the [ledger-app-dev-tools](https://github.com/LedgerHQ/ledger-app-builder/pkgs/container/ledger-app-builder%2Fledger-app-dev-tools) docker image by selecting `Run dev-tools image`.
    
# Build
Open the vscode tasks with  `ctrl + shift + b` (`command + shift + b` on a Mac) and run the build for the device model of your choice with `Build app`.
To build the app in debug mode use `Build app [Debug]` instead.

# Clean
Open the vscode tasks with  `ctrl + shift + b` (`command + shift + b` on a Mac) and run the build for the device model of your choice with `Clean build files`.

# Load
Open the vscode tasks with  `ctrl + shift + b` (`command + shift + b` on a Mac) and load your binary on a Ledger device with `Load app on device`.
# Test
## Python
### First install the deps
* Open the vscode tasks with  `ctrl + shift + b` (`command + shift + b` on a Mac) and run the following actions :
    * First install the requirements with `Install tests requirements`.
    * After building, use `Copy from bin to test folder`.
    * To generate golden snapshots for first run, use `Generate snapshots`.
    * Run the tests with `Run functional tests`.
## Unit
Run C tests:
```bash
make -C lib
```

# Chapter 14 - Building the Purrfect Cat Locator App with TensorFlow Object Detection API

Note: All images in this directory, unless specified otherwise, are licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

## Figure List

| Figure number | Description | Notes |
|:---|:---|:---|
| [13-1](https://apps.apple.com/us/app/not-hotdog/id1212457521) | Not Hotdog app listing on the Apple App Store | |
| [13-2](2-tf-lite-stack.png) | High-level architecture of the TensorFlow Lite ecosystem | |
| [13-3](3-android-studio-start.png) | Start screen of Android Studio | |
| [13-4](4-android-studio-open-project.png) | Android Studio “Open Existing Project” screen in the TensorFlow repository | |
| [13-5](5-about-phone-with-arrow.png) | System information screen on an Android phone; select the About Phone option here | |
| [13-6](6-you-are-now-a-dev.png) | The About Phone screen on an Android device | |
| [13-7](7-developer-options-with-arrow.png) | The System information screen showing “Developer options” enabled | |
| [13-8](8-developer-options-usb-debugging.png) | “Developer options” screen on an Android device with USB debugging enabled | |
| [13-9](9-usb-debugging-key.png) | Allow USB debugging on the displayed alert | |
| [13-10](10-debug-toolbar.png) | Debug toolbar in Android Studio | |
| [13-11](11-deployment-target.png) | Select the phone from the deployment target selection screen | |
| [13-12](12-app-screenshot.png) | The app up-and-running app, showing real-time predictions | |
| [13-13](13-firebase-home.png) | Home page of Google Cloud Firebase | |
| [13-14](14-choose-android-app.png) | The Project Overview screen on Google Cloud Firebase | |
| [13-15](15-register-app.png) | App creation screen on Firebase | |
| [13-16](16-add-model.png) | The ML Kit custom models tab | |
| [13-17](17-upload-model.png) | Uploading a TensorFlow Lite model file to Firebase | |
| [13-18](18-two-models.png) | Currently uploaded custom models to Firebase | |
| [13-19](19-create-experiment.png) | A/B testing screen in Firebase where we can create an experiment | |
| [13-20](20-experiment-basics.png) | The Basics section of the screen to create a remote configuration experiment | |
| [13-21](21-experiment-targeting.png) | The Targeting section of the Remote Config screen | |
| [13-22](22-experiment-variants.png) | The Variants section of the Remote Config screen | |
| [13-23](23-available-analytics.png) | Analytics available when setting up an A/B testing experiment | |
| [13-24](24-fritz-real-world-device-perf.png) | Performance of Fritz SDK’s object detection functionality on different mobile devices, relative to the iPhone X | Copyright reserved with [Fritz.ai](https://www.fritz.ai/) |
| [13-25](25-mobile-dev-lifecycle.png) | Mobile AI app development life cycle | |
| [13-26](26-incorrect-feedback.png) | The feedback cycle of an incorrect prediction, generating more training data, leading to an improved model | |
| [13-27](27-release-cycle.png) | The self-evolving model cycle | |
| [13-28](28-lose-it-pizza.jpg) | Snap It feature from Lose It! showing multiple suggestions for a scanned food item | |
| [13-29](29-blurred.jpg) | Portrait effect on Pixel 3, which achieves separation between foreground and background using blurring | |
| [13-30](https://firebase.google.com/docs/ml-kit/ios/detect-faces) | Face contour points identified by ML Kit | |
| [13-31](https://ai.googleblog.com/2018/03/mobile-real-time-video-segmentation.html) | An input image (left) is broken down into its three components layers (R, G, B). The output mask of the previous frame ithen  |appended with these components | |
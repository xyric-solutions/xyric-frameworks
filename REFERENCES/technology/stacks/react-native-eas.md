# react-native-eas

Status: default for mobile

Use this pattern for Xyric iOS and Android apps built with Expo and shipped through EAS.

## Core Stack

| Layer | Choice |
|-------|--------|
| Framework | Expo SDK 54 with React Native |
| Build service | EAS Build |
| Updates | Expo OTA updates |
| Auth | expo-auth-session for OAuth where appropriate |
| Backend communication | HTTPS APIs |

## Use When

- The product needs iOS and Android support.
- Cross-platform velocity matters more than fully custom native implementation.
- The mobile app talks to a backend API hosted separately.

## Consider Another Pattern When

- The app requires native capabilities that Expo cannot support cleanly.
- The project owner explicitly chooses separate native iOS and Android apps.

## Delivery Notes

- Use `eas build --profile preview` for preview builds.
- Use `eas build --profile production` for production builds.
- Store mobile build secrets in EAS secrets or CI secrets, never in git.
- Document backend URLs, auth flow, and release channels in the project `tech-stack.md`.

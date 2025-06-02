# Passwordless Identity Pilot

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

A WebAuthn-based identity project that integrates with AWS Cognito and Azure AD to eliminate passwords and enable phishing-resistant authentication.

## Why Amazon Cares

Builds on AWS-native tools (Cognito) to implement scalable, secure identity flows — a direct contribution to AppSec team priorities around zero-trust and IAM modernization.

## Features
- FIDO2/WebAuthn integration
- MFA/SSO interoperability
- Seamless fallback and browser support

## Stack
- Python, Flask
- AWS Cognito
- Azure AD
- WebAuthn

## Setup

```bash
git clone https://github.com/jeevana-muninarayana/passwordless-auth-pilot
cd passwordless-auth-pilot
pip install -r requirements.txt

# Cybersecurity Take-Home Assignment

## Overview

This repository contains the solution to a cybersecurity-themed take-home assessment, consisting of two major tasks:

---

## Task 1: Data Quality Assessment & Security Interpretation

> **Dataset:**  
> [Cyber Security Attacks – Kaggle Dataset](https://www.kaggle.com/datasets/teamincribo/cyber-security-attacks)  
> A simulated dataset representing various types of cyber attacks including source/destination IPs, protocols, signatures, severity, anomaly scores, and user-agent data.

**Goal:**
- Perform a comprehensive data quality (DQ) assessment across multiple dimensions: completeness, validity, and uniqueness.
- Detect and explain data anomalies.
- Derive actionable security insights based on pattern, signature, reputation (e.g., RBL), and heuristics.

**[Open Task 1 Report →](./Task1.md)**

---

## Task 2: Minimal Gentoo Linux Image Build (DevOps Test)

**Goal:**
Build a minimal Gentoo-based Linux system using a musl-based stage 3 archive. The resulting system should:

- Be as small as possible (minimal total filesystem size).
- Include two users: `root` and one casual user, each with their own home directory.
- Use `busybox` (or similar compact shell) as the default shell for both users, with full script compatibility.
- Successfully run `nmap` version 7.97 or higher with full support for:
  - OS detection (`-O`)
  - Service name detection (`-sV`)
  - Default script scan (`-sC`)
- Be based on **musl**, with multilib disabled.
- Produce an image in **qcow2** or **raw** format that can boot under QEMU full system emulation.

**[Open Task 2 Report →](./Task2.md)**

---
Hani Perkasa |
2025
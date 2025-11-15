---
title:          "Waveform Design for ISAC: Trends and Future Directions"
date:           2025-12-16 00:01:00 +0800
selected:       true
pub:            "IEEE International Conference on Computing, Networking and Communications (ICNC 2026)"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-publication badge-success">Conference</span>'
pub_date:       "2025"
# semantic_scholar_id: 204e3073870fae3d05bcbc2f6a8e263d9b72e776  # use this to retrieve citation count
abstract: >-
  Respiratory monitoring is essential for early detection of various health conditions. Conventional methods rely on contact sensors or clinical equipment, limiting usability for daily healthcare or remote settings. Wireless sensing provides a contactless alternative; however, OFDM-based systems face challenges in resolution and motion robustness, while FMCW radars lack communication capabilities without additional hardware.
  
  In this paper, we make an attempt toward a lightweight Integrated Sensing and Communication (ISAC) system by embedding narrowband FMCW signals into the guard bands of OFDM channels. This re-purposing enables high-resolution sensing and reliable communication simultaneously, without modifying the OFDM structure or introducing extra hardware. We explore trade-offs between sensing accuracy and communication quality, evaluated in terms of Error Vector Magnitude (EVM), under varying FMCW sweep bandwidths and FMCW-to-OFDM power ratios. By integrating signal enhancement techniques and a 1D-CNN classifier, we develop a robust respiratory pattern recognition system resilient to motion interference.
  
  We implement a 28 GHz mmWave testbed with USRPs. Through extensive experimental evaluation, we determine suitable parameter settings for the proposed composite waveform based on EVM performance and alignment with ground truth measurements. Ultimately, our system classifies four respiratory patterns achieves over $98\%$ accuracy, demonstrating its effectiveness and practicality for wireless health monitoring.
cover:          
authors:
  - Xiaochan Xue#
  - Shucheng Yu#
  - Saurabh Parkar 
  - JIarui Li
links:
  Paper: 
  #Code: https://github.com/Luna-Xue
  Demo: 
---

---
title:          "Secure Device Trust Bootstrapping Against Collaborative Signal Modification Attacks"
date:           2023-5-17 00:01:00 +0800
selected:       true
pub:            "IEEE Conference on Computer Communications (INFOCOM)"
# pub_pre:        "Submitted to "
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-publication badge-success">Conference</span>'
pub_date:       "2023"
# semantic_scholar_id: 204e3073870fae3d05bcbc2f6a8e263d9b72e776  # use this to retrieve citation count
abstract: >-
  Bootstrapping security among wireless devices without prior-shared secrets is frequently demanded in emerging wireless and mobile applications. One promising approach for this problem is to utilize in-band physical-layer radio-frequency (RF) signals for authenticated key establishment because of the efficiency and high usability. However, existing in-band authenticated key agreement (AKA) protocols are mostly vulnerable to Man-in-the-Middle (MitM) attacks, which can be launched by modifying the transmitted wireless signals over the air. By annihilating legitimate signals and injecting malicious signals, signal modification attackers are able to completely control the communication channels and spoof victim wireless devices. State-of-the-art (SOTA) techniques addressing such attacks require additional auxiliary hardware or are limited to single attackers. This paper proposes a novel in-band security bootstrapping technique that can thwart colluding signal modification attackers. Different from SOTA solutions, our design is compatible with commodity devices without requiring additional hardware. We achieve this based on the internal randomness of each device that is unpredictable to attackers. Any modification to RF signals will be detected with high probabilities. Extensive security analysis and experimentation on the USRP platform demonstrate the effectiveness of our design under various attack strategies.
cover:          /assets/images/covers/INFOCOM2023.png
authors:
  - Xiaochan Xue#
  - Shucheng Yu#
  - Min Song
links:
  Paper: https://ieeexplore.ieee.org/abstract/document/10229007
  # Code: https://github.com/luost26/academic-homepage
  # Unsplash: https://unsplash.com/photos/sliced-in-half-pineapple--_PLJZmHZzk
---
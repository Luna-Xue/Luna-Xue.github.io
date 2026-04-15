---
title:          "DomusMind: A Benchmark for Evaluating Lifelong Smart Home Agents Under Drift"
date:           2026-03-01 00:01:00 +0800
selected:       true
pub:            "ICLR 2026 Workshop on Lifelong Agents: Learning, Aligning, Evolving."
# pub_pre:        "Submitted to TCCN."
# pub_post:       'Under review.'
pub_last:       ' <span class="badge badge-pill badge-publication badge-primary">Workshop</span>'
pub_date:       "2026"
# semantic_scholar_id: 204e3073870fae3d05bcbc2f6a8e263d9b72e776  # use this to retrieve citation count
abstract: >-
    Smart home agents require continuous operation in non-stationary environments
    where human preferences and device reliability keep evolving. However, dominant evaluation protocols remain episodic and reset-based, failing to capture the
    degradation and recovery dynamics essential for long-term deployment. To address this gap, we introduce DomusMind, a benchmark for evaluating lifelong
    agents under two sources of non-stationarity: preference drift (persona) and tool
    drift (execution). DomusMind instantiates a persistent interaction loop where
    agents balance autonomous execution and user burden. By tracking time-resolved
    metrics across preference, tool, and mixed drift scenarios, our results show that online Theory of Mind (ToM) with uncertainty-gated confirmation provides the most
    robust adaptation overall. Notably, ORACLE persona access fails to mitigate tool
    drift, which identifies execution reliability as a distinct bottleneck. By sweeping a
    confirmation threshold, DomusMind characterizes a success–annoyance frontier
    that enables principled selection of operating points for long-horizon alignment.
cover:          /assets/images/covers/2026_iclrw.png
authors:
  - Rong Xu#
  - Yinxin Wan
  - Xiaochan Xue#

links:
  Paper: https://openreview.net/forum?id=dCBF23RZYJ
  Poster: /assets/files/2026_iclrw_DomusMind.pdf
#   Code: https://github.com/Luna-Xue
#   Demo: 
---

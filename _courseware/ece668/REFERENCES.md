# Related resources and provenance

The v0.1.0 Python implementations, handouts, rubrics, and synthetic generators in
this package were independently written for ECE 668. No source files, datasets,
figures, slides, or assignment wording from the resources below are included.
The package is not a fork or an endorsed edition of those projects. Its MIT
license covers its original files, not the linked resources or the entire website.

These resources informed the selection of teaching topics and remain useful for
students seeking deeper or more realistic implementations:

| Resource | Connection to our curriculum |
| --- | --- |
| [Peterson and Davie, Computer Networks: A Systems Approach](https://github.com/SystemsApproach/book) | Network architecture, transport, congestion, and course reading. The book's CC BY 4.0 terms apply to its material. |
| [Stanford CS244 Bufferbloat assignment](https://2022-cs244.github.io/assignments/a1.pdf) and [starter repository](https://github.com/stanford-cs244/cs244-bufferbloat) | Experimental study of queues, latency, and throughput. Our P1 uses an independently implemented abstract simulator. |
| [Mininet walkthrough](https://mininet.org/walkthrough/) | Possible future Linux network-emulation extension. |
| [UPC Graph Neural Networking Challenge 2022](https://github.com/BNN-UPC/GNNetworkingChallenge/tree/2022_DataCentricAI) | Data-centric network learning and evaluation. Our P2 is a causal time-series forecast, not RouteNet or a GNN replica. |
| [ns3-ai](https://github.com/hust-diangroup/ns3-ai) | Connecting network simulators to learning algorithms. Our P3 has a separate Python environment and no ns-3 dependency. |
| [NVIDIA Sionna scheduling tutorial](https://nvlabs.github.io/sionna/v2.1.0/sys/tutorials/notebooks/Scheduling.html) | Optional wireless scheduling and fairness reading. No Sionna code is included. |
| [NVIDIA NeMo Skills telecom incident tutorial](https://nvidia-nemo.github.io/Skills/tutorials/2026/02/27/teaching-a-model-to-reason-over-telecom-network-incidents/) | Demonstration data, agent training, and baseline evaluation. Our P4 trains a small decision-tree policy, not the tutorial's language model. |
| [Stanford CS329Z project guidance](https://cs329z.stanford.edu/project.html) | Agent evaluation, reproducibility, and staged project delivery. Our project requirements and rubrics are independently written. |
| [OCUDU](https://ocudu.org/) and [OpenISAC-Edge](https://github.com/OpenISAC-Edge/OpenISAC-Edge) | Optional advanced course projects involving RAN telemetry and sensing. No live connector is included. |

If a later version imports code or data, record the exact origin, version, license,
and modifications in a third-party notice file and retain required notices.
References alone do not replace an upstream license or permission to redistribute.

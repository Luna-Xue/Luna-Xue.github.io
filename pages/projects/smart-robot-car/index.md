---
layout: default
title: "Robotic Car Control (UHM VIP)"
header_title: "Robotic Car Control (UHM VIP)"
subtitle: "Physical AI test case for AI-RAN-assisted remote robot driving"
include_header: page_header.html
nav_item: Projects
permalink: /projects/smart-robot-car/
---

This Physical AI project explores remote robot driving with AI-RAN-assisted
communication control through the UHM Vertically Integrated Project (VIP) setting.
The project combines a smart robot car, a gaming steering wheel, and wireless
communication control to help students understand robotics, networking, and
intelligent control through an end-to-end physical system.

Remote robots depend on wireless connectivity for command delivery, video feedback,
and safe operation, especially when latency, congestion, coverage, and changing radio
conditions affect the control loop. This project uses a remotely operated robot to
demonstrate how O-RAN can connect wireless-network intelligence with physical systems
and support future network-aware control.

### Project Focus

- Remote robot driving and control
- Wireless communication for robotics
- AI-assisted network adaptation
- Hands-on learning for UHM VIP and outreach students

### Why O-RAN?

O-RAN introduces an open and software-driven architecture in which xApps can be
deployed on the RAN Intelligent Controller. This enables network functions and
application logic to be developed, updated, and extended without rebuilding the
underlying radio system.

For remote robotics, an xApp can act as a common control and coordination layer that can:

- Process commands from remote operators
- Observe robot and application state
- Incorporate RAN measurements into control decisions
- Apply safety or resource-management policies
- Coordinate multiple robots or wireless devices
- Support future AI-assisted network adaptation

The broader goal is to demonstrate how O-RAN can support applications whose behavior
is closely linked to wireless-network performance.

### Project Setup and Steering Architecture

The prototype uses a PC-based operator station, a ROS2 robot platform, and the
private O-RAN testbed to drive the robot over a cellular link.

- **Operator GUI:** reads steering, acceleration, and braking inputs from the
  Logitech steering wheel and pedals connected to the PC, then sends corresponding
  curl-based commands to the steering xApp.
- **Video control:** plays the robot video stream in the selected mode, including
  <em style="font-weight: 550;">normal</em>, <em style="font-weight: 550;">IR</em>,
  <em style="font-weight: 550;">depth</em>, and <em style="font-weight: 550;">YOLO-assisted</em> views.
- **Steering xApp:** acts as the middle layer between the GUI and the robot. It
  receives driving and video-control commands, converts them into ROS2 commands, and
  forwards them toward the robot.
- **Robot platform:** executes the ROS2 commands and carries a Quectel modem with a
  programmed SIM card for cellular connectivity.
- **O-RAN/gNB path:** carries the translated commands through the USRP-X310 gNB,
  connected to the O-RAN computer, so they can be executed on the robot.

<figure style="max-width: 930px; margin: 1.25rem auto;">
  <img src="/assets/img/jesse-setup.png" alt="Smart Robot Car project setup showing the Logitech steering wheel and pedals, ROSOrin Pro ROS2 robot, and USRP-X310 radio hardware" style="display: block; width: 100%; height: auto; margin: 0 auto; border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, .12);">
  <figcaption style="margin-top: .55rem; text-align: center; font-size: .92rem;">Physical setup with the steering wheel, ROS2 robot platform, and USRP-X310 gNB hardware.</figcaption>
</figure>

### Prototype Demonstration

The implemented dashboard demonstrates end-to-end control through the steering xApp.
It combines the live robot video feed, connection status, camera mode selection,
driving controls, arm servo readouts, key mappings, and command logs in one operator
interface.

<figure style="max-width: 980px; margin: 1.25rem auto;">
  <img src="/assets/img/robotgui.png" alt="Steering xApp dashboard showing live video, status, controls, key bindings, and logs" style="display: block; width: 100%; height: auto; margin: 0 auto; border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, .12);">
  <figcaption style="margin-top: .55rem; text-align: center; font-size: .92rem;">Steering xApp dashboard used for remote robot operation.</figcaption>
</figure>

The right-side status and log pane updates as commands are accepted, camera modes are
changed, and video freshness is reported. The lower control pane tracks live steering,
throttle, brake, and arm-servo values while the robot is operated.

The following demo shows how this interface translates into operation: the robot
motion is shown alongside the operator's point of view during remote driving.

<figure style="max-width: 980px; margin: 1.25rem auto;">
  <iframe src="https://www.youtube.com/embed/M1iJpMhH46o?mute=1" title="Smart Robot Car split-view demo" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="display: block; width: 100%; aspect-ratio: 16 / 9; margin: 0 auto; border: 0; border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, .12);"></iframe>
  <figcaption style="margin-top: .55rem; text-align: center; font-size: .92rem;">Split-view demo showing the robot in motion alongside the operator POV.</figcaption>
</figure>

During operation, the same dashboard can switch the incoming robot feed between
standard camera feedback, sensing views, and AI-assisted perception modes.

<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; max-width: 980px; margin: 1rem auto 0;">
  <figure style="margin: 0;">
    <img src="/assets/img/mode_rgb.png" alt="RGB video mode output from the smart robot car dashboard" style="display: block; width: 100%; height: auto; margin: 0 auto; border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, .12);">
    <figcaption style="margin-top: .55rem; text-align: center; font-size: .92rem;">RGB Mode</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="/assets/img/mode_ir.png" alt="IR video mode output from the smart robot car dashboard" style="display: block; width: 100%; height: auto; margin: 0 auto; border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, .12);">
    <figcaption style="margin-top: .55rem; text-align: center; font-size: .92rem;">IR Mode</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="/assets/img/mode_depth.png" alt="Depth video mode output from the smart robot car dashboard" style="display: block; width: 100%; height: auto; margin: 0 auto; border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, .12);">
    <figcaption style="margin-top: .55rem; text-align: center; font-size: .92rem;">Depth Mode</figcaption>
  </figure>
  <figure style="margin: 0;">
    <img src="/assets/img/mode_yolo.png" alt="YOLO-assisted video mode output from the smart robot car dashboard" style="display: block; width: 100%; height: auto; margin: 0 auto; border-radius: 10px; box-shadow: 0 6px 22px rgba(0, 0, 0, .12);">
    <figcaption style="margin-top: .55rem; text-align: center; font-size: .92rem;">YOLO-Assisted Mode</figcaption>
  </figure>
</div>

---
show: true
width: 4
date: 2021-09-12 00:01:00 +0800
height: 295px
images:
- src: /asserts/images/trip/1.jpg
  title: Photo 1
  desc: Description 1.
  #link: https://picsum.photos/
- src: /asserts/images/trip/2.jpg
  title: Photo 2
  desc: Description 2
- src: /asserts/images/trip/3.jpg
- src: /asserts/images/trip/4.jpg
- src: /asserts/images/trip/5.jpg
- src: /asserts/images/trip/6.jpg
- src: /asserts/images/trip/7.jpg
---

{% include widgets/carousel.html id=page.id images=page.images height=page.height %}

var allTags = [
  'wireless_security',
  'ai_ran',
  'isac',
  'federated_learning',
  'smart_agents',
  'spectrum_wireless'
];

var tags = allTags.slice(); // start with all active

function modifyTag(c) {
  var idx = tags.indexOf(c);
  if (idx === -1) {
    tags.push(c);
  } else {
    tags.splice(idx, 1);
  }

  // If user turns everything off, show all again
  if (tags.length === 0) {
    tags = allTags.slice();
  }
}

function filterSelection(c) {
  if (typeof c === 'string') {
    modifyTag(c);
  } else {
    tags = c;
  }

  // Show/hide publication entries
  var divs = document.getElementsByClassName("filterDiv");
  for (var i = 0; i < divs.length; i++) {
    var isMatch = tags.some(function(tag) {
      return divs[i].className.split(" ").indexOf(tag) > -1;
    });

    if (isMatch) {
      w3AddClass(divs[i], "show");
    } else {
      w3RemoveClass(divs[i], "show");
    }
  }

  // Sync paper tags
  var paperTags = document.getElementsByClassName('paper-tag');
  for (var j = 0; j < paperTags.length; j++) {
    var isActive = tags.some(function(tag) {
      return paperTags[j].className.split(" ").indexOf(tag) > -1;
    });

    if (isActive) {
      w3AddClass(paperTags[j], "active");
    } else {
      w3RemoveClass(paperTags[j], "active");
    }
  }

  // Sync filter buttons
  var container = document.getElementById("myBtnContainer");
  if (!container) return;

  var btns = container.getElementsByClassName("btn");
  for (var k = 0; k < btns.length; k++) {
    var btnTag = getBtnTag(btns[k]);

    if (btnTag && tags.indexOf(btnTag) > -1) {
      w3AddClass(btns[k], "active");
    } else {
      w3RemoveClass(btns[k], "active");
    }
  }
}

function getBtnTag(btn) {
  var classList = btn.className.split(" ");
  for (var i = 0; i < allTags.length; i++) {
    if (classList.indexOf(allTags[i]) > -1) {
      return allTags[i];
    }
  }
  return null;
}

function w3AddClass(element, name) {
  var arr = element.className.split(" ");
  if (arr.indexOf(name) === -1) {
    element.className += " " + name;
  }
}

function w3RemoveClass(element, name) {
  var arr = element.className.split(" ");
  var idx;
  while ((idx = arr.indexOf(name)) > -1) {
    arr.splice(idx, 1);
  }
  element.className = arr.join(" ");
}

// Initialize on page load
filterSelection(allTags.slice());

// Handle URL-based filtering, e.g. ?tags=isac ai_ran
try {
  var urlParams = new URLSearchParams(window.location.search);
  var urlTagsParam = urlParams.get('tags');

  if (urlTagsParam) {
    var urlTags = urlTagsParam.split(' ').filter(function(t) {
      return allTags.indexOf(t) > -1;
    });

    if (urlTags.length > 0) {
      filterSelection(urlTags);
    }
  }
} catch(e) {}
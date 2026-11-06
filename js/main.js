/* ===== PetLogic 寵物知識百科 - Main JS ===== */

// Dropdown toggle
function toggleDropdown() {
  var dropdown = document.getElementById("catDropdown");
  if (dropdown) {
    dropdown.classList.toggle("show");
  }
}

// Close dropdown when clicking outside
document.addEventListener("click", function(e) {
  var dropdown = document.getElementById("catDropdown");
  var dropbtn = document.querySelector(".dropbtn");
  if (dropdown && !dropdown.contains(e.target) && (!dropbtn || !dropbtn.contains(e.target))) {
    dropdown.classList.remove("show");
  }
});

// Category filter for blog page
function filterPosts(category) {
  var cards = document.querySelectorAll(".post-card");
  var buttons = document.querySelectorAll(".cat-btn");

  buttons.forEach(function(btn) {
    btn.classList.remove("active");
    if (btn.getAttribute("data-cat") === category) {
      btn.classList.add("active");
    }
  });

  cards.forEach(function(card) {
    if (category === "all" || card.getAttribute("data-cat") === category) {
      card.style.display = "flex";
    } else {
      card.style.display = "none";
    }
  });
}

// Initialize category filter on page load
document.addEventListener("DOMContentLoaded", function() {
  var activeBtn = document.querySelector(".cat-btn.active");
  if (activeBtn) {
    filterPosts(activeBtn.getAttribute("data-cat"));
  }

  // Set current year in footer
  var yearEl = document.getElementById("current-year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
});

// Lazy loading fallback for older browsers
if ("loading" in HTMLImageElement.prototype === false) {
  var lazyImages = document.querySelectorAll("img[loading='lazy']");
  if ("IntersectionObserver" in window) {
    var imageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var img = entry.target;
          if (img.dataset.src) {
            img.src = img.dataset.src;
          }
          observer.unobserve(img);
        }
      });
    });
    lazyImages.forEach(function(img) { imageObserver.observe(img); });
  }
}

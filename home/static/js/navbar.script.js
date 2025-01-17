function initializeNavbar() {
  //   const navbarFeature = document.querySelector("#features");
  //   const navbarFeatureArrowDown = navbarFeature?.querySelector(".arrow-down");
  const navbarSolution = document.querySelector("#solutions");
  const navbarSolutionArrowDown = navbarSolution.querySelector(".arrow-down");
  const navbarResource = document.querySelector("#resources");
  const navbarResourceArrowDown = navbarResource.querySelector(".arrow-down");
  const modalOverlay = document.querySelector(".modal-overlay");
  // const expandNavbarFeatures = document.querySelector(
  //   ".navbar-features-expand-container"
  // );
  const expandNavbarSolutions = document.querySelector(
    ".navbar-solutions-expand-container"
  );
  const expandNavbarResources = document.querySelector(
    ".navbar-resources-expand-container"
  );

  navbarSolution.addEventListener("click", () => {
    expandNavbarResources.classList.remove("active");
    expandNavbarSolutions.classList.toggle("active");
    navbarResourceArrowDown?.classList.remove("active");
    navbarSolutionArrowDown?.classList.toggle("active");
    navbarResource.classList.remove("active");
    navbarSolution.classList.toggle("active");

    if (modalOverlay) {
      if (expandNavbarSolutions.classList.contains("active")) {
        const navbar = document.getElementById("navbar");
        const y = navbar.getBoundingClientRect().bottom;

        modalOverlay.style.display = "block";
        modalOverlay.style.top = y + "px";
        expandNavbarSolutions.style.top = y + "px";
        document.body.style.overflow = "hidden";
      } else {
        modalOverlay.style.display = "none";
        document.body.style.overflow = "auto";
      }
    }
  });
  navbarResource.addEventListener("click", () => {
    expandNavbarSolutions.classList.remove("active");
    expandNavbarResources.classList.toggle("active");
    navbarSolutionArrowDown?.classList.remove("active");
    navbarResourceArrowDown?.classList.toggle("active");
    navbarResource.classList.toggle("active");
    navbarSolution.classList.remove("active");
    if (modalOverlay) {
      if (expandNavbarResources.classList.contains("active")) {
        const navbar = document.getElementById("navbar");
        const y = navbar.getBoundingClientRect().bottom;

        modalOverlay.style.display = "block";
        modalOverlay.style.top = y + "px";
        expandNavbarResources.style.top = y + "px";
        document.body.style.overflow = "hidden";
      } else {
        modalOverlay.style.display = "none";
        document.body.style.overflow = "auto";
      }
    }
  });

  const hamburgerIcon = document.querySelector(".hamburger-menu-icon");
  const mobileNavbar = document.querySelector(".mobile-navbar");

  hamburgerIcon.addEventListener("click", () => {
    hamburgerIcon.classList.toggle("active");
    mobileNavbar.classList.toggle("active");
    if (hamburgerIcon.classList.contains("active")) {
      hamburgerIcon.src =
        "https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-close-1024.png";
      const navbar = document.getElementById("navbar");
      const y = navbar.getBoundingClientRect().bottom;
      mobileNavbar.style.top = y / 2 + "px";
    } else {
      hamburgerIcon.src =
        "https://w7.pngwing.com/pngs/436/707/png-transparent-hamburger-button-computer-icons-menu-menu-food-text-rectangle.png";
    }
  });

  const toggleSection = (header, content, toggle) => {
    let isExpanded = false;

    header.addEventListener("click", () => {
      isExpanded = !isExpanded;

      if (isExpanded) {
        content.classList.add("show");
        toggle.textContent = "-";
      } else {
        content.classList.remove("show");
        toggle.textContent = "+";
      }
    });
  };

  const navbarItems = document.querySelectorAll(".navbar-item");

  navbarItems.forEach((item) => {
    const header = item.querySelector(".navbar-header");
    const toggle = header.querySelector(".toggle");
    const content = item.querySelector(".navbar-content");

    toggleSection(header, content, toggle);

    const nestedItems = item.querySelectorAll(".nested-item");

    nestedItems.forEach((nestedItem) => {
      const nestedHeader = nestedItem.querySelector(".navbar-header");
      const nestedToggle = nestedHeader.querySelector(".toggle");
      const nestedContent = nestedItem.querySelector(".navbar-content");

      toggleSection(nestedHeader, nestedContent, nestedToggle);
    });
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth >= 1200) {
      mobileNavbar.classList.remove("active");
      hamburgerIcon.style.display = "none";
    }
    if (window.innerWidth < 1200) {
      modalOverlay.style.display = "none";
      document.body.style.overflow = "auto";
      expandNavbarSolutions.classList.remove("active");
      expandNavbarResources.classList.remove("active");
    }
  });

  console.log("hii", document.querySelector("#features"));
}

document.addEventListener("DOMContentLoaded", initializeNavbar);

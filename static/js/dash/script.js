const hamBurger = document.querySelector(".toggle-btn");

// Set default state if it doesn't exist
if (localStorage.getItem("sidebarState") === null) {
  localStorage.setItem("sidebarState", "expanded");
}

// Check the sidebar state on page load
document.addEventListener("DOMContentLoaded", function () {
  if (localStorage.getItem("sidebarState") === "expanded") {
    document.querySelector("#sidebar").classList.add("expand");
  }
});

hamBurger.addEventListener("click", function () {
  const sidebar = document.querySelector("#sidebar");
  sidebar.classList.toggle("expand");

  // Save the state in local storage
  if (sidebar.classList.contains("expand")) {
    localStorage.setItem("sidebarState", "expanded");
  } else {
    localStorage.setItem("sidebarState", "collapsed");
  }
});

// Upload form 
// function showModal() {
//   document.getElementById('modal-overlay').style.display = 'flex';
// }

// function hideModal() {
//   document.getElementById('modal-overlay').style.display = 'none';
// }
